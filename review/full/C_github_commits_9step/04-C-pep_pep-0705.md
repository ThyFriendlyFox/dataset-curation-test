# 4. Python PEP: TypedDict: Read-only items

`C-pep_pep-0705` · [full/C_github_commits_9step](README.md)

Source: <https://github.com/python/peps/blob/545c670f1e986162eb7161d63c944108e504bd09/peps/pep-0705.rst> · License: Public domain / CC0-1.0 (PEP text) · 17 commits touching the file; 10 distinct versions

| step | name | words | citations | similarity to final | provenance |
|---|---|---|---|---|---|
| 0 | title | 3 | 0 | 0.00 | source_title |
| 1 | revision_1 | 1734 | 0 | 0.30 | commit f749a27e89 (2023-03-13) |
| 2 | revision_2 | 4067 | 0 | 0.45 | commit 54f10d9ca4 (2023-10-16) |
| 3 | revision_3 | 4068 | 0 | 0.45 | commit fb526a8822 (2023-10-17) |
| 4 | revision_4 | 3063 | 0 | 0.95 | commit 718157a661 (2023-10-24) |
| 5 | revision_5 | 3269 | 0 | 1.00 | commit 66d1fc80bd (2023-11-28) |
| 6 | revision_6 | 3269 | 0 | 1.00 | commit 9ef5738251 (2024-02-05) |
| 7 | revision_7 | 3268 | 0 | 1.00 | commit 77c09421e5 (2024-09-03) |
| 8 | final | 3273 | 0 | 1.00 | commit 818bac5d1f (2024-09-03) |

<details><summary><b>Step 0 — title</b> (3 words)</summary>

````text
TypedDict: Read-only items
````

</details>

<details><summary><b>Step 1 — revision_1</b> (1734 words)</summary>

````text
Abstract
========

:pep:`589` defines the structural type :class:`~typing.TypedDict` for dictionaries with a fixed set of keys.
As ``TypedDict`` is a mutable type, it is difficult to correctly annotate methods which accept read-only parameters in a way that doesn't prevent valid inputs.
This PEP proposes a type constructor ``typing.TypedMapping`` to support this use case.

Motivation
==========

Representing structured data using (potentially nested) dictionaries with string keys is a common pattern in Python programs. :pep:`589` allows these values to be type checked when the exact type is known up-front, but it is hard to write read-only code code that accepts more specific variants: for instance, where fields may be subtypes or restrict a union of possible types. This is an especially common issue when writing APIs for services, which may support a wide range of input structures, and typically do not need to modify their input.

For illustration, we will try to add type hints to a function ``movie_string``::

    def movie_string(movie: Movie) -> str:
        if movie.get("year") is None:
            return movie["name"]
        else:
            return f'{movie["name"]} ({movie["year"]})'

We could define this ``Movie`` type using a ``TypedDict``::

    from typing import NotRequired, TypedDict

    class Movie(TypedDict):
        name: str
        year: NotRequired[int | None]

But suppose we have another type where year is required::

    class MovieRecord(TypedDict):
        name: str
        year: int

Attempting to pass a ``MovieRecord`` into ``movie_string`` results in the error (using mypy):

.. code-block:: text

    Argument 1 to "movie_string" has incompatible type "MovieRecord"; expected "Movie"

This particular use case should be type-safe, but the type checker correctly stops the
user from passing a ``MovieRecord`` into a ``Movie`` parameter in the general case, because
the ``Movie`` class has mutator methods that could potentially allow the function to break
the type constraints in ``MovieRecord`` (e.g. with ``movie["year"] = None`` or ``del movie["year"]``).
The problem disappears if we don't have mutator methods in ``Movie``. This could be achieved by defining an immutable interface using a :pep:`544` :class:`~typing.Protocol`::

    from typing import Literal, Protocol, overload

    class Movie(Protocol):
        @overload
        def get(self, key: Literal["name"]) -> str: ...

        @overload
        def get(self, key: Literal["year"]) -> int | None: ...

        @overload
        def __getitem__(self, key: Literal["name"]) -> str: ...

        @overload
        def __getitem__(self, key: Literal["year"]) -> int | None: ...

This is very repetitive, easy to get wrong, and is still missing important method definitions like ``__contains__()`` and ``keys()``.

Rationale
=========

The proposed ``TypedMapping`` type allows a straightforward way of defining these types that should be familiar to existing users of ``TypedDict`` and support the cases exemplified above::

    from typing import NotRequired, TypedMapping

    class Movie(TypedMapping):
        name: str
        year: NotRequired[int | None]

In addition to those benefits, by flagging arguments of a function as ``TypedMapping``, it makes explicit not just to typecheckers but also to users that the function is not going to modify its inputs, which is usually a desirable property of a function interface.
Finally, this allows bringing the benefits of ``TypedDict`` to other mapping types that are unrelated to ``dict``.

Specification
=============

A ``TypedMapping`` type defines a protocol with the same methods as :class:`~collections.abc.Mapping`, but with value types determined per-key as with ``TypedDict``.

Notable similarities to ``TypedDict``:

* A ``TypedMapping`` protocol can be declared using class-based or alternative syntax.
* Keys must be strings.
* By default, all specified keys must be present in a ``TypedMapping`` instance. It is possible to override this by specifying totality, or by using ``NotRequired`` from :pep:`655`.
* Methods are not allowed in the declaration (though they may be inherited).

Notable differences from ``TypedDict``:

* The runtime type of a ``TypedMapping`` object is not constrained to be a ``dict``.
* No mutator methods (``__setitem__``, ``__delitem__``, ``update``, etc.) will be generated.
* The ``|`` operator is not supported.
* A class definition defines a ``TypedMapping`` protocol if and only if ``TypedMapping`` appears directly in its class bases.
* Subclasses can narrow value types, in the same manner as other protocols.

As with :pep:`589`, this PEP provides a sketch of how a type checker is expected to support type checking operations involving ``TypedMapping`` and ``TypedDict`` objects, but details are left to implementors. In particular, type compatibility should be based on structural compatibility.


Multiple inheritance and TypedDict
----------------------------------

A type that inherits from a ``TypedMapping`` protocol and from ``TypedDict`` (either directly or indirectly):

* is the structural intersection of its parents, or invalid if no such intersection exists
* instances must be a dict subclass
* adds mutator methods only for fields it explicitly (re)declares

For example::

    class Movie(TypedMapping):
        name: str
        year: int | None

    class MovieRecord(Movie, TypedDict):
        year: int

    movie: MovieRecord = { "name": "Blade Runner",
                           "year": 1982 }
     
    movie["year"] = 1985  # Fine; mutator methods added in definition
    movie["name"] = "Terminator"  # Type check error; "name" mutator not declared

Inheriting, directly or indirectly, from both ``TypedDict`` and ``Protocol`` will continue to fail at runtime, and should continue to be rejected by type checkers.


Multiple inheritance and Protocol
---------------------------------

* A type that inherits from a ``TypedMapping`` protocol and from a ``Protocol`` protocol must satisfy the protocols defined by both, but is not itself a protocol unless it inherits directly from ``TypedMapping`` or ``Protocol``.
* A type that inherits from a ``TypedMapping`` protocol and from ``Protocol`` itself is configured as a ``Protocol``. Methods and properties may be defined; keys may not::

    class A(Movie, Protocol):
        # Declare a mutable property called 'year'
        # This does not affect the dictionary key 'year'
        year: str

* A type that inherits from a ``Protocol`` protocol and from ``TypedMapping`` itself is configured as a ``TypedMapping``. Keys may be defined; methods and properties may not::

    class B(A, TypedMapping):
        # Declare a key 'year'
        # This does not affect the property 'year'
        year: int


Type consistency rules
----------------------

Informally speaking, *type consistency* is a generalization of the is-subtype-of relation to support the ``Any`` type. It is defined more formally in :pep:`483`. This section introduces the new, non-trivial rules needed to support type consistency for ``TypedMapping`` types.

First, any ``TypedMapping`` type is consistent with ``Mapping[str, object]``.
Second, a ``TypedMapping`` or ``TypedDict`` type ``A`` is consistent with ``TypedMapping`` ``B`` if ``A`` is structurally compatible with ``B``. This is true if and only if both of these conditions are satisfied:

* For each key in ``A``, ``B`` has the corresponding key and the corresponding value type in ``B`` is consistent with the value type in ``A``.

* For each required key in ``A``, the corresponding key is required in ``B``.

Discussion:

* Value types behave covariantly, since ``TypedMapping`` objects have no mutator methods. This is similar to container types such as ``Mapping``, and different from relationships between two ``TypedDict`` types. Example::

    class A(TypedMapping):
        x: int | None

    class B(TypedDict):
        x: int

    def f(a: A) -> None:
        print(a['x'] or 0)

    b: B = {'x': 0}
    f(b)  # Accepted by type checker

* A ``TypedDict`` or ``TypedMapping`` type with a required key is consistent with a ``TypedMapping`` type where the same key is a non-required key, again unlike relationships between two ``TypedDict`` types. Example::

    class A(TypedMapping, total=False):
        x: int

    class B(TypedDict):
        x: int

    def f(a: A) -> None:
        print(a.get('x', 0))

    b: B = {'x': 0}
    f(b)  # Accepted by type checker

* A ``TypedMapping`` type ``A`` with no key ``'x'`` is not consistent with a ``TypedMapping`` type with a non-required key ``'x'``, since at runtime the key ``'x'`` could be present and have an incompatible type (which may not be visible through ``A`` due to structural subtyping). This is the same as for ``TypedDict`` types. Example::

    class A(TypedMapping, total=False):
        x: int
        y: int

    class B(TypedMapping, total=False):
        x: int

    class C(TypedMapping, total=False):
        x: int
        y: str

    def f(a: A) -> None:
        print(a.get('y') + 1)

    def g(b: B) -> None:
        f(b)  # Type check error: 'B' incompatible with 'A'

    c: C = {'x': 0, 'y': 'foo'}
    g(c)  # Runtime error: str + int

* A ``TypedMapping`` with all ``int`` values is not consistent with ``Mapping[str, int]``, since there may be additional non-``int`` values not visible through the type, due to structural subtyping. This mirrors ``TypedDict``. Example::

    class A(TypedMapping):
        x: int

    class B(TypedMapping):
        x: int
        y: str

    def sum_values(m: Mapping[str, int]) -> int:
        return sum(m.values())

    def f(a: A) -> None:
        sum_values(a)  # Type check error: 'A' incompatible with Mapping[str, int]

    b: B = {'x': 0, 'y': 'foo'}
    f(b)  # Runtime error: int + str


Backwards Compatibility
=======================

This PEP changes the rules for how ``TypedDict`` behaves (allowing subclasses to
inherit from ``TypedMapping`` protocols in a way that changes the resulting
overloads), so code that inspects ``TypedDict`` types will have to change. This
is expected to mainly affect type-checkers.

The ``TypedMapping`` type will be added to the ``typing_extensions`` module,
enabling its use in older versions of Python.


Security Implications
=====================

There are no known security consequences arising from this PEP.


How to Teach This
=================

Class documentation should be added to the :mod:`typing` module's documentation, using
that for :class:`~collections.abc.Mapping`, :class:`~typing.Protocol` and
:class:`~typing.TypedDict` as examples. Suggested introductory sentence: "Base class
for read-only mapping protocol classes."

This PEP could be added to the others listed in the :mod:`typing` module's documentation.


Reference Implementation
========================

No reference implementation exists yet.


Rejected Alternatives
=====================

Several variations were considered and discarded:

* A ``readonly`` parameter to ``TypedDict``, behaving much like ``TypedMapping`` but with the additional constraint that instances must be dictionaries at runtime. This was discarded as less flexible due to the extra constraint; additionally, the new type nicely mirrors the existing ``Mapping``/``Dict`` types.
* Inheriting from a ``TypedMapping`` subclass and ``TypedDict`` resulting in mutator methods being added for all fields, not just those actively (re)declared in the class body. Discarded as less flexible, and not matching how inheritance works in other cases for ``TypedDict`` (e.g. total=False and total=True do not affect fields not specified in the class body).
* A generic type that removes mutator methods from its parameter, e.g. ``Readonly[MovieRecord]``. This would naturally want to be defined for a wider set of types than just ``TypedDict`` subclasses, and also raises questions about whether and how it applies to nested types. We decided to keep the scope of this PEP narrower.
* Declaring methods directly on a ``TypedMapping`` class. Methods are a kind of property, but declarations on a ``TypedMapping`` class are defining keys, so mixing the two is potentially confusing. Banning methods also makes it very easy to decide whether a ``TypedDict`` subclass can mix in a protocol or not (yes if it's just ``TypedMapping`` superclasses, no if there's a ``Protocol``).


Copyright
=========
This document is placed in the public domain or under the
CC0-1.0-Universal license, whichever is more permissive.
````

</details>

<details><summary><b>Step 2 — revision_2</b> (4067 words)</summary>

````text
Abstract
========

:pep:`589` defines the structural type :class:`~typing.TypedDict` for dictionaries with a fixed set of keys.
As ``TypedDict`` is a mutable type, it is difficult to correctly annotate methods which accept read-only parameters in a way that doesn't prevent valid inputs.
As structural subtypes can add other keys in, it is also difficult for type-checkers to safely define covariant methods like ``update``, or support type narrowing.
This PEP proposes two new ``TypedDict`` flags, ``readonly`` and ``other_keys``, plus an associated type qualifier, ``typing.ReadOnly``.

Motivation
==========

Representing structured data using (potentially nested) dictionaries with string keys is a common pattern in Python programs. :pep:`589` allows these values to be type checked when the exact type is known up-front, but it is hard to write read-only code that accepts more specific variants: for instance, where fields may be subtypes or restrict a union of possible types. This is an especially common issue when writing APIs for services, which may support a wide range of input structures, and typically do not need to modify their input.


Pure functions
--------------

Consider trying to add type hints to a function ``movie_string``::

    def movie_string(movie: Movie) -> str:
        if movie.get("year") is None:
            return movie["name"]
        else:
            return f'{movie["name"]} ({movie["year"]})'

We could define this ``Movie`` type using a ``TypedDict``::

    from typing import NotRequired, TypedDict

    class Movie(TypedDict):
        name: str
        year: NotRequired[int | None]

But suppose we have another type where year is required::

    class MovieRecord(TypedDict):
        name: str
        year: int

Attempting to pass a ``MovieRecord`` into ``movie_string`` results in the error (using mypy):

.. code-block:: text

    Argument 1 to "movie_string" has incompatible type "MovieRecord"; expected "Movie"

This particular use case should be type-safe, but the type checker correctly stops the
user from passing a ``MovieRecord`` into a ``Movie`` parameter in the general case, because
the ``Movie`` class has mutator methods that could potentially allow the function to break
the type constraints in ``MovieRecord`` (e.g. with ``movie["year"] = None`` or ``del movie["year"]``).
The problem disappears if we don't have mutator methods in ``Movie``. This could be achieved by defining an immutable interface using a :pep:`544` :class:`~typing.Protocol`::

    from typing import Literal, Protocol, overload

    class Movie(Protocol):
        @overload
        def get(self, key: Literal["name"]) -> str: ...

        @overload
        def get(self, key: Literal["year"]) -> int | None: ...

        @overload
        def __getitem__(self, key: Literal["name"]) -> str: ...

        @overload
        def __getitem__(self, key: Literal["year"]) -> int | None: ...

This is very repetitive, easy to get wrong, and is still missing important method definitions like ``__contains__()`` and ``keys()``.

Updating nested dicts
---------------------

The structural typing of ``TypedDict`` is supposed to permit writing update functions that only constrain the types of entries they modify::

    class HasTimestamp(TypedDict):
        timestamp: float

    class Logs(TypedDict):
        timestamp: float
        loglines: list[str]

    def update_timestamp(d: HasTimestamp) -> None:
        d["timestamp"] = now()

    def add_logline(logs: Logs, logline: str) -> None:
        logs["loglines"].append(logline)
        update_timestamp(logs)  # Accepted by type checker

However, this no longer works once you start nesting dictionaries::

    class HasTimestampedMetadata(TypedDict):
        metadata: HasTimestamp

    class UserAudit(TypedDict):
        name: str
        metadata: Logs

    def update_metadata_timestamp(d: HasTimestampedMetadata) -> None:
        d["metadata"]["timestamp"] = now()

    def rename_user(d: UserAudit, name: str) -> None:
        d["name"] = name
        update_metadata_timestamp(d)  # Type check error: "metadata" is not of type HasTimestamp

This looks like an error, but is simply due to the (unwanted) ability to overwrite the ``metadata`` entry held by the ``HasTimestampedMetadata`` instance with a different ``HasTimestamp`` instance, that may no longer be a ``UserAudit`` instance.

It is possible to work around this issue with generics (as of Python 3.11), but it is very complicated, requiring a type parameter for every nested dict.


Type discrimination
-------------------

Another common idiom in JSON APIs is to discriminate between mutually exclusive choices with a single-entry dictionary, where the key on the dictionary distinguishes between choices, and constrains the associated value type::

    class Movie(TypedDict):
        name: str
        director: str

    class Book(TypedDict):
        name: str
        author: str

    class EntertainmentMovie(TypedDict):
        movie: Movie

    class EntertainmentBook(TypedDict):
        book: Book

    Entertainment = EntertainmentMovie | EntertainmentBook

Users of this pattern expect type-checkers to allow the following pattern::

    def get_name(entertainment: Entertainment) -> str:
        if "movie" in entertainment:
            return entertainment["movie"]["name"]
        elif "book" in entertainment:
            return entertainment["book"]["name"]
        else:
            # Theoretically unreachable but common defensive coding
            raise ValueError("Unexpected entertainment type")

However, type-checkers will actually raise an error on this code; mypy, for instance, will complain that ``TypedDict "EntertainmentBook" has no key "movie"`` on the third line. This is because ``TypedDict`` does not prevent instances from having keys not specified in the type, and so the check ``"movie" in entertainment`` can return True for an ``EntertainmentBook``.

Users can alternatively use a non-total ``TypedDict`` instead of a union::

    class Entertainment(TypedDict, total=False):
        movie: Movie
        book: Book

This ensures the ``get_name`` example type-checks correctly, but it no longer encodes the constraint that exactly one key must be present, meaning other valid code raises spurious type-check failures. In practice, we tend to see code using types like this either casting to the correct type, with the associated risk of mistakes, or moving the ``in`` checks to dedicated ``TypeGuard`` functions, reducing readability.

Rationale
=========

The first two motivating examples can be solved by removing the ability to update one or more of the entries in a ``TypedDict``. This does not mean the entries are immutable; a reference to the underlying dictionary could still exist with a different but compatible type in which those entries have mutator operations. As such, these are not "final" entries; using this term would risk confusion with final attributes, which are fully immutable. These entries are "readonly".

To support this, we propose adding a new boolean flag to ``TypedDict``, ``readonly``, which when set to True, removes all mutator operations from the type::

    from typing import NotRequired, TypedDict

    class Movie(TypedDict, readonly=True):
        name: str
        director: str

    class Book(TypedDict, readonly=True):
        name: str
        author: str

In addition to these benefits, by flagging arguments of a function as read-only (by using a read-only ``TypedDict`` like ``Movie`` or ``Book``), it makes explicit not just to typecheckers but also to users that the function is not going to modify its inputs, which is usually a desireable property of a function interface.

A new ``typing.ReadOnly`` type qualifier allows removing the ability to mutate individual entries, permitting a mixture of readonly and mutable entries. This is necessary for supporting the second motivating example, updating nested dicts::

    class UserAudit(TypedDict):
        name: str
        metadata: ReadOnly[Logs]

This PEP only proposes making ``ReadOnly`` valid in a ``TypedDict``. A possible future extension would be to support it in additional contexts, such as in protocols.

Finally, to support type discrimination, we add a second flag to ``TypedDict``, ``other_keys``, which when set to ``typing.Never``, prevents instances from holding any key not explicitly listed in the type::

    class EntertainmentMovie(TypedDict, readonly=True, other_keys=Never):
        movie: Movie

    class EntertainmentBook(TypedDict, readonly=True, other_keys=Never):
        book: Book

    Entertainment = EntertainmentMovie | EntertainmentBook

    def get_name(entertainment: Entertainment) -> str:
        if "movie" in entertainment:
            return entertainment["movie"]["name"]
        elif "book" in entertainment:
            return entertainment["book"]["name"]
        else:
            raise ValueError("Unexpected entertainment type")

Note this is a subset of the functionality of the `unmerged proposal of PEP-728 <https://github.com/python/peps/pull/3441>`_.

Specification
=============

``TypedDict`` will gain two new flags: ``other_keys`` and ``readonly``. A new ``typing.ReadOnly`` type qualifier is added.

``other_keys`` flag
-------------------

The optional ``other_keys`` flag to ``TypedDict`` can have the value ``typing.Never``, indicating that instances may only contain keys explicitly listed in the type::

    class Album(TypedDict, other_keys=Never):
        name: str
        year: int

    class AlbumExtra(Album, TypedDict):
        band: str  # Runtime error

Type-checkers may rely on this restriction::

    def album_keys(album: Album) -> Collection[Literal['name', 'year']]:
        # Type checkers may permit this, but should error if Album did not specify `other_keys=Never`
        return album.keys()

Type-checkers should prevent operations that would violate this restriction::

    class AlbumExtra(TypedDict, other_keys=Never):
        name: str
        year: int
        band: str

    album: AlbumExtra = { "name": "Flood", year: 1990, band: "They Might Be Giants" }
    album_keys(album)  # Type check error: extra key 'band'

This PEP does not propose supporting any other values than ``other_keys=Never``. Future or concurrent PEPs may extend this flag to permit other types.

``readonly`` flag
-----------------

The optional boolean ``readonly`` flag to ``TypedDict``, when ``True``, indicates that no mutator operations (``__setitem__``, ``__delitem__``, ``update``, etc.) will be permitted::

    class NamedDict(TypedDict, readonly=True):
        name: str

    def get_name(d: NamedDict) -> str:
        return d["name"]

    def set_name(d: NamedDict, name: str) -> None:
        d["name"] = name  # Type check error: cannot modify a read-only entry

The ``readonly`` flag defaults to ``False``.

``typing.ReadOnly`` flag
------------------------

The ``typing.ReadOnly`` type qualifier is used to indicate that a variable declared in a ``TypedDict`` definition may not be mutated by any operation performed on instances of the ``TypedDict``::

    from typing import ReadOnly

    class BandAndAlbum(TypedDict):
        band: str
        album: ReadOnly[Album]

The ``readonly`` flag is equivalent to marking all entries as ``ReadOnly[]``, guaranteeing no entries are missed by mistake. To avoid potential confusion, it is an error to use both ``readonly=True`` and ``ReadOnly[]``::

    class Band(TypedDict, readonly=True):
        name: ReadOnly[str]  # Runtime error: redundant ReadOnly qualifier
        members: Collection[str]

Alternative functional syntax
-----------------------------

The :pep:`alternative functional syntax <589#alternative-syntax>` for TypedDict also supports these features::

   EntityBand = TypedDict('EntityBand', {'band': Band}, readonly=True, other_keys=Never)
   BandAndAlbum = TypedDict(`BandAndAlbum', {'band': str, 'album': ReadOnly[Album]})

Interaction with other special types
------------------------------------

``ReadOnly[]`` can be used with ``Required[]``, ``NotRequired[]`` and ``Annotated[]``, in any nesting order:

::

    class Movie(TypedDict):
        title: ReadOnly[Required[str]]  # OK
        year: ReadOnly[NotRequired[Annotated[int, ValueRange(-9999, 9999)]]]  # OK

::

    class Movie(TypedDict):
        title: Required[ReadOnly[str]]  # OK
        year: Annotated[NotRequired[ReadOnly[int]], ValueRange(-9999, 9999)]  # OK

This is consistent with the behavior introduced in :pep:`655`.

Inheritance
-----------

To avoid potential confusion, it is an error to have a read-only type extend a non-read-only type::

    class BandAlbumAndLabel(BandAndAlbum, readonly=True):  # Runtime error
        label: str


It is also an error to have a type without ``other_keys`` specified extend a type with ``other_keys=Never``::

    class NamedDict(TypedDict, readonly=True):
        name: str

    class Person(NamedDict):  # Runtime error
        age: float

It is valid to have a non-read-only type extend a read-only one. The subclass will not be read-only, but any keys not redeclared in the subclass will remain read-only::

    class Album(NamedDict, TypedDict):
        year: int

    album: Album = { name: "Flood", year: 1990 }
    album["year"] = 1973  # OK
    album["name"] = "Dark Side Of The Moon"  # Type check error: "name" is read-only

Subclasses can redeclare read-only entries as non-read-only, allowing them to be mutated::

    class Album(NamedDict, TypedDict):
        name: str
        year: int

    album: Album = { name: "Flood", year: 1990 }
    album["year"] = 1973  # OK
    album["name"] = "Dark Side Of The Moon"  # Also OK now

Subclasses can narrow value types of read-only entries::

    class AlbumCollection(TypedDict, readonly=True):
        albums: Collection[Album]

    class RecordShop(AlbumCollection, TypedDict):
        name: str
        albums: list[Album]

Subclasses can also require keys that are read-only but not required in the superclass::

    class OptionalName(TypedDict, readonly=True):
        name: NotRequired[str]

    class Person(OptionalName, TypedDict):
        name: Required[str]

    person: Person = {}  # Type check error: "name" required

Note that these are just consequences of structural typing, but they are highlighted here as the behavior now differs from the rules specified in :pep:`589`.

Finally, subclasses can have ``other_keys=Never`` even if the superclass does not::

    class Person(OptionalName, other_keys=Never):
        name: Required[str]

Type consistency
----------------

*This section updates the type consistency rules introduced in* :pep:`589` *to cover the new features in this PEP. In particular, any pair of types that do not use the new features will be consistent under these new rules if (and only if) they were already consistent.*

A TypedDict type with ``other_keys=Never`` is consistent with ``Mapping[str, V]``, where ``V`` is the union of all its value types. For instance, the following type is consistent with ``Mapping[str, int | str]``::

    class Person(TypedDict, other_keys=Never):
        name: str
        age: int

A TypedDict type ``A`` is consistent with TypedDict ``B`` if ``A`` is structurally compatible with ``B``. This is true if and only if all of the following are satisfied:

* For each key in ``B``, ``A`` has the corresponding key and the corresponding value type in ``A`` is consistent with the value type in ``B``, unless the key in ``B`` is of type ``ReadOnly[NotRequired[Any]]``, in which case it may be missing in ``A`` provided ``A`` allows other keys.
* For each non-read-only key in ``B``, the corresponding value type in ``B`` is also consistent with the corresponding value type in ``A``.
* For each required key in ``B``, the corresponding key is required in ``A``.
* For each non-read-only, non-required key in ``B``, the corresponding key is not required in ``A``.
* If ``B`` does not allow other keys, then ``A`` does not allow other keys.
* If ``B`` does not allow other keys, then for each key in ``A``, ``B`` has the corresponding key.

Discussion:

* All non-specified keys in a type that allows other keys are implicitly of type ``ReadOnly[NotRequired[Any]]`` (or ``ReadOnly[NotRequired[Unknown]]`` in pyright).

* Read-only value types behave covariantly, as they cannot be mutated. This is similar to container types such as ``Sequence``, and different from non-read-only value types, which behave invariantly. Example::

    class A(TypedDict, readonly=True):
        x: int | None

    class B(TypedDict):
        x: int

    def f(a: A) -> None:
        print(a['x'] or 0)

    b: B = {'x': 1}
    f(b)  # Accepted by type checker

* A TypedDict type ``A`` with no explicit key ``'x'`` that allows other keys is not consistent with a TypedDict type with a non-required key ``'x'``, since at runtime the key ``'x'`` could be present and have an incompatible type (which may not be visible through ``A`` due to structural subtyping). The only exception to this rule is if ``'x'`` is non-required, read-only and of type ``object`` (or ``Any`` or pylance's ``Unknown``).

* A TypedDict type ``A`` with no key ``'x'`` that does not allow other keys may be consistent with a TypedDict type with a read-only, non-required key ``'x'``. Example::

    class A(TypedDict, total=False, readonly=True):
        y: int

    class B(TypedDict, other_keys=Never):
        x: int

    def f(a: A) -> int:
       return a.get("y", 0)

    def g(b: B) -> None:
       b["x"] = f(b)  # Accepted by type checker

Union Operation
---------------

The union operation creates a new dictionary with the merged keys and values of its two operands. As such, the result should be consistent with any type that can hold the possible key-value pairs, not just types compatible with the operand types. For example::

    class A(TypedDict, readonly=True, other_keys=Never):
        x: int

    class B(TypedDict, total=False, readonly=True, other_keys=Never):
        x: str

    class C(TypedDict):
        x: int | str

    def union_a_b(a: A, b: B) -> C:
        # Accepted by type-checker, even though C is not read-only and
        # allows other keys:
        return a | b

This is different from the usual compatibility rules, where the result of an operation has a defined type which the variable it is assigned to must be consistent with. A similar situation occurs with ``TypedDict`` and ``copy()`` or ``deepcopy()``.

If the union of two TypedDict objects of type ``A`` and ``B`` are assigned to a TypedDict of type ``C``, the type checker should verify that:

* if ``C`` does not allow other keys, neither ``A`` nor ``B`` allow other keys
* if ``C`` does not allow other keys, it contains all keys found in either ``A`` or ``B``
* if a key ``'x'`` is found in ``A`` and ``C``, its type in ``A`` is consistent with its type in ``C``.
* if a key ``'x'`` is found in ``B`` and ``C``, its type in ``B`` is consistent with its type in ``C``.
* if a key ``'x'`` is required in ``C``, it is required in either ``A`` or ``B``.

Notes:

* The read-only status of the keys does not matter. A key can be read-only on just ``A``, just ``B``, or just ``C``, or any combination.
* A key found on ``A`` or ``B`` may be missed off ``C`` if it allows other keys. Type-checkers may however choose to flag this edge-case with a warning or error in some circumstances, if it is found to be a source of mistakes.

Update Operations
-----------------

Previously, ``clear()`` and ``popitem()`` were rejected by type checkers on TypedDict objects, as they could remove required keys, some of which may not be directly visible because of structural subtyping. However, these methods should be allowed on TypedDicts objects with all keys non-read-only and non-required and with no other keys allowed::

    class A(TypedDict, total=False, other_keys=Never):
        x: int
        y: str

    a: A = { "x": 1, "y": "foo" }
    a.popitem()  # Accepted by type checker
    a.clear()  # Accepted by type checker

``update`` has been difficult to type correctly due to the open nature of TypedDict objects. Keys not specified on the type could still be present (and constrained) due to structural subtyping, meaning type safety could be accidentally violated. For instance::

    class B(TypedDict, total=False):
        x: int

    def update_b(b1: B, b2: B) -> None:
        b1.update(b2)

    class C(B, TypedDict, total=False):
        y: int

    class D(B, TypedDict, total=False):
        y: str

    c: C = { "x": 1, "y": 2 }
    d: D = { "x": 3, "y": "foo" }
    update_b(c, d)  # c is no longer a C at runtime

Both mypy and pyright currectly permit this usage, however, as the only viable alternative has been to prevent calling ``update`` at all.

With the addition of ``other_keys``, it becomes possible to more accurately type the update method:

* Declare a new read-only TypedDict type that does not allow other keys
* Copy all non-read-only entries to it
* Make all entries read-only and non-required
* Union this with an iterable of matching key-value pairs

For instance::

    class Example(TypedDict):
        a: int
        b: NotRequired[str]
        c: ReadOnly[int]

    class ExampleUpdateDict(TypedDict, total=False, readonly=True, other_keys=Never):
        a: int
        b: str
        # c is not present as it is read-only in Example

    ExampleUpdateEntry = tuple[Literal["a"], int] | tuple[Literal["b"], str]
    ExampleUpdate = ExampleUpdateDict | Iterable[ExampleUpdateEntry]

Type checkers should permit any type compatible with this TypedDict to be passed into the update operation. As with :pep:`589`, they may choose to continue permitting TypedDict types that allow other keys as well, to avoid generating false positives.

Keyword argument typing
-----------------------

:pep:`692` introduced ``Unpack`` to annotate ``**kwargs`` with a ``TypedDict``. Marking one or more of the entries of a ``TypedDict`` used in this way as read-only will have no effect on the type signature of the method, since all keyword arguments are read-only by design in Python. However, it *will* prevent the entry from being modified in the body of the function::

    class Args(TypedDict):
        key1: int
        key2: str

    class ReadonlyArgs(TypedDict, readonly=True):
        key1: int
        key2: str

    class Function(Protocol):
        def __call__(self, **kwargs: Unpack[Args]) -> None: ...

    def impl(self, **kwargs: Unpack[ReadonlyArgs]) -> None:
        kwargs["key1"] = 3  # Type check error: key1 is readonly

    fn: Function = impl  # Accepted by type checker: function signatures are identical


Backwards compatibility
=======================

This PEP adds new features to ``TypedDict``, so code that inspects ``TypedDict`` types will have to change to support types using the new features. This is expected to mainly affect type-checkers.

Security implications
=====================

There are no known security consequences arising from this PEP.

How to Teach This
=================

Suggestion for changes to the :mod:`typing` module, in line with current practice:

* Add this PEP to the others listed.
* Add ``typing.ReadOnly``, linked to TypedDict and this PEP.
* Add the following text to the TypedDict entry:

By default, keys not specified in a TypedDict may still be present. Instances can be restricted to only the named keys with the ``other_keys`` flag. *insert example, perhaps using ``in`` to illustrate the benefit*

Individual keys can be excluded from mutate operations using ReadOnly, allowing them to be read but not changed. This is useful when the exact type of the value is not known yet, and so modifying it would break structural subtypes. *insert example*

If all keys on a TypedDict should be read-only, the ``readonly`` flag can be used as a shorthand. *insert example*

Reference Implementation
========================

No complete reference implementation exists yet. pyright 1.1.310 ships with a partial implementation of the ReadOnly qualifier.

Rejected Alternatives
=====================

A TypedMapping protocol type
----------------------------

An earlier version of :pep:`705` proposed a ``TypedMapping`` protocol type, behaving much like a read-only TypedDict but without the constraint that the runtime type be a ``dict``. The behavior described in the current version of this PEP could then be obtained by inheriting a TypedDict from a TypedMapping. This has been set aside for now as more complex, without a strong use-case motivating the additional complexity.

A higher-order Readonly type
----------------------------

A generalized higher-order type could be added that removes mutator methods from its parameter, e.g. ``ReadOnly[MovieRecord]``. For a TypedDict, this would be like adding ``readonly=True`` to the declaration. This would naturally want to be defined for a wider set of types than just TypedDict subclasses, and also raises questions about whether and how it applies to nested types. We decided to keep the scope of this PEP narrower.

Preventing other keys with the typing.final decorator
-----------------------------------------------------

Instead of adding an ``other_keys`` flag to TypedDict, treat classes decorated with :func:`~typing.final` as disallowing other keys. This makes intuitive sense for TypedDict as it stands now: preventing adding any other keys guarantees no other types will be structurally compatible, so it is effectively final. There is also partial support for this idiom in mypy and pyright, which both use it as a way to achieve type discrimination. However, if any keys are read-only, preventing adding any other keys does **not** make the type final any more, so using the decorator this way seems incorrect. For example::

    class Foo: ...
    class Bar(Foo): ...

    @final
    class FooHolder(TypedDict, readonly=True):
      item: Foo

    @final
    class BarHolder(FooHolder, readonly=True):
      item: Bar

Extending a ``TypedDict`` to refine the types is a reasonable feature, but the above code looks like it should raise a runtime error. Should ``@final`` be modified to allow inheritance? Should users be prevented from using this pattern?

More context for this can be found on `pyright issue 5254 <https://github.com/microsoft/pyright/issues/5254>`_.

We recommend type checkers treat decorating a TypedDict type with final as identical to setting ``other_keys=Never``, if they continue to support the idiom for backwards compatibility, but reject any use of final on a TypedDict with read-only keys. Once ``other_keys`` is adopted, they may also wish to deprecate use of final on TypedDicts entirely.

Using different casing for ``readonly`` keyword or ``ReadOnly`` type
--------------------------------------------------------------------

It appears to be common convention to put an initial caps onto words separated by a dash when converting to CamelCase, but to drop the dash completely when converting to snake_case. Django uses ``readonly``, for instance. This appears consistent with the definition of both on Wikipedia: snake_case replaces spaces with dashes, while CamelCase uppercases the first letter of each word. That said, more examples or counterexamples, ideally from the core Python libraries, or better explicit guidance on the convention, would be greatly appreciated.

Mandate unsound type narrowing
------------------------------

The main use-case we are aware of for ``other_keys=Never`` (and the current workaround of final-decorated TypedDict types) is to simplify type discrimination, as shown in the motivation section.

By comparison, TypeScript handles this edge-case by ignoring the possibility of instances of one type in the union having undeclared keys. If a variable is known to be of type ``A | B`` and an ``in`` check is done using a key not explicitly declared on ``B``, it is assumed no instance of ``B`` will pass that check. While technically unsound, this a common enough idiom that it could fall under the recommendation in :pep:`589` that "potentially unsafe operations may be accepted if the alternative is to generate false positive errors for idiomatic code".

This user request has been rejected multiple times by type checkers, however, suggesting the community prefers strict type-safety over idiomatic code here.

Make the ``other_keys`` flag a boolean
--------------------------------------

Since ``other_keys`` can only effectively take two values, ``Never`` or absent, it was originally proposed as a boolean flag, with ``other_keys=False`` equivalent to the current ``other_keys=Never``. However, the `unmerged proposal of PEP-728 <https://github.com/python/peps/pull/3441>`_ provides equivalent functionality when restricting other types to ``Never``, so this proposal was updated to use comparable syntax, to make it clearer how the proposals intersect.

Use a reserved ``__extra__`` key
--------------------------------

The `unmerged proposal of PEP-728 <https://github.com/python/peps/pull/3441>`_ proposes different syntax for disallowing other keys::

    class EntertainmentMovie(TypedDict, readonly=True):
        movie: Movie
        __extra__: Never

This new key does not function like other keys -- for instance, it is implicitly ``NotRequired`` but cannot be explicitly marked as such. The author of this PEP prefers the asymmetry of using a keyword argument to set expectations that it does not behave like other key declarations, and others have provided similar feedback on the PR.

However, this PEP will be updated to match whatever syntax the PEP-728 author decides to go with.

Leave other_keys to PEP-728
---------------------------

This PEP could drop the ``other_keys`` proposal entirely rather than propose a limited subset of it. However, as this PEP affects the unofficial status-quo of using final to disallow other keys, it seems important to both highlight that issue and propose a solution.


Copyright
=========
This document is placed in the public domain or under the
CC0-1.0-Universal license, whichever is more permissive.
````

</details>

<details><summary><b>Step 3 — revision_3</b> (4068 words)</summary>

````text
Abstract
========

:pep:`589` defines the structural type :class:`~typing.TypedDict` for dictionaries with a fixed set of keys.
As ``TypedDict`` is a mutable type, it is difficult to correctly annotate methods which accept read-only parameters in a way that doesn't prevent valid inputs.
As structural subtypes can add other keys in, it is also difficult for type-checkers to safely define covariant methods like ``update``, or support type narrowing.
This PEP proposes two new ``TypedDict`` flags, ``readonly`` and ``other_keys``, plus an associated type qualifier, ``typing.ReadOnly``.

Motivation
==========

Representing structured data using (potentially nested) dictionaries with string keys is a common pattern in Python programs. :pep:`589` allows these values to be type checked when the exact type is known up-front, but it is hard to write read-only code that accepts more specific variants: for instance, where fields may be subtypes or restrict a union of possible types. This is an especially common issue when writing APIs for services, which may support a wide range of input structures, and typically do not need to modify their input.


Pure functions
--------------

Consider trying to add type hints to a function ``movie_string``::

    def movie_string(movie: Movie) -> str:
        if movie.get("year") is None:
            return movie["name"]
        else:
            return f'{movie["name"]} ({movie["year"]})'

We could define this ``Movie`` type using a ``TypedDict``::

    from typing import NotRequired, TypedDict

    class Movie(TypedDict):
        name: str
        year: NotRequired[int | None]

But suppose we have another type where year is required::

    class MovieRecord(TypedDict):
        name: str
        year: int

Attempting to pass a ``MovieRecord`` into ``movie_string`` results in the error (using mypy):

.. code-block:: text

    Argument 1 to "movie_string" has incompatible type "MovieRecord"; expected "Movie"

This particular use case should be type-safe, but the type checker correctly stops the
user from passing a ``MovieRecord`` into a ``Movie`` parameter in the general case, because
the ``Movie`` class has mutator methods that could potentially allow the function to break
the type constraints in ``MovieRecord`` (e.g. with ``movie["year"] = None`` or ``del movie["year"]``).
The problem disappears if we don't have mutator methods in ``Movie``. This could be achieved by defining an immutable interface using a :pep:`544` :class:`~typing.Protocol`::

    from typing import Literal, Protocol, overload

    class Movie(Protocol):
        @overload
        def get(self, key: Literal["name"]) -> str: ...

        @overload
        def get(self, key: Literal["year"]) -> int | None: ...

        @overload
        def __getitem__(self, key: Literal["name"]) -> str: ...

        @overload
        def __getitem__(self, key: Literal["year"]) -> int | None: ...

This is very repetitive, easy to get wrong, and is still missing important method definitions like ``__contains__()`` and ``keys()``.

Updating nested dicts
---------------------

The structural typing of ``TypedDict`` is supposed to permit writing update functions that only constrain the types of entries they modify::

    class HasTimestamp(TypedDict):
        timestamp: float

    class Logs(TypedDict):
        timestamp: float
        loglines: list[str]

    def update_timestamp(d: HasTimestamp) -> None:
        d["timestamp"] = now()

    def add_logline(logs: Logs, logline: str) -> None:
        logs["loglines"].append(logline)
        update_timestamp(logs)  # Accepted by type checker

However, this no longer works once you start nesting dictionaries::

    class HasTimestampedMetadata(TypedDict):
        metadata: HasTimestamp

    class UserAudit(TypedDict):
        name: str
        metadata: Logs

    def update_metadata_timestamp(d: HasTimestampedMetadata) -> None:
        d["metadata"]["timestamp"] = now()

    def rename_user(d: UserAudit, name: str) -> None:
        d["name"] = name
        update_metadata_timestamp(d)  # Type check error: "metadata" is not of type HasTimestamp

This looks like an error, but is simply due to the (unwanted) ability to overwrite the ``metadata`` entry held by the ``HasTimestampedMetadata`` instance with a different ``HasTimestamp`` instance, that may no longer be a ``UserAudit`` instance.

It is possible to work around this issue with generics (as of Python 3.11), but it is very complicated, requiring a type parameter for every nested dict.


Type discrimination
-------------------

Another common idiom in JSON APIs is to discriminate between mutually exclusive choices with a single-entry dictionary, where the key on the dictionary distinguishes between choices, and constrains the associated value type::

    class Movie(TypedDict):
        name: str
        director: str

    class Book(TypedDict):
        name: str
        author: str

    class EntertainmentMovie(TypedDict):
        movie: Movie

    class EntertainmentBook(TypedDict):
        book: Book

    Entertainment = EntertainmentMovie | EntertainmentBook

Users of this pattern expect type-checkers to allow the following pattern::

    def get_name(entertainment: Entertainment) -> str:
        if "movie" in entertainment:
            return entertainment["movie"]["name"]
        elif "book" in entertainment:
            return entertainment["book"]["name"]
        else:
            # Theoretically unreachable but common defensive coding
            raise ValueError("Unexpected entertainment type")

However, type-checkers will actually raise an error on this code; mypy, for instance, will complain that ``TypedDict "EntertainmentBook" has no key "movie"`` on the third line. This is because ``TypedDict`` does not prevent instances from having keys not specified in the type, and so the check ``"movie" in entertainment`` can return True for an ``EntertainmentBook``.

Users can alternatively use a non-total ``TypedDict`` instead of a union::

    class Entertainment(TypedDict, total=False):
        movie: Movie
        book: Book

This ensures the ``get_name`` example type-checks correctly, but it no longer encodes the constraint that exactly one key must be present, meaning other valid code raises spurious type-check failures. In practice, we tend to see code using types like this either casting to the correct type, with the associated risk of mistakes, or moving the ``in`` checks to dedicated ``TypeGuard`` functions, reducing readability.

Rationale
=========

The first two motivating examples can be solved by removing the ability to update one or more of the entries in a ``TypedDict``. This does not mean the entries are immutable; a reference to the underlying dictionary could still exist with a different but compatible type in which those entries have mutator operations. As such, these are not "final" entries; using this term would risk confusion with final attributes, which are fully immutable. These entries are "readonly".

To support this, we propose adding a new boolean flag to ``TypedDict``, ``readonly``, which when set to True, removes all mutator operations from the type::

    from typing import NotRequired, TypedDict

    class Movie(TypedDict, readonly=True):
        name: str
        director: str

    class Book(TypedDict, readonly=True):
        name: str
        author: str

In addition to these benefits, by flagging arguments of a function as read-only (by using a read-only ``TypedDict`` like ``Movie`` or ``Book``), it makes explicit not just to typecheckers but also to users that the function is not going to modify its inputs, which is usually a desireable property of a function interface.

A new ``typing.ReadOnly`` type qualifier allows removing the ability to mutate individual entries, permitting a mixture of readonly and mutable entries. This is necessary for supporting the second motivating example, updating nested dicts::

    class UserAudit(TypedDict):
        name: str
        metadata: ReadOnly[Logs]

This PEP only proposes making ``ReadOnly`` valid in a ``TypedDict``. A possible future extension would be to support it in additional contexts, such as in protocols.

Finally, to support type discrimination, we add a second flag to ``TypedDict``, ``other_keys``, which when set to ``typing.Never``, prevents instances from holding any key not explicitly listed in the type::

    class EntertainmentMovie(TypedDict, readonly=True, other_keys=Never):
        movie: Movie

    class EntertainmentBook(TypedDict, readonly=True, other_keys=Never):
        book: Book

    Entertainment = EntertainmentMovie | EntertainmentBook

    def get_name(entertainment: Entertainment) -> str:
        if "movie" in entertainment:
            return entertainment["movie"]["name"]
        elif "book" in entertainment:
            return entertainment["book"]["name"]
        else:
            raise ValueError("Unexpected entertainment type")

Note this is a subset of the functionality of the `unmerged proposal of PEP-728 <https://github.com/python/peps/pull/3441>`_.

Specification
=============

``TypedDict`` will gain two new flags: ``other_keys`` and ``readonly``. A new ``typing.ReadOnly`` type qualifier is added.

``other_keys`` flag
-------------------

The optional ``other_keys`` flag to ``TypedDict`` can have the value ``typing.Never``, indicating that instances may only contain keys explicitly listed in the type::

    class Album(TypedDict, other_keys=Never):
        name: str
        year: int

    class AlbumExtra(Album, TypedDict):
        band: str  # Runtime error

Type-checkers may rely on this restriction::

    def album_keys(album: Album) -> Collection[Literal['name', 'year']]:
        # Type checkers may permit this, but should error if Album did not specify `other_keys=Never`
        return album.keys()

Type-checkers should prevent operations that would violate this restriction::

    class AlbumExtra(TypedDict, other_keys=Never):
        name: str
        year: int
        band: str

    album: AlbumExtra = { "name": "Flood", year: 1990, band: "They Might Be Giants" }
    album_keys(album)  # Type check error: extra key 'band'

This PEP does not propose supporting any other values than ``other_keys=Never``. Future or concurrent PEPs may extend this flag to permit other types.

``readonly`` flag
-----------------

The optional boolean ``readonly`` flag to ``TypedDict``, when ``True``, indicates that no mutator operations (``__setitem__``, ``__delitem__``, ``update``, etc.) will be permitted::

    class NamedDict(TypedDict, readonly=True):
        name: str

    def get_name(d: NamedDict) -> str:
        return d["name"]

    def set_name(d: NamedDict, name: str) -> None:
        d["name"] = name  # Type check error: cannot modify a read-only entry

The ``readonly`` flag defaults to ``False``.

``typing.ReadOnly`` type qualifier
----------------------------------

The ``typing.ReadOnly`` type qualifier is used to indicate that a variable declared in a ``TypedDict`` definition may not be mutated by any operation performed on instances of the ``TypedDict``::

    from typing import ReadOnly

    class BandAndAlbum(TypedDict):
        band: str
        album: ReadOnly[Album]

The ``readonly`` flag is equivalent to marking all entries as ``ReadOnly[]``, guaranteeing no entries are missed by mistake. To avoid potential confusion, it is an error to use both ``readonly=True`` and ``ReadOnly[]``::

    class Band(TypedDict, readonly=True):
        name: ReadOnly[str]  # Runtime error: redundant ReadOnly qualifier
        members: Collection[str]

Alternative functional syntax
-----------------------------

The :pep:`alternative functional syntax <589#alternative-syntax>` for TypedDict also supports these features::

   EntityBand = TypedDict('EntityBand', {'band': Band}, readonly=True, other_keys=Never)
   BandAndAlbum = TypedDict(`BandAndAlbum', {'band': str, 'album': ReadOnly[Album]})

Interaction with other special types
------------------------------------

``ReadOnly[]`` can be used with ``Required[]``, ``NotRequired[]`` and ``Annotated[]``, in any nesting order:

::

    class Movie(TypedDict):
        title: ReadOnly[Required[str]]  # OK
        year: ReadOnly[NotRequired[Annotated[int, ValueRange(-9999, 9999)]]]  # OK

::

    class Movie(TypedDict):
        title: Required[ReadOnly[str]]  # OK
        year: Annotated[NotRequired[ReadOnly[int]], ValueRange(-9999, 9999)]  # OK

This is consistent with the behavior introduced in :pep:`655`.

Inheritance
-----------

To avoid potential confusion, it is an error to have a read-only type extend a non-read-only type::

    class BandAlbumAndLabel(BandAndAlbum, readonly=True):  # Runtime error
        label: str


It is also an error to have a type without ``other_keys`` specified extend a type with ``other_keys=Never``::

    class NamedDict(TypedDict, readonly=True):
        name: str

    class Person(NamedDict):  # Runtime error
        age: float

It is valid to have a non-read-only type extend a read-only one. The subclass will not be read-only, but any keys not redeclared in the subclass will remain read-only::

    class Album(NamedDict, TypedDict):
        year: int

    album: Album = { name: "Flood", year: 1990 }
    album["year"] = 1973  # OK
    album["name"] = "Dark Side Of The Moon"  # Type check error: "name" is read-only

Subclasses can redeclare read-only entries as non-read-only, allowing them to be mutated::

    class Album(NamedDict, TypedDict):
        name: str
        year: int

    album: Album = { name: "Flood", year: 1990 }
    album["year"] = 1973  # OK
    album["name"] = "Dark Side Of The Moon"  # Also OK now

Subclasses can narrow value types of read-only entries::

    class AlbumCollection(TypedDict, readonly=True):
        albums: Collection[Album]

    class RecordShop(AlbumCollection, TypedDict):
        name: str
        albums: list[Album]

Subclasses can also require keys that are read-only but not required in the superclass::

    class OptionalName(TypedDict, readonly=True):
        name: NotRequired[str]

    class Person(OptionalName, TypedDict):
        name: Required[str]

    person: Person = {}  # Type check error: "name" required

Note that these are just consequences of structural typing, but they are highlighted here as the behavior now differs from the rules specified in :pep:`589`.

Finally, subclasses can have ``other_keys=Never`` even if the superclass does not::

    class Person(OptionalName, other_keys=Never):
        name: Required[str]

Type consistency
----------------

*This section updates the type consistency rules introduced in* :pep:`589` *to cover the new features in this PEP. In particular, any pair of types that do not use the new features will be consistent under these new rules if (and only if) they were already consistent.*

A TypedDict type with ``other_keys=Never`` is consistent with ``Mapping[str, V]``, where ``V`` is the union of all its value types. For instance, the following type is consistent with ``Mapping[str, int | str]``::

    class Person(TypedDict, other_keys=Never):
        name: str
        age: int

A TypedDict type ``A`` is consistent with TypedDict ``B`` if ``A`` is structurally compatible with ``B``. This is true if and only if all of the following are satisfied:

* For each key in ``B``, ``A`` has the corresponding key and the corresponding value type in ``A`` is consistent with the value type in ``B``, unless the key in ``B`` is of type ``ReadOnly[NotRequired[Any]]``, in which case it may be missing in ``A`` provided ``A`` allows other keys.
* For each non-read-only key in ``B``, the corresponding value type in ``B`` is also consistent with the corresponding value type in ``A``.
* For each required key in ``B``, the corresponding key is required in ``A``.
* For each non-read-only, non-required key in ``B``, the corresponding key is not required in ``A``.
* If ``B`` does not allow other keys, then ``A`` does not allow other keys.
* If ``B`` does not allow other keys, then for each key in ``A``, ``B`` has the corresponding key.

Discussion:

* All non-specified keys in a type that allows other keys are implicitly of type ``ReadOnly[NotRequired[Any]]`` (or ``ReadOnly[NotRequired[Unknown]]`` in pyright).

* Read-only value types behave covariantly, as they cannot be mutated. This is similar to container types such as ``Sequence``, and different from non-read-only value types, which behave invariantly. Example::

    class A(TypedDict, readonly=True):
        x: int | None

    class B(TypedDict):
        x: int

    def f(a: A) -> None:
        print(a['x'] or 0)

    b: B = {'x': 1}
    f(b)  # Accepted by type checker

* A TypedDict type ``A`` with no explicit key ``'x'`` that allows other keys is not consistent with a TypedDict type with a non-required key ``'x'``, since at runtime the key ``'x'`` could be present and have an incompatible type (which may not be visible through ``A`` due to structural subtyping). The only exception to this rule is if ``'x'`` is non-required, read-only and of type ``object`` (or ``Any`` or pylance's ``Unknown``).

* A TypedDict type ``A`` with no key ``'x'`` that does not allow other keys may be consistent with a TypedDict type with a read-only, non-required key ``'x'``. Example::

    class A(TypedDict, total=False, readonly=True):
        y: int

    class B(TypedDict, other_keys=Never):
        x: int

    def f(a: A) -> int:
       return a.get("y", 0)

    def g(b: B) -> None:
       b["x"] = f(b)  # Accepted by type checker

Union Operation
---------------

The union operation creates a new dictionary with the merged keys and values of its two operands. As such, the result should be consistent with any type that can hold the possible key-value pairs, not just types compatible with the operand types. For example::

    class A(TypedDict, readonly=True, other_keys=Never):
        x: int

    class B(TypedDict, total=False, readonly=True, other_keys=Never):
        x: str

    class C(TypedDict):
        x: int | str

    def union_a_b(a: A, b: B) -> C:
        # Accepted by type-checker, even though C is not read-only and
        # allows other keys:
        return a | b

This is different from the usual compatibility rules, where the result of an operation has a defined type which the variable it is assigned to must be consistent with. A similar situation occurs with ``TypedDict`` and ``copy()`` or ``deepcopy()``.

If the union of two TypedDict objects of type ``A`` and ``B`` are assigned to a TypedDict of type ``C``, the type checker should verify that:

* if ``C`` does not allow other keys, neither ``A`` nor ``B`` allow other keys
* if ``C`` does not allow other keys, it contains all keys found in either ``A`` or ``B``
* if a key ``'x'`` is found in ``A`` and ``C``, its type in ``A`` is consistent with its type in ``C``.
* if a key ``'x'`` is found in ``B`` and ``C``, its type in ``B`` is consistent with its type in ``C``.
* if a key ``'x'`` is required in ``C``, it is required in either ``A`` or ``B``.

Notes:

* The read-only status of the keys does not matter. A key can be read-only on just ``A``, just ``B``, or just ``C``, or any combination.
* A key found on ``A`` or ``B`` may be missed off ``C`` if it allows other keys. Type-checkers may however choose to flag this edge-case with a warning or error in some circumstances, if it is found to be a source of mistakes.

Update Operations
-----------------

Previously, ``clear()`` and ``popitem()`` were rejected by type checkers on TypedDict objects, as they could remove required keys, some of which may not be directly visible because of structural subtyping. However, these methods should be allowed on TypedDicts objects with all keys non-read-only and non-required and with no other keys allowed::

    class A(TypedDict, total=False, other_keys=Never):
        x: int
        y: str

    a: A = { "x": 1, "y": "foo" }
    a.popitem()  # Accepted by type checker
    a.clear()  # Accepted by type checker

``update`` has been difficult to type correctly due to the open nature of TypedDict objects. Keys not specified on the type could still be present (and constrained) due to structural subtyping, meaning type safety could be accidentally violated. For instance::

    class B(TypedDict, total=False):
        x: int

    def update_b(b1: B, b2: B) -> None:
        b1.update(b2)

    class C(B, TypedDict, total=False):
        y: int

    class D(B, TypedDict, total=False):
        y: str

    c: C = { "x": 1, "y": 2 }
    d: D = { "x": 3, "y": "foo" }
    update_b(c, d)  # c is no longer a C at runtime

Both mypy and pyright currectly permit this usage, however, as the only viable alternative has been to prevent calling ``update`` at all.

With the addition of ``other_keys``, it becomes possible to more accurately type the update method:

* Declare a new read-only TypedDict type that does not allow other keys
* Copy all non-read-only entries to it
* Make all entries read-only and non-required
* Union this with an iterable of matching key-value pairs

For instance::

    class Example(TypedDict):
        a: int
        b: NotRequired[str]
        c: ReadOnly[int]

    class ExampleUpdateDict(TypedDict, total=False, readonly=True, other_keys=Never):
        a: int
        b: str
        # c is not present as it is read-only in Example

    ExampleUpdateEntry = tuple[Literal["a"], int] | tuple[Literal["b"], str]
    ExampleUpdate = ExampleUpdateDict | Iterable[ExampleUpdateEntry]

Type checkers should permit any type compatible with this TypedDict to be passed into the update operation. As with :pep:`589`, they may choose to continue permitting TypedDict types that allow other keys as well, to avoid generating false positives.

Keyword argument typing
-----------------------

:pep:`692` introduced ``Unpack`` to annotate ``**kwargs`` with a ``TypedDict``. Marking one or more of the entries of a ``TypedDict`` used in this way as read-only will have no effect on the type signature of the method, since all keyword arguments are read-only by design in Python. However, it *will* prevent the entry from being modified in the body of the function::

    class Args(TypedDict):
        key1: int
        key2: str

    class ReadonlyArgs(TypedDict, readonly=True):
        key1: int
        key2: str

    class Function(Protocol):
        def __call__(self, **kwargs: Unpack[Args]) -> None: ...

    def impl(self, **kwargs: Unpack[ReadonlyArgs]) -> None:
        kwargs["key1"] = 3  # Type check error: key1 is readonly

    fn: Function = impl  # Accepted by type checker: function signatures are identical


Backwards compatibility
=======================

This PEP adds new features to ``TypedDict``, so code that inspects ``TypedDict`` types will have to change to support types using the new features. This is expected to mainly affect type-checkers.

Security implications
=====================

There are no known security consequences arising from this PEP.

How to Teach This
=================

Suggestion for changes to the :mod:`typing` module, in line with current practice:

* Add this PEP to the others listed.
* Add ``typing.ReadOnly``, linked to TypedDict and this PEP.
* Add the following text to the TypedDict entry:

By default, keys not specified in a TypedDict may still be present. Instances can be restricted to only the named keys with the ``other_keys`` flag. *insert example, perhaps using ``in`` to illustrate the benefit*

Individual keys can be excluded from mutate operations using ReadOnly, allowing them to be read but not changed. This is useful when the exact type of the value is not known yet, and so modifying it would break structural subtypes. *insert example*

If all keys on a TypedDict should be read-only, the ``readonly`` flag can be used as a shorthand. *insert example*

Reference Implementation
========================

No complete reference implementation exists yet. pyright 1.1.310 ships with a partial implementation of the ReadOnly qualifier.

Rejected Alternatives
=====================

A TypedMapping protocol type
----------------------------

An earlier version of :pep:`705` proposed a ``TypedMapping`` protocol type, behaving much like a read-only TypedDict but without the constraint that the runtime type be a ``dict``. The behavior described in the current version of this PEP could then be obtained by inheriting a TypedDict from a TypedMapping. This has been set aside for now as more complex, without a strong use-case motivating the additional complexity.

A higher-order Readonly type
----------------------------

A generalized higher-order type could be added that removes mutator methods from its parameter, e.g. ``ReadOnly[MovieRecord]``. For a TypedDict, this would be like adding ``readonly=True`` to the declaration. This would naturally want to be defined for a wider set of types than just TypedDict subclasses, and also raises questions about whether and how it applies to nested types. We decided to keep the scope of this PEP narrower.

Preventing other keys with the typing.final decorator
-----------------------------------------------------

Instead of adding an ``other_keys`` flag to TypedDict, treat classes decorated with :func:`~typing.final` as disallowing other keys. This makes intuitive sense for TypedDict as it stands now: preventing adding any other keys guarantees no other types will be structurally compatible, so it is effectively final. There is also partial support for this idiom in mypy and pyright, which both use it as a way to achieve type discrimination. However, if any keys are read-only, preventing adding any other keys does **not** make the type final any more, so using the decorator this way seems incorrect. For example::

    class Foo: ...
    class Bar(Foo): ...

    @final
    class FooHolder(TypedDict, readonly=True):
      item: Foo

    @final
    class BarHolder(FooHolder, readonly=True):
      item: Bar

Extending a ``TypedDict`` to refine the types is a reasonable feature, but the above code looks like it should raise a runtime error. Should ``@final`` be modified to allow inheritance? Should users be prevented from using this pattern?

More context for this can be found on `pyright issue 5254 <https://github.com/microsoft/pyright/issues/5254>`_.

We recommend type checkers treat decorating a TypedDict type with final as identical to setting ``other_keys=Never``, if they continue to support the idiom for backwards compatibility, but reject any use of final on a TypedDict with read-only keys. Once ``other_keys`` is adopted, they may also wish to deprecate use of final on TypedDicts entirely.

Using different casing for ``readonly`` keyword or ``ReadOnly`` type
--------------------------------------------------------------------

It appears to be common convention to put an initial caps onto words separated by a dash when converting to CamelCase, but to drop the dash completely when converting to snake_case. Django uses ``readonly``, for instance. This appears consistent with the definition of both on Wikipedia: snake_case replaces spaces with dashes, while CamelCase uppercases the first letter of each word. That said, more examples or counterexamples, ideally from the core Python libraries, or better explicit guidance on the convention, would be greatly appreciated.

Mandate unsound type narrowing
------------------------------

The main use-case we are aware of for ``other_keys=Never`` (and the current workaround of final-decorated TypedDict types) is to simplify type discrimination, as shown in the motivation section.

By comparison, TypeScript handles this edge-case by ignoring the possibility of instances of one type in the union having undeclared keys. If a variable is known to be of type ``A | B`` and an ``in`` check is done using a key not explicitly declared on ``B``, it is assumed no instance of ``B`` will pass that check. While technically unsound, this a common enough idiom that it could fall under the recommendation in :pep:`589` that "potentially unsafe operations may be accepted if the alternative is to generate false positive errors for idiomatic code".

This user request has been rejected multiple times by type checkers, however, suggesting the community prefers strict type-safety over idiomatic code here.

Make the ``other_keys`` flag a boolean
--------------------------------------

Since ``other_keys`` can only effectively take two values, ``Never`` or absent, it was originally proposed as a boolean flag, with ``other_keys=False`` equivalent to the current ``other_keys=Never``. However, the `unmerged proposal of PEP-728 <https://github.com/python/peps/pull/3441>`_ provides equivalent functionality when restricting other types to ``Never``, so this proposal was updated to use comparable syntax, to make it clearer how the proposals intersect.

Use a reserved ``__extra__`` key
--------------------------------

The `unmerged proposal of PEP-728 <https://github.com/python/peps/pull/3441>`_ proposes different syntax for disallowing other keys::

    class EntertainmentMovie(TypedDict, readonly=True):
        movie: Movie
        __extra__: Never

This new key does not function like other keys -- for instance, it is implicitly ``NotRequired`` but cannot be explicitly marked as such. The author of this PEP prefers the asymmetry of using a keyword argument to set expectations that it does not behave like other key declarations, and others have provided similar feedback on the PR.

However, this PEP will be updated to match whatever syntax the PEP-728 author decides to go with.

Leave other_keys to PEP-728
---------------------------

This PEP could drop the ``other_keys`` proposal entirely rather than propose a limited subset of it. However, as this PEP affects the unofficial status-quo of using final to disallow other keys, it seems important to both highlight that issue and propose a solution.


Copyright
=========
This document is placed in the public domain or under the
CC0-1.0-Universal license, whichever is more permissive.
````

</details>

<details><summary><b>Step 4 — revision_4</b> (3063 words)</summary>

````text
Abstract
========

:pep:`589` defines the structural type :class:`~typing.TypedDict` for dictionaries with a fixed set of keys.
As ``TypedDict`` is a mutable type, it is difficult to correctly annotate methods which accept read-only parameters in a way that doesn't prevent valid inputs.
This PEP proposes a new type qualifier, ``typing.ReadOnly``, to support these usages.

Motivation
==========

Representing structured data using (potentially nested) dictionaries with string keys is a common pattern in Python programs. :pep:`589` allows these values to be type checked when the exact type is known up-front, but it is hard to write read-only code that accepts more specific variants: for instance, where values may be subtypes or restrict a union of possible types. This is an especially common issue when writing APIs for services, which may support a wide range of input structures, and typically do not need to modify their input.

Pure functions
--------------

Consider trying to add type hints to a function ``movie_string``::

    def movie_string(movie: Movie) -> str:
        if movie.get("year") is None:
            return movie["name"]
        else:
            return f'{movie["name"]} ({movie["year"]})'

We could define this ``Movie`` type using a ``TypedDict``::

    from typing import NotRequired, TypedDict

    class Movie(TypedDict):
        name: str
        year: NotRequired[int | None]

But suppose we have another type where year is required::

    class MovieRecord(TypedDict):
        name: str
        year: int

Attempting to pass a ``MovieRecord`` into ``movie_string`` results in the error (using mypy):

.. code-block:: text

    Argument 1 to "movie_string" has incompatible type "MovieRecord"; expected "Movie"

This particular use case should be type-safe, but the type checker correctly stops the
user from passing a ``MovieRecord`` into a ``Movie`` parameter in the general case, because
the ``Movie`` class has mutator methods that could potentially allow the function to break
the type constraints in ``MovieRecord`` (e.g. with ``movie["year"] = None`` or ``del movie["year"]``).
The problem disappears if we don't have mutator methods in ``Movie``. This could be achieved by defining an immutable interface using a :pep:`544` :class:`~typing.Protocol`::

    from typing import Literal, Protocol, overload

    class Movie(Protocol):
        @overload
        def get(self, key: Literal["name"]) -> str: ...

        @overload
        def get(self, key: Literal["year"]) -> int | None: ...

        @overload
        def __getitem__(self, key: Literal["name"]) -> str: ...

        @overload
        def __getitem__(self, key: Literal["year"]) -> int | None: ...

This is very repetitive, easy to get wrong, and is still missing important method definitions like ``__contains__()`` and ``keys()``.

Updating nested dicts
---------------------

The structural typing of ``TypedDict`` is supposed to permit writing update functions that only constrain the types of items they modify::

    class HasTimestamp(TypedDict):
        timestamp: float

    class Logs(TypedDict):
        timestamp: float
        loglines: list[str]

    def update_timestamp(d: HasTimestamp) -> None:
        d["timestamp"] = now()

    def add_logline(logs: Logs, logline: str) -> None:
        logs["loglines"].append(logline)
        update_timestamp(logs)  # Accepted by type checker

However, this no longer works once you start nesting dictionaries::

    class HasTimestampedMetadata(TypedDict):
        metadata: HasTimestamp

    class UserAudit(TypedDict):
        name: str
        metadata: Logs

    def update_metadata_timestamp(d: HasTimestampedMetadata) -> None:
        d["metadata"]["timestamp"] = now()

    def rename_user(d: UserAudit, name: str) -> None:
        d["name"] = name
        update_metadata_timestamp(d)  # Type check error: "metadata" is not of type HasTimestamp

This looks like an error, but is simply due to the (unwanted) ability to overwrite the ``metadata`` item held by the ``HasTimestampedMetadata`` instance with a different ``HasTimestamp`` instance, that may no longer be a ``UserAudit`` instance.

It is possible to work around this issue with generics (as of Python 3.11), but it is very complicated, requiring a type parameter for every nested dict.


Rationale
=========

These problems can be resolved by removing the ability to update one or more of the items in a ``TypedDict``. This does not mean the items are immutable: a reference to the underlying dictionary could still exist with a different but compatible type in which those items have mutator operations. As such, these are not "final" items; using this term would risk confusion with final attributes, which are fully immutable. These items are "read-only", and we introduce a new ``typing.ReadOnly`` type qualifier for this purpose.

The ``movie_string`` function in the first motivating example can then be typed as follows::

    from typing import NotRequired, ReadOnly, TypedDict

    class Movie(TypedDict):
        name: ReadOnly[str]
        year: ReadOnly[NotRequired[int | None]]

    def movie_string(movie: Movie) -> str:
        if movie.get("year") is None:
            return movie["name"]
        else:
            return f'{movie["name"]} ({movie["year"]})'

A mixture of read-only and non-read-only items is permitted, allowing the second motivating example to be correctly annotated::

    class HasTimestamp(TypedDict):
        timestamp: float

    class HasTimestampedMetadata(TypedDict):
        metadata: ReadOnly[HasTimestamp]

    def update_metadata_timestamp(d: HasTimestampedMetadata) -> None:
        d["metadata"]["timestamp"] = now()

    class Logs(HasTimestamp):
        loglines: list[str]

    class UserAudit(TypedDict):
        name: str
        metadata: Logs

    def rename_user(d: UserAudit, name: str) -> None:
        d["name"] = name
        update_metadata_timestamp(d)  # Now OK

In addition to these benefits, by flagging arguments of a function as read-only (by using a ``TypedDict`` like ``Movie`` with read-only items), it makes explicit not just to typecheckers but also to users that the function is not going to modify its inputs, which is usually a desirable property of a function interface.

This PEP proposes making ``ReadOnly`` valid only in a ``TypedDict``. A possible future extension would be to support it in additional contexts, such as in protocols.


Specification
=============

A new ``typing.ReadOnly`` type qualifier is added.

``typing.ReadOnly`` type qualifier
----------------------------------

The ``typing.ReadOnly`` type qualifier is used to indicate that an item declared in a ``TypedDict`` definition may not be mutated (added, modified, or removed)::

    from typing import ReadOnly

    class Band(TypedDict):
        name: str
        members: ReadOnly[list[str]]

    blur: Band = {"name": "blur", "members": []}
    blur["name"] = "Blur"  # OK: "name" is not read-only
    blur["members"] = ["Damon Albarn"]  # Type check error: "members" is read-only
    blur["members"].append("Damon Albarn")  # OK: list is mutable

Alternative functional syntax
-----------------------------

The :pep:`alternative functional syntax <589#alternative-syntax>` for TypedDict also supports the new type qualifier::

   Band = TypedDict("Band", {"name": str, "members": ReadOnly[list[str]]})

Interaction with other special types
------------------------------------

``ReadOnly[]`` can be used with ``Required[]``, ``NotRequired[]`` and ``Annotated[]``, in any nesting order:

::

    class Movie(TypedDict):
        title: ReadOnly[Required[str]]  # OK
        year: ReadOnly[NotRequired[Annotated[int, ValueRange(-9999, 9999)]]]  # OK

::

    class Movie(TypedDict):
        title: Required[ReadOnly[str]]  # OK
        year: Annotated[NotRequired[ReadOnly[int]], ValueRange(-9999, 9999)]  # OK

This is consistent with the behavior introduced in :pep:`655`.

Inheritance
-----------

Subclasses can redeclare read-only items as non-read-only, allowing them to be mutated::

    class NamedDict(TypedDict):
        name: ReadOnly[str]

    class Album(NamedDict):
        name: str
        year: int

    album: Album = { "name": "Flood", "year": 1990 }
    album["year"] = 1973
    album["name"] = "Dark Side Of The Moon"  # OK: "name" is not read-only in Album

If a read-only item is not redeclared, it remains read-only::

    class Album(NamedDict):
        year: int

    album: Album = { "name": "Flood", "year": 1990 }
    album["name"] = "Dark Side Of The Moon"  # Type check error: "name" is read-only in Album

Subclasses can narrow value types of read-only items::

    class AlbumCollection(TypedDict):
        albums: ReadOnly[Collection[Album]]

    class RecordShop(AlbumCollection):
        name: str
        albums: ReadOnly[list[Album]]  # OK: "albums" is read-only in AlbumCollection

Subclasses can require items that are read-only but not required in the superclass::

    class OptionalName(TypedDict):
        name: ReadOnly[NotRequired[str]]

    class RequiredName(OptionalName):
        name: ReadOnly[Required[str]]

    d: RequiredName = {}  # Type check error: "name" required

Subclasses can combine these rules::

    class OptionalIdent(TypedDict):
        ident: ReadOnly[NotRequired[str | int]]

    class User(OptionalIdent):
        ident: str  # Required, mutable, and not an int

Note that these are just consequences of structural typing, but they are highlighted here as the behavior now differs from the rules specified in :pep:`589`.

Type consistency
----------------

*This section updates the type consistency rules introduced in* :pep:`589` *to cover the new feature in this PEP. In particular, any pair of types that do not use the new feature will be consistent under these new rules if (and only if) they were already consistent.*

A TypedDict type ``A`` is consistent with TypedDict ``B`` if ``A`` is structurally compatible with ``B``. This is true if and only if all of the following are satisfied:

* For each item in ``B``, ``A`` has the corresponding key, unless the item in ``B`` is read-only, not required, and of top value type (``ReadOnly[NotRequired[object]]``).
* For each item in ``B``, if ``A`` has the corresponding key, the corresponding value type in ``A`` is consistent with the value type in ``B``.
* For each non-read-only item in ``B``, its value type is consistent with the corresponding value type in ``A``.
* For each required key in ``B``, the corresponding key is required in ``A``.
* For each non-required key in ``B``, if the item is not read-only in ``B``, the corresponding key is not required in ``A``.

Discussion:

* All non-specified items in a TypedDict implicitly have value type ``ReadOnly[NotRequired[object]]``.

* Read-only items behave covariantly, as they cannot be mutated. This is similar to container types such as ``Sequence``, and different from non-read-only items, which behave invariantly. Example::

    class A(TypedDict):
        x: ReadOnly[int | None]

    class B(TypedDict):
        x: int

    def f(a: A) -> None:
        print(a["x"] or 0)

    b: B = {"x": 1}
    f(b)  # Accepted by type checker

* A TypedDict type ``A`` with no explicit key ``'x'`` is not consistent with a TypedDict type ``B`` with a non-required key ``'x'``, since at runtime the key ``'x'`` could be present and have an incompatible type (which may not be visible through ``A`` due to structural subtyping). The only exception to this rule is if the item in ``B`` is read-only, and the value type is of top type (``object``). For example::

    class A(TypedDict):
        x: int

    class B(TypedDict):
        x: int
        y: ReadOnly[NotRequired[object]]

    a: A = { "x": 1 }
    b: B = a  # Accepted by type checker

Update method
-------------

In addition to existing type checking rules, type checkers should error if a TypedDict with a read-only item is updated with another TypedDict that declares that key::

    class A(TypedDict):
        x: ReadOnly[int]
        y: int

    a1: A = { "x": 1, "y": 2 }
    a2: A = { "x": 3, "y": 4 }
    a1.update(a2)  # Type check error: "x" is read-only in A

Unless the declared value is of bottom type::

    class B(TypedDict):
        x: NotRequired[typing.Never]
        y: ReadOnly[int]

    def update_a(a: A, b: B) -> None:
        a.update(b)  # Accepted by type checker: "x" cannot be set on b

Keyword argument typing
-----------------------

:pep:`692` introduced ``Unpack`` to annotate ``**kwargs`` with a ``TypedDict``. Marking one or more of the items of a ``TypedDict`` used in this way as read-only will have no effect on the type signature of the method. However, it *will* prevent the item from being modified in the body of the function::

    class Args(TypedDict):
        key1: int
        key2: str

    class ReadOnlyArgs(TypedDict):
        key1: ReadOnly[int]
        key2: ReadOnly[str]

    class Function(Protocol):
        def __call__(self, **kwargs: Unpack[Args]) -> None: ...

    def impl(self, **kwargs: Unpack[ReadOnlyArgs]) -> None:
        kwargs["key1"] = 3  # Type check error: key1 is readonly

    fn: Function = impl  # Accepted by type checker: function signatures are identical


Backwards compatibility
=======================

This PEP adds a new feature to ``TypedDict``, so code that inspects ``TypedDict`` types will have to change to support types using it. This is expected to mainly affect type-checkers.

Security implications
=====================

There are no known security consequences arising from this PEP.

How to teach this
=================

Suggestion for changes to the :mod:`typing` module, in line with current practice:

* Add this PEP to the others listed.
* Add ``typing.ReadOnly``, linked to TypedDict and this PEP.
* Add the following text to the TypedDict entry:

Individual items can be excluded from mutate operations using ReadOnly, allowing them to be read but not changed. This is useful when the exact type of the value is not known yet, and so modifying it would break structural subtypes. *insert example*

Reference implementation
========================

pyright 1.1.332 fully implements this proposal.

Rejected alternatives
=====================

A TypedMapping protocol type
----------------------------

An earlier version of this PEP proposed a ``TypedMapping`` protocol type, behaving much like a read-only TypedDict but without the constraint that the runtime type be a ``dict``. The behavior described in the current version of this PEP could then be obtained by inheriting a TypedDict from a TypedMapping. This has been set aside for now as more complex, without a strong use-case motivating the additional complexity.

A higher-order ReadOnly type
----------------------------

A generalized higher-order type could be added that removes mutator methods from its parameter, e.g. ``ReadOnly[MovieRecord]``. For a TypedDict, this would be like adding ``ReadOnly`` to every item, including those declared in superclasses. This would naturally want to be defined for a wider set of types than just TypedDict subclasses, and also raises questions about whether and how it applies to nested types. We decided to keep the scope of this PEP narrower.

Calling the type ``Readonly``
-----------------------------

``Read-only`` is generally hyphenated, and it appears to be common convention to put initial caps onto words separated by a dash when converting to CamelCase. This appears consistent with the definition of CamelCase on Wikipedia: CamelCase uppercases the first letter of each word. That said, Python examples or counter-examples, ideally from the core Python libraries, or better explicit guidance on the convention, would be greatly appreciated.

A readonly flag
---------------

Earlier versions of this PEP introduced a boolean flag that would ensure all items in a TypedDict were read-only::

    class Movie(TypedDict, readonly=True):
        name: str
        year: NotRequired[int | None]

    movie: Movie = { "name": "A Clockwork Orange" }
    movie["year"] = 1971  # Type check error: "year" is read-only

However, this led to confusion when inheritance was introduced::

    class A(TypedDict):
        key1: int

    class B(A, TypedDict, readonly=True):
        key2: int

    b: B = { "key1": 1, "key2": 2 }
    b["key1"] = 4  # Accepted by type checker: "key1" is not read-only

It would be reasonable for someone familiar with ``frozen``, on seeing just the definition of B, to assume that the whole type was read-only. On the other hand, it would be reasonable for someone familiar with ``total`` to assume that read-only only applies to the current type.

The original proposal attempted to eliminate this ambiguity by making it both a type check and a runtime error to define ``B`` in this way. This was still a source of surprise to people expecting it to work like ``total``.

Given that no extra types could be expressed with the ``readonly`` flag, it has been removed from the proposal to avoid ambiguity and surprise.

Supporting type-checked removal of read-only qualifier via copy and other methods
---------------------------------------------------------------------------------

An earlier version of this PEP mandated that code like the following be supported by type-checkers::

    class A(TypedDict):
        x: ReadOnly[int]

    class B(TypedDict):
        x: ReadOnly[str]

    class C(TypedDict):
        x: int | str

    def copy_and_modify(a: A) -> C:
        c: C = copy.copy(a)
        if not c['x']:
            c['x'] = "N/A"
        return c

    def merge_and_modify(a: A, b: B) -> C:
        c: C = a | b
        if not c['x']:
            c['x'] = "N/A"
        return c

However, there is currently no way to express this in the typeshed, meaning type-checkers would be forced to special-case these functions. There is already a way to code these operations that mypy and pyright do support, though arguably this is less readable::

    copied: C = { **a }
    merged: C = { **a, **b }

While not as flexible as would be ideal, the current typeshed stubs are sound, and remain so if this PEP is accepted. Updating the typeshed would require new typing features, like a type constructor to express the type resulting from merging two or more dicts, and a type qualifier to indicate a returned value is not shared (so may have type constraints like read-only and invariance of generics loosened in specific ways), plus details of how type-checkers would be expected to interpret these features. These could be valuable additions to the language, but are outside the scope of this PEP.

Given this, we have deferred any update of the typeshed stubs.

Preventing unspecified keys in TypedDicts
-----------------------------------------

Consider the following "type discrimination" code::

    class A(TypedDict):
      foo: int

    class B(TypedDict):
      bar: int

    def get_field(d: A | B) -> int:
      if "foo" in d:
        return d["foo"]  # !!!
      else:
        return d["bar"]

This is a common idiom, and other languages like Typescript allow it. Technically, however, this code is unsound: ``B`` does not declare ``foo``, but instances of ``B`` may still have the key present, and the associated value may be of any type::

    class C(TypedDict):
      foo: str
      bar: int

    c: C = { "foo": "hi", "bar" 3 }
    b: B = c  # OK: C is structurally compatible with B
    v = get_field(b)  # Returns a string at runtime, not an int!

mypy rejects the definition of ``get_field`` on the marked line with the error ``TypedDict "B" has no key "foo"``, which is a rather confusing error message, but is caused by this unsoundness.

One option for correcting this would be to explicitly prevent ``B`` from holding a ``foo``::

    class B(TypedDict):
      foo: NotRequired[Never]
      bar: int

    b: B = c  # Type check error: key "foo" not allowed in B

However, this requires every possible key that might be used to discriminate on to be explicitly declared in every type, which is not generally feasible. A better option would be to have a way of preventing all unspecified keys from being included in ``B``. mypy supports this using the ``@final`` decorator from :pep:`591`::

    @final
    class B(TypedDict):
      bar: int

The reasoning here is that this prevents ``C`` or any other type from being considered a "subclass" of ``B``, so instances of ``B`` can now be relied on to never hold the key ``foo``, even though it is not explicitly declared to be of bottom type.

With the introduction of read-only items, however, this reasoning would imply type-checkers should ban the following::

    @final
    class D(TypedDict):
      field: ReadOnly[Collection[str]]

    @final
    class E(TypedDict):
      field: list[str]

    e: E = { "field": ["value1", "value2"] }
    d: D = e  # Error?

The conceptual problem here is that TypedDicts are structural types: they cannot really be subclassed. As such, using ``@final`` on them is not well-defined; it is certainly not mentioned in :pep:`591`.

An earlier version of this PEP proposed resolving this by adding a new flag to ``TypedDict`` that would explicitly prevent other keys from being used, but not other kinds of structural compatibility::

    class B(TypedDict, other_keys=Never):
      bar: int

    b: B = c  # Type check error: key "foo" not allowed in B

However, during the process of drafting, the situation changed:

* pyright, which previously worked similarly to mypy in this type discrimination case, `changed to allow the original example without error <https://github.com/microsoft/pyright/commit/6a25a7bf0b5cb3721a06d0e0d6245b2ebfbf053b>`_, despite the unsoundness, due to it being a common idiom
* mypy has `an open issue <https://github.com/python/mypy/issues/15697>`_ to follow the lead of pyright and Typescript and permit the idiom as well
* a `draft of PEP-728 <https://github.com/python/peps/pull/3441>`_ was created that is a superset of the ``other_keys`` functionality

As such, there is less urgency to address this issue in this PEP, and it has been deferred to PEP-728.


Copyright
=========
This document is placed in the public domain or under the
CC0-1.0-Universal license, whichever is more permissive.
````

</details>

<details><summary><b>Step 5 — revision_5</b> (3269 words)</summary>

````text
Abstract
========

:pep:`589` defines the structural type :class:`~typing.TypedDict` for dictionaries with a fixed set of keys.
As ``TypedDict`` is a mutable type, it is difficult to correctly annotate methods which accept read-only parameters in a way that doesn't prevent valid inputs.

This PEP proposes a new type qualifier, ``typing.ReadOnly``, to support these usages. It makes no Python grammar changes. Correct usage of read-only keys of TypedDicts is intended to be enforced only by static type checkers, and will not be enforced by Python itself at runtime.

Motivation
==========

Representing structured data using (potentially nested) dictionaries with string keys is a common pattern in Python programs. :pep:`589` allows these values to be type checked when the exact type is known up-front, but it is hard to write read-only code that accepts more specific variants: for instance, where values may be subtypes or restrict a union of possible types. This is an especially common issue when writing APIs for services, which may support a wide range of input structures, and typically do not need to modify their input.

Pure functions
--------------

Consider trying to add type hints to a function ``movie_string``::

    def movie_string(movie: Movie) -> str:
        if movie.get("year") is None:
            return movie["name"]
        else:
            return f'{movie["name"]} ({movie["year"]})'

We could define this ``Movie`` type using a ``TypedDict``::

    from typing import NotRequired, TypedDict

    class Movie(TypedDict):
        name: str
        year: NotRequired[int | None]

But suppose we have another type where year is required::

    class MovieRecord(TypedDict):
        name: str
        year: int

Attempting to pass a ``MovieRecord`` into ``movie_string`` results in the error (using mypy):

.. code-block:: text

    Argument 1 to "movie_string" has incompatible type "MovieRecord"; expected "Movie"

This particular use case should be type-safe, but the type checker correctly stops the
user from passing a ``MovieRecord`` into a ``Movie`` parameter in the general case, because
the ``Movie`` class has mutator methods that could potentially allow the function to break
the type constraints in ``MovieRecord`` (e.g. with ``movie["year"] = None`` or ``del movie["year"]``).
The problem disappears if we don't have mutator methods in ``Movie``. This could be achieved by defining an immutable interface using a :pep:`544` :class:`~typing.Protocol`::

    from typing import Literal, Protocol, overload

    class Movie(Protocol):
        @overload
        def get(self, key: Literal["name"]) -> str: ...

        @overload
        def get(self, key: Literal["year"]) -> int | None: ...

        @overload
        def __getitem__(self, key: Literal["name"]) -> str: ...

        @overload
        def __getitem__(self, key: Literal["year"]) -> int | None: ...

This is very repetitive, easy to get wrong, and is still missing important method definitions like ``__contains__()`` and ``keys()``.

Updating nested dicts
---------------------

The structural typing of ``TypedDict`` is supposed to permit writing update functions that only constrain the types of items they modify::

    class HasTimestamp(TypedDict):
        timestamp: float

    class Logs(TypedDict):
        timestamp: float
        loglines: list[str]

    def update_timestamp(d: HasTimestamp) -> None:
        d["timestamp"] = now()

    def add_logline(logs: Logs, logline: str) -> None:
        logs["loglines"].append(logline)
        update_timestamp(logs)  # Accepted by type checker

However, this no longer works once you start nesting dictionaries::

    class HasTimestampedMetadata(TypedDict):
        metadata: HasTimestamp

    class UserAudit(TypedDict):
        name: str
        metadata: Logs

    def update_metadata_timestamp(d: HasTimestampedMetadata) -> None:
        d["metadata"]["timestamp"] = now()

    def rename_user(d: UserAudit, name: str) -> None:
        d["name"] = name
        update_metadata_timestamp(d)  # Type check error: "metadata" is not of type HasTimestamp

This looks like an error, but is simply due to the (unwanted) ability to overwrite the ``metadata`` item held by the ``HasTimestampedMetadata`` instance with a different ``HasTimestamp`` instance, that may no longer be a ``UserAudit`` instance.

It is possible to work around this issue with generics (as of Python 3.11), but it is very complicated, requiring a type parameter for every nested dict.


Rationale
=========

These problems can be resolved by removing the ability to update one or more of the items in a ``TypedDict``. This does not mean the items are immutable: a reference to the underlying dictionary could still exist with a different but compatible type in which those items have mutator operations. These items are "read-only", and we introduce a new ``typing.ReadOnly`` type qualifier for this purpose.

The ``movie_string`` function in the first motivating example can then be typed as follows::

    from typing import NotRequired, ReadOnly, TypedDict

    class Movie(TypedDict):
        name: ReadOnly[str]
        year: ReadOnly[NotRequired[int | None]]

    def movie_string(movie: Movie) -> str:
        if movie.get("year") is None:
            return movie["name"]
        else:
            return f'{movie["name"]} ({movie["year"]})'

A mixture of read-only and non-read-only items is permitted, allowing the second motivating example to be correctly annotated::

    class HasTimestamp(TypedDict):
        timestamp: float

    class HasTimestampedMetadata(TypedDict):
        metadata: ReadOnly[HasTimestamp]

    def update_metadata_timestamp(d: HasTimestampedMetadata) -> None:
        d["metadata"]["timestamp"] = now()

    class Logs(HasTimestamp):
        loglines: list[str]

    class UserAudit(TypedDict):
        name: str
        metadata: Logs

    def rename_user(d: UserAudit, name: str) -> None:
        d["name"] = name
        update_metadata_timestamp(d)  # Now OK

In addition to these benefits, by flagging arguments of a function as read-only (by using a ``TypedDict`` like ``Movie`` with read-only items), it makes explicit not just to typecheckers but also to users that the function is not going to modify its inputs, which is usually a desirable property of a function interface.

This PEP proposes making ``ReadOnly`` valid only in a ``TypedDict``. A possible future extension would be to support it in additional contexts, such as in protocols.


Specification
=============

A new ``typing.ReadOnly`` type qualifier is added.

``typing.ReadOnly`` type qualifier
----------------------------------

The ``typing.ReadOnly`` type qualifier is used to indicate that an item declared in a ``TypedDict`` definition may not be mutated (added, modified, or removed)::

    from typing import ReadOnly

    class Band(TypedDict):
        name: str
        members: ReadOnly[list[str]]

    blur: Band = {"name": "blur", "members": []}
    blur["name"] = "Blur"  # OK: "name" is not read-only
    blur["members"] = ["Damon Albarn"]  # Type check error: "members" is read-only
    blur["members"].append("Damon Albarn")  # OK: list is mutable

Alternative functional syntax
-----------------------------

The :pep:`alternative functional syntax <589#alternative-syntax>` for TypedDict also supports the new type qualifier::

   Band = TypedDict("Band", {"name": str, "members": ReadOnly[list[str]]})

Interaction with other special types
------------------------------------

``ReadOnly[]`` can be used with ``Required[]``, ``NotRequired[]`` and ``Annotated[]``, in any nesting order:

::

    class Movie(TypedDict):
        title: ReadOnly[Required[str]]  # OK
        year: ReadOnly[NotRequired[Annotated[int, ValueRange(-9999, 9999)]]]  # OK

::

    class Movie(TypedDict):
        title: Required[ReadOnly[str]]  # OK
        year: Annotated[NotRequired[ReadOnly[int]], ValueRange(-9999, 9999)]  # OK

This is consistent with the behavior introduced in :pep:`655`.

Inheritance
-----------

Subclasses can redeclare read-only items as non-read-only, allowing them to be mutated::

    class NamedDict(TypedDict):
        name: ReadOnly[str]

    class Album(NamedDict):
        name: str
        year: int

    album: Album = { "name": "Flood", "year": 1990 }
    album["year"] = 1973
    album["name"] = "Dark Side Of The Moon"  # OK: "name" is not read-only in Album

If a read-only item is not redeclared, it remains read-only::

    class Album(NamedDict):
        year: int

    album: Album = { "name": "Flood", "year": 1990 }
    album["name"] = "Dark Side Of The Moon"  # Type check error: "name" is read-only in Album

Subclasses can narrow value types of read-only items::

    class AlbumCollection(TypedDict):
        albums: ReadOnly[Collection[Album]]

    class RecordShop(AlbumCollection):
        name: str
        albums: ReadOnly[list[Album]]  # OK: "albums" is read-only in AlbumCollection

Subclasses can require items that are read-only but not required in the superclass::

    class OptionalName(TypedDict):
        name: ReadOnly[NotRequired[str]]

    class RequiredName(OptionalName):
        name: ReadOnly[Required[str]]

    d: RequiredName = {}  # Type check error: "name" required

Subclasses can combine these rules::

    class OptionalIdent(TypedDict):
        ident: ReadOnly[NotRequired[str | int]]

    class User(OptionalIdent):
        ident: str  # Required, mutable, and not an int

Note that these are just consequences of structural typing, but they are highlighted here as the behavior now differs from the rules specified in :pep:`589`.

Type consistency
----------------

*This section updates the type consistency rules introduced in* :pep:`589` *to cover the new feature in this PEP. In particular, any pair of types that do not use the new feature will be consistent under these new rules if (and only if) they were already consistent.*

A TypedDict type ``A`` is consistent with TypedDict ``B`` if ``A`` is structurally compatible with ``B``. This is true if and only if all of the following are satisfied:

* For each item in ``B``, ``A`` has the corresponding key, unless the item in ``B`` is read-only, not required, and of top value type (``ReadOnly[NotRequired[object]]``).
* For each item in ``B``, if ``A`` has the corresponding key, the corresponding value type in ``A`` is consistent with the value type in ``B``.
* For each non-read-only item in ``B``, its value type is consistent with the corresponding value type in ``A``.
* For each required key in ``B``, the corresponding key is required in ``A``.
* For each non-required key in ``B``, if the item is not read-only in ``B``, the corresponding key is not required in ``A``.

Discussion:

* All non-specified items in a TypedDict implicitly have value type ``ReadOnly[NotRequired[object]]``.

* Read-only items behave covariantly, as they cannot be mutated. This is similar to container types such as ``Sequence``, and different from non-read-only items, which behave invariantly. Example::

    class A(TypedDict):
        x: ReadOnly[int | None]

    class B(TypedDict):
        x: int

    def f(a: A) -> None:
        print(a["x"] or 0)

    b: B = {"x": 1}
    f(b)  # Accepted by type checker

* A TypedDict type ``A`` with no explicit key ``'x'`` is not consistent with a TypedDict type ``B`` with a non-required key ``'x'``, since at runtime the key ``'x'`` could be present and have an incompatible type (which may not be visible through ``A`` due to structural subtyping). The only exception to this rule is if the item in ``B`` is read-only, and the value type is of top type (``object``). For example::

    class A(TypedDict):
        x: int

    class B(TypedDict):
        x: int
        y: ReadOnly[NotRequired[object]]

    a: A = { "x": 1 }
    b: B = a  # Accepted by type checker

Update method
-------------

In addition to existing type checking rules, type checkers should error if a TypedDict with a read-only item is updated with another TypedDict that declares that key::

    class A(TypedDict):
        x: ReadOnly[int]
        y: int

    a1: A = { "x": 1, "y": 2 }
    a2: A = { "x": 3, "y": 4 }
    a1.update(a2)  # Type check error: "x" is read-only in A

Unless the declared value is of bottom type (:data:`~typing.Never`)::

    class B(TypedDict):
        x: NotRequired[typing.Never]
        y: ReadOnly[int]

    def update_a(a: A, b: B) -> None:
        a.update(b)  # Accepted by type checker: "x" cannot be set on b

Note: Nothing will ever match the ``Never`` type, so an item annotated with it must be absent.

Keyword argument typing
-----------------------

:pep:`692` introduced ``Unpack`` to annotate ``**kwargs`` with a ``TypedDict``. Marking one or more of the items of a ``TypedDict`` used in this way as read-only will have no effect on the type signature of the method. However, it *will* prevent the item from being modified in the body of the function::

    class Args(TypedDict):
        key1: int
        key2: str

    class ReadOnlyArgs(TypedDict):
        key1: ReadOnly[int]
        key2: ReadOnly[str]

    class Function(Protocol):
        def __call__(self, **kwargs: Unpack[Args]) -> None: ...

    def impl(self, **kwargs: Unpack[ReadOnlyArgs]) -> None:
        kwargs["key1"] = 3  # Type check error: key1 is readonly

    fn: Function = impl  # Accepted by type checker: function signatures are identical

Runtime behavior
----------------

``TypedDict`` types will gain two new attributes, ``__readonly_keys__`` and ``__mutable_keys__``, which will be frozensets containing all read-only and non-read-only keys, respectively::

    class Example(TypedDict):
        a: int
        b: ReadOnly[int]
        c: int
        d: ReadOnly[int]

    assert Example.__readonly_keys__ == frozenset({'b', 'd'})
    assert Example.__mutable_keys__ == frozenset({'a', 'c'})

``typing.get_type_hints`` will strip out any ``ReadOnly`` type qualifiers, unless ``include_extras`` is ``True``::

    assert get_type_hints(Example)['b'] == int
    assert get_type_hints(Example, include_extras=True)['b'] == ReadOnly[int]

``typing.get_origin`` and ``typing.get_args`` will be updated to recognize ``ReadOnly``::

    assert get_origin(ReadOnly[int]) is ReadOnly
    assert get_args(ReadOnly[int]) == (int,)


Backwards compatibility
=======================

This PEP adds a new feature to ``TypedDict``, so code that inspects ``TypedDict`` types will have to change to support types using it. This is expected to mainly affect type-checkers.

Security implications
=====================

There are no known security consequences arising from this PEP.

How to teach this
=================

Suggested changes to the :mod:`typing` module documentation, in line with current practice:

* Add this PEP to the others listed.
* Add ``typing.ReadOnly``, linked to TypedDict and this PEP.
* Add the following text to the TypedDict entry:

The ``ReadOnly`` type qualifier indicates that an item declared in a ``TypedDict`` definition may be read but not mutated (added, modified or removed). This is useful when the exact type of the value is not known yet, and so modifying it would break structural subtypes. *insert example*

Reference implementation
========================

`pyright 1.1.333 fully implements this proposal <https://github.com/microsoft/pyright/releases/tag/1.1.333>`_.

Rejected alternatives
=====================

A TypedMapping protocol type
----------------------------

An earlier version of this PEP proposed a ``TypedMapping`` protocol type, behaving much like a read-only TypedDict but without the constraint that the runtime type be a ``dict``. The behavior described in the current version of this PEP could then be obtained by inheriting a TypedDict from a TypedMapping. This has been set aside for now as more complex, without a strong use-case motivating the additional complexity.

A higher-order ReadOnly type
----------------------------

A generalized higher-order type could be added that removes mutator methods from its parameter, e.g. ``ReadOnly[MovieRecord]``. For a TypedDict, this would be like adding ``ReadOnly`` to every item, including those declared in superclasses. This would naturally want to be defined for a wider set of types than just TypedDict subclasses, and also raises questions about whether and how it applies to nested types. We decided to keep the scope of this PEP narrower.

Calling the type ``Readonly``
-----------------------------

``Read-only`` is generally hyphenated, and it appears to be common convention to put initial caps onto words separated by a dash when converting to CamelCase. This appears consistent with the definition of CamelCase on Wikipedia: CamelCase uppercases the first letter of each word. That said, Python examples or counter-examples, ideally from the core Python libraries, or better explicit guidance on the convention, would be greatly appreciated.

Reusing the ``Final`` annotation
--------------------------------

The :class:`~typing.Final` annotation prevents an attribute from being modified, like the proposed ``ReadOnly`` qualifier does for ``TypedDict`` items. However, it is also documented as preventing redefinition in subclasses too; from :pep:`591`:

    The ``typing.Final`` type qualifier is used to indicate that a variable or attribute should not be reassigned, redefined, or overridden.

This does not fit with the intended use of ``ReadOnly``. Rather than introduce confusion by having ``Final`` behave differently in different contexts, we chose to introduce a new qualifier.

A readonly flag
---------------

Earlier versions of this PEP introduced a boolean flag that would ensure all items in a TypedDict were read-only::

    class Movie(TypedDict, readonly=True):
        name: str
        year: NotRequired[int | None]

    movie: Movie = { "name": "A Clockwork Orange" }
    movie["year"] = 1971  # Type check error: "year" is read-only

However, this led to confusion when inheritance was introduced::

    class A(TypedDict):
        key1: int

    class B(A, TypedDict, readonly=True):
        key2: int

    b: B = { "key1": 1, "key2": 2 }
    b["key1"] = 4  # Accepted by type checker: "key1" is not read-only

It would be reasonable for someone familiar with ``frozen`` (from :mod:`dataclasses`), on seeing just the definition of B, to assume that the whole type was read-only. On the other hand, it would be reasonable for someone familiar with ``total`` to assume that read-only only applies to the current type.

The original proposal attempted to eliminate this ambiguity by making it both a type check and a runtime error to define ``B`` in this way. This was still a source of surprise to people expecting it to work like ``total``.

Given that no extra types could be expressed with the ``readonly`` flag, it has been removed from the proposal to avoid ambiguity and surprise.

Supporting type-checked removal of read-only qualifier via copy and other methods
---------------------------------------------------------------------------------

An earlier version of this PEP mandated that code like the following be supported by type-checkers::

    class A(TypedDict):
        x: ReadOnly[int]

    class B(TypedDict):
        x: ReadOnly[str]

    class C(TypedDict):
        x: int | str

    def copy_and_modify(a: A) -> C:
        c: C = copy.copy(a)
        if not c['x']:
            c['x'] = "N/A"
        return c

    def merge_and_modify(a: A, b: B) -> C:
        c: C = a | b
        if not c['x']:
            c['x'] = "N/A"
        return c

However, there is currently no way to express this in the typeshed, meaning type-checkers would be forced to special-case these functions. There is already a way to code these operations that mypy and pyright do support, though arguably this is less readable::

    copied: C = { **a }
    merged: C = { **a, **b }

While not as flexible as would be ideal, the current typeshed stubs are sound, and remain so if this PEP is accepted. Updating the typeshed would require new typing features, like a type constructor to express the type resulting from merging two or more dicts, and a type qualifier to indicate a returned value is not shared (so may have type constraints like read-only and invariance of generics loosened in specific ways), plus details of how type-checkers would be expected to interpret these features. These could be valuable additions to the language, but are outside the scope of this PEP.

Given this, we have deferred any update of the typeshed stubs.

Preventing unspecified keys in TypedDicts
-----------------------------------------

Consider the following "type discrimination" code::

    class A(TypedDict):
      foo: int

    class B(TypedDict):
      bar: int

    def get_field(d: A | B) -> int:
      if "foo" in d:
        return d["foo"]  # !!!
      else:
        return d["bar"]

This is a common idiom, and other languages like Typescript allow it. Technically, however, this code is unsound: ``B`` does not declare ``foo``, but instances of ``B`` may still have the key present, and the associated value may be of any type::

    class C(TypedDict):
      foo: str
      bar: int

    c: C = { "foo": "hi", "bar" 3 }
    b: B = c  # OK: C is structurally compatible with B
    v = get_field(b)  # Returns a string at runtime, not an int!

mypy rejects the definition of ``get_field`` on the marked line with the error ``TypedDict "B" has no key "foo"``, which is a rather confusing error message, but is caused by this unsoundness.

One option for correcting this would be to explicitly prevent ``B`` from holding a ``foo``::

    class B(TypedDict):
      foo: NotRequired[Never]
      bar: int

    b: B = c  # Type check error: key "foo" not allowed in B

However, this requires every possible key that might be used to discriminate on to be explicitly declared in every type, which is not generally feasible. A better option would be to have a way of preventing all unspecified keys from being included in ``B``. mypy supports this using the ``@final`` decorator from :pep:`591`::

    @final
    class B(TypedDict):
      bar: int

The reasoning here is that this prevents ``C`` or any other type from being considered a "subclass" of ``B``, so instances of ``B`` can now be relied on to never hold the key ``foo``, even though it is not explicitly declared to be of bottom type.

With the introduction of read-only items, however, this reasoning would imply type-checkers should ban the following::

    @final
    class D(TypedDict):
      field: ReadOnly[Collection[str]]

    @final
    class E(TypedDict):
      field: list[str]

    e: E = { "field": ["value1", "value2"] }
    d: D = e  # Error?

The conceptual problem here is that TypedDicts are structural types: they cannot really be subclassed. As such, using ``@final`` on them is not well-defined; it is certainly not mentioned in :pep:`591`.

An earlier version of this PEP proposed resolving this by adding a new flag to ``TypedDict`` that would explicitly prevent other keys from being used, but not other kinds of structural compatibility::

    class B(TypedDict, other_keys=Never):
      bar: int

    b: B = c  # Type check error: key "foo" not allowed in B

However, during the process of drafting, the situation changed:

* pyright, which previously worked similarly to mypy in this type discrimination case, `changed to allow the original example without error <https://github.com/microsoft/pyright/commit/6a25a7bf0b5cb3721a06d0e0d6245b2ebfbf053b>`_, despite the unsoundness, due to it being a common idiom
* mypy has `an open issue <https://github.com/python/mypy/issues/15697>`_ to follow the lead of pyright and Typescript and permit the idiom as well
* a `draft of PEP-728 <https://github.com/python/peps/pull/3441>`_ was created that is a superset of the ``other_keys`` functionality

As such, there is less urgency to address this issue in this PEP, and it has been deferred to PEP-728.


Copyright
=========
This document is placed in the public domain or under the
CC0-1.0-Universal license, whichever is more permissive.
````

</details>

<details><summary><b>Step 6 — revision_6</b> (3269 words)</summary>

````text
Abstract
========

:pep:`589` defines the structural type :class:`~typing.TypedDict` for dictionaries with a fixed set of keys.
As ``TypedDict`` is a mutable type, it is difficult to correctly annotate methods which accept read-only parameters in a way that doesn't prevent valid inputs.

This PEP proposes a new type qualifier, ``typing.ReadOnly``, to support these usages. It makes no Python grammar changes. Correct usage of read-only keys of TypedDicts is intended to be enforced only by static type checkers, and will not be enforced by Python itself at runtime.

Motivation
==========

Representing structured data using (potentially nested) dictionaries with string keys is a common pattern in Python programs. :pep:`589` allows these values to be type checked when the exact type is known up-front, but it is hard to write read-only code that accepts more specific variants: for instance, where values may be subtypes or restrict a union of possible types. This is an especially common issue when writing APIs for services, which may support a wide range of input structures, and typically do not need to modify their input.

Pure functions
--------------

Consider trying to add type hints to a function ``movie_string``::

    def movie_string(movie: Movie) -> str:
        if movie.get("year") is None:
            return movie["name"]
        else:
            return f'{movie["name"]} ({movie["year"]})'

We could define this ``Movie`` type using a ``TypedDict``::

    from typing import NotRequired, TypedDict

    class Movie(TypedDict):
        name: str
        year: NotRequired[int | None]

But suppose we have another type where year is required::

    class MovieRecord(TypedDict):
        name: str
        year: int

Attempting to pass a ``MovieRecord`` into ``movie_string`` results in the error (using mypy):

.. code-block:: text

    Argument 1 to "movie_string" has incompatible type "MovieRecord"; expected "Movie"

This particular use case should be type-safe, but the type checker correctly stops the
user from passing a ``MovieRecord`` into a ``Movie`` parameter in the general case, because
the ``Movie`` class has mutator methods that could potentially allow the function to break
the type constraints in ``MovieRecord`` (e.g. with ``movie["year"] = None`` or ``del movie["year"]``).
The problem disappears if we don't have mutator methods in ``Movie``. This could be achieved by defining an immutable interface using a :pep:`544` :class:`~typing.Protocol`::

    from typing import Literal, Protocol, overload

    class Movie(Protocol):
        @overload
        def get(self, key: Literal["name"]) -> str: ...

        @overload
        def get(self, key: Literal["year"]) -> int | None: ...

        @overload
        def __getitem__(self, key: Literal["name"]) -> str: ...

        @overload
        def __getitem__(self, key: Literal["year"]) -> int | None: ...

This is very repetitive, easy to get wrong, and is still missing important method definitions like ``__contains__()`` and ``keys()``.

Updating nested dicts
---------------------

The structural typing of ``TypedDict`` is supposed to permit writing update functions that only constrain the types of items they modify::

    class HasTimestamp(TypedDict):
        timestamp: float

    class Logs(TypedDict):
        timestamp: float
        loglines: list[str]

    def update_timestamp(d: HasTimestamp) -> None:
        d["timestamp"] = now()

    def add_logline(logs: Logs, logline: str) -> None:
        logs["loglines"].append(logline)
        update_timestamp(logs)  # Accepted by type checker

However, this no longer works once you start nesting dictionaries::

    class HasTimestampedMetadata(TypedDict):
        metadata: HasTimestamp

    class UserAudit(TypedDict):
        name: str
        metadata: Logs

    def update_metadata_timestamp(d: HasTimestampedMetadata) -> None:
        d["metadata"]["timestamp"] = now()

    def rename_user(d: UserAudit, name: str) -> None:
        d["name"] = name
        update_metadata_timestamp(d)  # Type check error: "metadata" is not of type HasTimestamp

This looks like an error, but is simply due to the (unwanted) ability to overwrite the ``metadata`` item held by the ``HasTimestampedMetadata`` instance with a different ``HasTimestamp`` instance, that may no longer be a ``Logs`` instance.

It is possible to work around this issue with generics (as of Python 3.11), but it is very complicated, requiring a type parameter for every nested dict.


Rationale
=========

These problems can be resolved by removing the ability to update one or more of the items in a ``TypedDict``. This does not mean the items are immutable: a reference to the underlying dictionary could still exist with a different but compatible type in which those items have mutator operations. These items are "read-only", and we introduce a new ``typing.ReadOnly`` type qualifier for this purpose.

The ``movie_string`` function in the first motivating example can then be typed as follows::

    from typing import NotRequired, ReadOnly, TypedDict

    class Movie(TypedDict):
        name: ReadOnly[str]
        year: ReadOnly[NotRequired[int | None]]

    def movie_string(movie: Movie) -> str:
        if movie.get("year") is None:
            return movie["name"]
        else:
            return f'{movie["name"]} ({movie["year"]})'

A mixture of read-only and non-read-only items is permitted, allowing the second motivating example to be correctly annotated::

    class HasTimestamp(TypedDict):
        timestamp: float

    class HasTimestampedMetadata(TypedDict):
        metadata: ReadOnly[HasTimestamp]

    def update_metadata_timestamp(d: HasTimestampedMetadata) -> None:
        d["metadata"]["timestamp"] = now()

    class Logs(HasTimestamp):
        loglines: list[str]

    class UserAudit(TypedDict):
        name: str
        metadata: Logs

    def rename_user(d: UserAudit, name: str) -> None:
        d["name"] = name
        update_metadata_timestamp(d)  # Now OK

In addition to these benefits, by flagging arguments of a function as read-only (by using a ``TypedDict`` like ``Movie`` with read-only items), it makes explicit not just to typecheckers but also to users that the function is not going to modify its inputs, which is usually a desirable property of a function interface.

This PEP proposes making ``ReadOnly`` valid only in a ``TypedDict``. A possible future extension would be to support it in additional contexts, such as in protocols.


Specification
=============

A new ``typing.ReadOnly`` type qualifier is added.

``typing.ReadOnly`` type qualifier
----------------------------------

The ``typing.ReadOnly`` type qualifier is used to indicate that an item declared in a ``TypedDict`` definition may not be mutated (added, modified, or removed)::

    from typing import ReadOnly

    class Band(TypedDict):
        name: str
        members: ReadOnly[list[str]]

    blur: Band = {"name": "blur", "members": []}
    blur["name"] = "Blur"  # OK: "name" is not read-only
    blur["members"] = ["Damon Albarn"]  # Type check error: "members" is read-only
    blur["members"].append("Damon Albarn")  # OK: list is mutable

Alternative functional syntax
-----------------------------

The :pep:`alternative functional syntax <589#alternative-syntax>` for TypedDict also supports the new type qualifier::

   Band = TypedDict("Band", {"name": str, "members": ReadOnly[list[str]]})

Interaction with other special types
------------------------------------

``ReadOnly[]`` can be used with ``Required[]``, ``NotRequired[]`` and ``Annotated[]``, in any nesting order:

::

    class Movie(TypedDict):
        title: ReadOnly[Required[str]]  # OK
        year: ReadOnly[NotRequired[Annotated[int, ValueRange(-9999, 9999)]]]  # OK

::

    class Movie(TypedDict):
        title: Required[ReadOnly[str]]  # OK
        year: Annotated[NotRequired[ReadOnly[int]], ValueRange(-9999, 9999)]  # OK

This is consistent with the behavior introduced in :pep:`655`.

Inheritance
-----------

Subclasses can redeclare read-only items as non-read-only, allowing them to be mutated::

    class NamedDict(TypedDict):
        name: ReadOnly[str]

    class Album(NamedDict):
        name: str
        year: int

    album: Album = { "name": "Flood", "year": 1990 }
    album["year"] = 1973
    album["name"] = "Dark Side Of The Moon"  # OK: "name" is not read-only in Album

If a read-only item is not redeclared, it remains read-only::

    class Album(NamedDict):
        year: int

    album: Album = { "name": "Flood", "year": 1990 }
    album["name"] = "Dark Side Of The Moon"  # Type check error: "name" is read-only in Album

Subclasses can narrow value types of read-only items::

    class AlbumCollection(TypedDict):
        albums: ReadOnly[Collection[Album]]

    class RecordShop(AlbumCollection):
        name: str
        albums: ReadOnly[list[Album]]  # OK: "albums" is read-only in AlbumCollection

Subclasses can require items that are read-only but not required in the superclass::

    class OptionalName(TypedDict):
        name: ReadOnly[NotRequired[str]]

    class RequiredName(OptionalName):
        name: ReadOnly[Required[str]]

    d: RequiredName = {}  # Type check error: "name" required

Subclasses can combine these rules::

    class OptionalIdent(TypedDict):
        ident: ReadOnly[NotRequired[str | int]]

    class User(OptionalIdent):
        ident: str  # Required, mutable, and not an int

Note that these are just consequences of structural typing, but they are highlighted here as the behavior now differs from the rules specified in :pep:`589`.

Type consistency
----------------

*This section updates the type consistency rules introduced in* :pep:`589` *to cover the new feature in this PEP. In particular, any pair of types that do not use the new feature will be consistent under these new rules if (and only if) they were already consistent.*

A TypedDict type ``A`` is consistent with TypedDict ``B`` if ``A`` is structurally compatible with ``B``. This is true if and only if all of the following are satisfied:

* For each item in ``B``, ``A`` has the corresponding key, unless the item in ``B`` is read-only, not required, and of top value type (``ReadOnly[NotRequired[object]]``).
* For each item in ``B``, if ``A`` has the corresponding key, the corresponding value type in ``A`` is consistent with the value type in ``B``.
* For each non-read-only item in ``B``, its value type is consistent with the corresponding value type in ``A``.
* For each required key in ``B``, the corresponding key is required in ``A``.
* For each non-required key in ``B``, if the item is not read-only in ``B``, the corresponding key is not required in ``A``.

Discussion:

* All non-specified items in a TypedDict implicitly have value type ``ReadOnly[NotRequired[object]]``.

* Read-only items behave covariantly, as they cannot be mutated. This is similar to container types such as ``Sequence``, and different from non-read-only items, which behave invariantly. Example::

    class A(TypedDict):
        x: ReadOnly[int | None]

    class B(TypedDict):
        x: int

    def f(a: A) -> None:
        print(a["x"] or 0)

    b: B = {"x": 1}
    f(b)  # Accepted by type checker

* A TypedDict type ``A`` with no explicit key ``'x'`` is not consistent with a TypedDict type ``B`` with a non-required key ``'x'``, since at runtime the key ``'x'`` could be present and have an incompatible type (which may not be visible through ``A`` due to structural subtyping). The only exception to this rule is if the item in ``B`` is read-only, and the value type is of top type (``object``). For example::

    class A(TypedDict):
        x: int

    class B(TypedDict):
        x: int
        y: ReadOnly[NotRequired[object]]

    a: A = { "x": 1 }
    b: B = a  # Accepted by type checker

Update method
-------------

In addition to existing type checking rules, type checkers should error if a TypedDict with a read-only item is updated with another TypedDict that declares that key::

    class A(TypedDict):
        x: ReadOnly[int]
        y: int

    a1: A = { "x": 1, "y": 2 }
    a2: A = { "x": 3, "y": 4 }
    a1.update(a2)  # Type check error: "x" is read-only in A

Unless the declared value is of bottom type (:data:`~typing.Never`)::

    class B(TypedDict):
        x: NotRequired[typing.Never]
        y: ReadOnly[int]

    def update_a(a: A, b: B) -> None:
        a.update(b)  # Accepted by type checker: "x" cannot be set on b

Note: Nothing will ever match the ``Never`` type, so an item annotated with it must be absent.

Keyword argument typing
-----------------------

:pep:`692` introduced ``Unpack`` to annotate ``**kwargs`` with a ``TypedDict``. Marking one or more of the items of a ``TypedDict`` used in this way as read-only will have no effect on the type signature of the method. However, it *will* prevent the item from being modified in the body of the function::

    class Args(TypedDict):
        key1: int
        key2: str

    class ReadOnlyArgs(TypedDict):
        key1: ReadOnly[int]
        key2: ReadOnly[str]

    class Function(Protocol):
        def __call__(self, **kwargs: Unpack[Args]) -> None: ...

    def impl(self, **kwargs: Unpack[ReadOnlyArgs]) -> None:
        kwargs["key1"] = 3  # Type check error: key1 is readonly

    fn: Function = impl  # Accepted by type checker: function signatures are identical

Runtime behavior
----------------

``TypedDict`` types will gain two new attributes, ``__readonly_keys__`` and ``__mutable_keys__``, which will be frozensets containing all read-only and non-read-only keys, respectively::

    class Example(TypedDict):
        a: int
        b: ReadOnly[int]
        c: int
        d: ReadOnly[int]

    assert Example.__readonly_keys__ == frozenset({'b', 'd'})
    assert Example.__mutable_keys__ == frozenset({'a', 'c'})

``typing.get_type_hints`` will strip out any ``ReadOnly`` type qualifiers, unless ``include_extras`` is ``True``::

    assert get_type_hints(Example)['b'] == int
    assert get_type_hints(Example, include_extras=True)['b'] == ReadOnly[int]

``typing.get_origin`` and ``typing.get_args`` will be updated to recognize ``ReadOnly``::

    assert get_origin(ReadOnly[int]) is ReadOnly
    assert get_args(ReadOnly[int]) == (int,)


Backwards compatibility
=======================

This PEP adds a new feature to ``TypedDict``, so code that inspects ``TypedDict`` types will have to change to support types using it. This is expected to mainly affect type-checkers.

Security implications
=====================

There are no known security consequences arising from this PEP.

How to teach this
=================

Suggested changes to the :mod:`typing` module documentation, in line with current practice:

* Add this PEP to the others listed.
* Add ``typing.ReadOnly``, linked to TypedDict and this PEP.
* Add the following text to the TypedDict entry:

The ``ReadOnly`` type qualifier indicates that an item declared in a ``TypedDict`` definition may be read but not mutated (added, modified or removed). This is useful when the exact type of the value is not known yet, and so modifying it would break structural subtypes. *insert example*

Reference implementation
========================

`pyright 1.1.333 fully implements this proposal <https://github.com/microsoft/pyright/releases/tag/1.1.333>`_.

Rejected alternatives
=====================

A TypedMapping protocol type
----------------------------

An earlier version of this PEP proposed a ``TypedMapping`` protocol type, behaving much like a read-only TypedDict but without the constraint that the runtime type be a ``dict``. The behavior described in the current version of this PEP could then be obtained by inheriting a TypedDict from a TypedMapping. This has been set aside for now as more complex, without a strong use-case motivating the additional complexity.

A higher-order ReadOnly type
----------------------------

A generalized higher-order type could be added that removes mutator methods from its parameter, e.g. ``ReadOnly[MovieRecord]``. For a TypedDict, this would be like adding ``ReadOnly`` to every item, including those declared in superclasses. This would naturally want to be defined for a wider set of types than just TypedDict subclasses, and also raises questions about whether and how it applies to nested types. We decided to keep the scope of this PEP narrower.

Calling the type ``Readonly``
-----------------------------

``Read-only`` is generally hyphenated, and it appears to be common convention to put initial caps onto words separated by a dash when converting to CamelCase. This appears consistent with the definition of CamelCase on Wikipedia: CamelCase uppercases the first letter of each word. That said, Python examples or counter-examples, ideally from the core Python libraries, or better explicit guidance on the convention, would be greatly appreciated.

Reusing the ``Final`` annotation
--------------------------------

The :class:`~typing.Final` annotation prevents an attribute from being modified, like the proposed ``ReadOnly`` qualifier does for ``TypedDict`` items. However, it is also documented as preventing redefinition in subclasses too; from :pep:`591`:

    The ``typing.Final`` type qualifier is used to indicate that a variable or attribute should not be reassigned, redefined, or overridden.

This does not fit with the intended use of ``ReadOnly``. Rather than introduce confusion by having ``Final`` behave differently in different contexts, we chose to introduce a new qualifier.

A readonly flag
---------------

Earlier versions of this PEP introduced a boolean flag that would ensure all items in a TypedDict were read-only::

    class Movie(TypedDict, readonly=True):
        name: str
        year: NotRequired[int | None]

    movie: Movie = { "name": "A Clockwork Orange" }
    movie["year"] = 1971  # Type check error: "year" is read-only

However, this led to confusion when inheritance was introduced::

    class A(TypedDict):
        key1: int

    class B(A, TypedDict, readonly=True):
        key2: int

    b: B = { "key1": 1, "key2": 2 }
    b["key1"] = 4  # Accepted by type checker: "key1" is not read-only

It would be reasonable for someone familiar with ``frozen`` (from :mod:`dataclasses`), on seeing just the definition of B, to assume that the whole type was read-only. On the other hand, it would be reasonable for someone familiar with ``total`` to assume that read-only only applies to the current type.

The original proposal attempted to eliminate this ambiguity by making it both a type check and a runtime error to define ``B`` in this way. This was still a source of surprise to people expecting it to work like ``total``.

Given that no extra types could be expressed with the ``readonly`` flag, it has been removed from the proposal to avoid ambiguity and surprise.

Supporting type-checked removal of read-only qualifier via copy and other methods
---------------------------------------------------------------------------------

An earlier version of this PEP mandated that code like the following be supported by type-checkers::

    class A(TypedDict):
        x: ReadOnly[int]

    class B(TypedDict):
        x: ReadOnly[str]

    class C(TypedDict):
        x: int | str

    def copy_and_modify(a: A) -> C:
        c: C = copy.copy(a)
        if not c['x']:
            c['x'] = "N/A"
        return c

    def merge_and_modify(a: A, b: B) -> C:
        c: C = a | b
        if not c['x']:
            c['x'] = "N/A"
        return c

However, there is currently no way to express this in the typeshed, meaning type-checkers would be forced to special-case these functions. There is already a way to code these operations that mypy and pyright do support, though arguably this is less readable::

    copied: C = { **a }
    merged: C = { **a, **b }

While not as flexible as would be ideal, the current typeshed stubs are sound, and remain so if this PEP is accepted. Updating the typeshed would require new typing features, like a type constructor to express the type resulting from merging two or more dicts, and a type qualifier to indicate a returned value is not shared (so may have type constraints like read-only and invariance of generics loosened in specific ways), plus details of how type-checkers would be expected to interpret these features. These could be valuable additions to the language, but are outside the scope of this PEP.

Given this, we have deferred any update of the typeshed stubs.

Preventing unspecified keys in TypedDicts
-----------------------------------------

Consider the following "type discrimination" code::

    class A(TypedDict):
      foo: int

    class B(TypedDict):
      bar: int

    def get_field(d: A | B) -> int:
      if "foo" in d:
        return d["foo"]  # !!!
      else:
        return d["bar"]

This is a common idiom, and other languages like Typescript allow it. Technically, however, this code is unsound: ``B`` does not declare ``foo``, but instances of ``B`` may still have the key present, and the associated value may be of any type::

    class C(TypedDict):
      foo: str
      bar: int

    c: C = { "foo": "hi", "bar" 3 }
    b: B = c  # OK: C is structurally compatible with B
    v = get_field(b)  # Returns a string at runtime, not an int!

mypy rejects the definition of ``get_field`` on the marked line with the error ``TypedDict "B" has no key "foo"``, which is a rather confusing error message, but is caused by this unsoundness.

One option for correcting this would be to explicitly prevent ``B`` from holding a ``foo``::

    class B(TypedDict):
      foo: NotRequired[Never]
      bar: int

    b: B = c  # Type check error: key "foo" not allowed in B

However, this requires every possible key that might be used to discriminate on to be explicitly declared in every type, which is not generally feasible. A better option would be to have a way of preventing all unspecified keys from being included in ``B``. mypy supports this using the ``@final`` decorator from :pep:`591`::

    @final
    class B(TypedDict):
      bar: int

The reasoning here is that this prevents ``C`` or any other type from being considered a "subclass" of ``B``, so instances of ``B`` can now be relied on to never hold the key ``foo``, even though it is not explicitly declared to be of bottom type.

With the introduction of read-only items, however, this reasoning would imply type-checkers should ban the following::

    @final
    class D(TypedDict):
      field: ReadOnly[Collection[str]]

    @final
    class E(TypedDict):
      field: list[str]

    e: E = { "field": ["value1", "value2"] }
    d: D = e  # Error?

The conceptual problem here is that TypedDicts are structural types: they cannot really be subclassed. As such, using ``@final`` on them is not well-defined; it is certainly not mentioned in :pep:`591`.

An earlier version of this PEP proposed resolving this by adding a new flag to ``TypedDict`` that would explicitly prevent other keys from being used, but not other kinds of structural compatibility::

    class B(TypedDict, other_keys=Never):
      bar: int

    b: B = c  # Type check error: key "foo" not allowed in B

However, during the process of drafting, the situation changed:

* pyright, which previously worked similarly to mypy in this type discrimination case, `changed to allow the original example without error <https://github.com/microsoft/pyright/commit/6a25a7bf0b5cb3721a06d0e0d6245b2ebfbf053b>`_, despite the unsoundness, due to it being a common idiom
* mypy has `an open issue <https://github.com/python/mypy/issues/15697>`_ to follow the lead of pyright and Typescript and permit the idiom as well
* a `draft of PEP-728 <https://github.com/python/peps/pull/3441>`_ was created that is a superset of the ``other_keys`` functionality

As such, there is less urgency to address this issue in this PEP, and it has been deferred to PEP-728.


Copyright
=========
This document is placed in the public domain or under the
CC0-1.0-Universal license, whichever is more permissive.
````

</details>

<details><summary><b>Step 7 — revision_7</b> (3268 words)</summary>

````text
Abstract
========

:pep:`589` defines the structural type :class:`~typing.TypedDict` for dictionaries with a fixed set of keys.
As ``TypedDict`` is a mutable type, it is difficult to correctly annotate methods which accept read-only parameters in a way that doesn't prevent valid inputs.

This PEP proposes a new type qualifier, ``typing.ReadOnly``, to support these usages. It makes no Python grammar changes. Correct usage of read-only keys of TypedDicts is intended to be enforced only by static type checkers, and will not be enforced by Python itself at runtime.

Motivation
==========

Representing structured data using (potentially nested) dictionaries with string keys is a common pattern in Python programs. :pep:`589` allows these values to be type checked when the exact type is known up-front, but it is hard to write read-only code that accepts more specific variants: for instance, where values may be subtypes or restrict a union of possible types. This is an especially common issue when writing APIs for services, which may support a wide range of input structures, and typically do not need to modify their input.

Pure functions
--------------

Consider trying to add type hints to a function ``movie_string``::

    def movie_string(movie: Movie) -> str:
        if movie.get("year") is None:
            return movie["name"]
        else:
            return f'{movie["name"]} ({movie["year"]})'

We could define this ``Movie`` type using a ``TypedDict``::

    from typing import NotRequired, TypedDict

    class Movie(TypedDict):
        name: str
        year: NotRequired[int | None]

But suppose we have another type where year is required::

    class MovieRecord(TypedDict):
        name: str
        year: int

Attempting to pass a ``MovieRecord`` into ``movie_string`` results in the error (using mypy):

.. code-block:: text

    Argument 1 to "movie_string" has incompatible type "MovieRecord"; expected "Movie"

This particular use case should be type-safe, but the type checker correctly stops the
user from passing a ``MovieRecord`` into a ``Movie`` parameter in the general case, because
the ``Movie`` class has mutator methods that could potentially allow the function to break
the type constraints in ``MovieRecord`` (e.g. with ``movie["year"] = None`` or ``del movie["year"]``).
The problem disappears if we don't have mutator methods in ``Movie``. This could be achieved by defining an immutable interface using a :pep:`544` :class:`~typing.Protocol`::

    from typing import Literal, Protocol, overload

    class Movie(Protocol):
        @overload
        def get(self, key: Literal["name"]) -> str: ...

        @overload
        def get(self, key: Literal["year"]) -> int | None: ...

        @overload
        def __getitem__(self, key: Literal["name"]) -> str: ...

        @overload
        def __getitem__(self, key: Literal["year"]) -> int | None: ...

This is very repetitive, easy to get wrong, and is still missing important method definitions like ``__contains__()`` and ``keys()``.

Updating nested dicts
---------------------

The structural typing of ``TypedDict`` is supposed to permit writing update functions that only constrain the types of items they modify::

    class HasTimestamp(TypedDict):
        timestamp: float

    class Logs(TypedDict):
        timestamp: float
        loglines: list[str]

    def update_timestamp(d: HasTimestamp) -> None:
        d["timestamp"] = now()

    def add_logline(logs: Logs, logline: str) -> None:
        logs["loglines"].append(logline)
        update_timestamp(logs)  # Accepted by type checker

However, this no longer works once you start nesting dictionaries::

    class HasTimestampedMetadata(TypedDict):
        metadata: HasTimestamp

    class UserAudit(TypedDict):
        name: str
        metadata: Logs

    def update_metadata_timestamp(d: HasTimestampedMetadata) -> None:
        d["metadata"]["timestamp"] = now()

    def rename_user(d: UserAudit, name: str) -> None:
        d["name"] = name
        update_metadata_timestamp(d)  # Type check error: "metadata" is not of type HasTimestamp

This looks like an error, but is simply due to the (unwanted) ability to overwrite the ``metadata`` item held by the ``HasTimestampedMetadata`` instance with a different ``HasTimestamp`` instance, that may no longer be a ``Logs`` instance.

It is possible to work around this issue with generics (as of Python 3.11), but it is very complicated, requiring a type parameter for every nested dict.


Rationale
=========

These problems can be resolved by removing the ability to update one or more of the items in a ``TypedDict``. This does not mean the items are immutable: a reference to the underlying dictionary could still exist with a different but compatible type in which those items have mutator operations. These items are "read-only", and we introduce a new ``typing.ReadOnly`` type qualifier for this purpose.

The ``movie_string`` function in the first motivating example can then be typed as follows::

    from typing import NotRequired, ReadOnly, TypedDict

    class Movie(TypedDict):
        name: ReadOnly[str]
        year: ReadOnly[NotRequired[int | None]]

    def movie_string(movie: Movie) -> str:
        if movie.get("year") is None:
            return movie["name"]
        else:
            return f'{movie["name"]} ({movie["year"]})'

A mixture of read-only and non-read-only items is permitted, allowing the second motivating example to be correctly annotated::

    class HasTimestamp(TypedDict):
        timestamp: float

    class HasTimestampedMetadata(TypedDict):
        metadata: ReadOnly[HasTimestamp]

    def update_metadata_timestamp(d: HasTimestampedMetadata) -> None:
        d["metadata"]["timestamp"] = now()

    class Logs(HasTimestamp):
        loglines: list[str]

    class UserAudit(TypedDict):
        name: str
        metadata: Logs

    def rename_user(d: UserAudit, name: str) -> None:
        d["name"] = name
        update_metadata_timestamp(d)  # Now OK

In addition to these benefits, by flagging arguments of a function as read-only (by using a ``TypedDict`` like ``Movie`` with read-only items), it makes explicit not just to typecheckers but also to users that the function is not going to modify its inputs, which is usually a desirable property of a function interface.

This PEP proposes making ``ReadOnly`` valid only in a ``TypedDict``. A possible future extension would be to support it in additional contexts, such as in protocols.


Specification
=============

A new ``typing.ReadOnly`` type qualifier is added.

``typing.ReadOnly`` type qualifier
----------------------------------

The ``typing.ReadOnly`` type qualifier is used to indicate that an item declared in a ``TypedDict`` definition may not be mutated (added, modified, or removed)::

    from typing import ReadOnly

    class Band(TypedDict):
        name: str
        members: ReadOnly[list[str]]

    blur: Band = {"name": "blur", "members": []}
    blur["name"] = "Blur"  # OK: "name" is not read-only
    blur["members"] = ["Damon Albarn"]  # Type check error: "members" is read-only
    blur["members"].append("Damon Albarn")  # OK: list is mutable

Alternative functional syntax
-----------------------------

The :pep:`alternative functional syntax <589#alternative-syntax>` for TypedDict also supports the new type qualifier::

   Band = TypedDict("Band", {"name": str, "members": ReadOnly[list[str]]})

Interaction with other special types
------------------------------------

``ReadOnly[]`` can be used with ``Required[]``, ``NotRequired[]`` and ``Annotated[]``, in any nesting order:

::

    class Movie(TypedDict):
        title: ReadOnly[Required[str]]  # OK
        year: ReadOnly[NotRequired[Annotated[int, ValueRange(-9999, 9999)]]]  # OK

::

    class Movie(TypedDict):
        title: Required[ReadOnly[str]]  # OK
        year: Annotated[NotRequired[ReadOnly[int]], ValueRange(-9999, 9999)]  # OK

This is consistent with the behavior introduced in :pep:`655`.

Inheritance
-----------

Subclasses can redeclare read-only items as non-read-only, allowing them to be mutated::

    class NamedDict(TypedDict):
        name: ReadOnly[str]

    class Album(NamedDict):
        name: str
        year: int

    album: Album = { "name": "Flood", "year": 1990 }
    album["year"] = 1973
    album["name"] = "Dark Side Of The Moon"  # OK: "name" is not read-only in Album

If a read-only item is not redeclared, it remains read-only::

    class Album(NamedDict):
        year: int

    album: Album = { "name": "Flood", "year": 1990 }
    album["name"] = "Dark Side Of The Moon"  # Type check error: "name" is read-only in Album

Subclasses can narrow value types of read-only items::

    class AlbumCollection(TypedDict):
        albums: ReadOnly[Collection[Album]]

    class RecordShop(AlbumCollection):
        name: str
        albums: ReadOnly[list[Album]]  # OK: "albums" is read-only in AlbumCollection

Subclasses can require items that are read-only but not required in the superclass::

    class OptionalName(TypedDict):
        name: ReadOnly[NotRequired[str]]

    class RequiredName(OptionalName):
        name: ReadOnly[Required[str]]

    d: RequiredName = {}  # Type check error: "name" required

Subclasses can combine these rules::

    class OptionalIdent(TypedDict):
        ident: ReadOnly[NotRequired[str | int]]

    class User(OptionalIdent):
        ident: str  # Required, mutable, and not an int

Note that these are just consequences of structural typing, but they are highlighted here as the behavior now differs from the rules specified in :pep:`589`.

Type consistency
----------------

*This section updates the type consistency rules introduced in* :pep:`589` *to cover the new feature in this PEP. In particular, any pair of types that do not use the new feature will be consistent under these new rules if (and only if) they were already consistent.*

A TypedDict type ``A`` is consistent with TypedDict ``B`` if ``A`` is structurally compatible with ``B``. This is true if and only if all of the following are satisfied:

* For each item in ``B``, ``A`` has the corresponding key, unless the item in ``B`` is read-only, not required, and of top value type (``ReadOnly[NotRequired[object]]``).
* For each item in ``B``, if ``A`` has the corresponding key, the corresponding value type in ``A`` is consistent with the value type in ``B``.
* For each non-read-only item in ``B``, its value type is consistent with the corresponding value type in ``A``.
* For each required key in ``B``, the corresponding key is required in ``A``.
* For each non-required key in ``B``, if the item is not read-only in ``B``, the corresponding key is not required in ``A``.

Discussion:

* All non-specified items in a TypedDict implicitly have value type ``ReadOnly[NotRequired[object]]``.

* Read-only items behave covariantly, as they cannot be mutated. This is similar to container types such as ``Sequence``, and different from non-read-only items, which behave invariantly. Example::

    class A(TypedDict):
        x: ReadOnly[int | None]

    class B(TypedDict):
        x: int

    def f(a: A) -> None:
        print(a["x"] or 0)

    b: B = {"x": 1}
    f(b)  # Accepted by type checker

* A TypedDict type ``A`` with no explicit key ``'x'`` is not consistent with a TypedDict type ``B`` with a non-required key ``'x'``, since at runtime the key ``'x'`` could be present and have an incompatible type (which may not be visible through ``A`` due to structural subtyping). The only exception to this rule is if the item in ``B`` is read-only, and the value type is of top type (``object``). For example::

    class A(TypedDict):
        x: int

    class B(TypedDict):
        x: int
        y: ReadOnly[NotRequired[object]]

    a: A = { "x": 1 }
    b: B = a  # Accepted by type checker

Update method
-------------

In addition to existing type checking rules, type checkers should error if a TypedDict with a read-only item is updated with another TypedDict that declares that key::

    class A(TypedDict):
        x: ReadOnly[int]
        y: int

    a1: A = { "x": 1, "y": 2 }
    a2: A = { "x": 3, "y": 4 }
    a1.update(a2)  # Type check error: "x" is read-only in A

Unless the declared value is of bottom type (:data:`~typing.Never`)::

    class B(TypedDict):
        x: NotRequired[typing.Never]
        y: ReadOnly[int]

    def update_a(a: A, b: B) -> None:
        a.update(b)  # Accepted by type checker: "x" cannot be set on b

Note: Nothing will ever match the ``Never`` type, so an item annotated with it must be absent.

Keyword argument typing
-----------------------

:pep:`692` introduced ``Unpack`` to annotate ``**kwargs`` with a ``TypedDict``. Marking one or more of the items of a ``TypedDict`` used in this way as read-only will have no effect on the type signature of the method. However, it *will* prevent the item from being modified in the body of the function::

    class Args(TypedDict):
        key1: int
        key2: str

    class ReadOnlyArgs(TypedDict):
        key1: ReadOnly[int]
        key2: ReadOnly[str]

    class Function(Protocol):
        def __call__(self, **kwargs: Unpack[Args]) -> None: ...

    def impl(**kwargs: Unpack[ReadOnlyArgs]) -> None:
        kwargs["key1"] = 3  # Type check error: key1 is readonly

    fn: Function = impl  # Accepted by type checker: function signatures are identical

Runtime behavior
----------------

``TypedDict`` types will gain two new attributes, ``__readonly_keys__`` and ``__mutable_keys__``, which will be frozensets containing all read-only and non-read-only keys, respectively::

    class Example(TypedDict):
        a: int
        b: ReadOnly[int]
        c: int
        d: ReadOnly[int]

    assert Example.__readonly_keys__ == frozenset({'b', 'd'})
    assert Example.__mutable_keys__ == frozenset({'a', 'c'})

``typing.get_type_hints`` will strip out any ``ReadOnly`` type qualifiers, unless ``include_extras`` is ``True``::

    assert get_type_hints(Example)['b'] == int
    assert get_type_hints(Example, include_extras=True)['b'] == ReadOnly[int]

``typing.get_origin`` and ``typing.get_args`` will be updated to recognize ``ReadOnly``::

    assert get_origin(ReadOnly[int]) is ReadOnly
    assert get_args(ReadOnly[int]) == (int,)


Backwards compatibility
=======================

This PEP adds a new feature to ``TypedDict``, so code that inspects ``TypedDict`` types will have to change to support types using it. This is expected to mainly affect type-checkers.

Security implications
=====================

There are no known security consequences arising from this PEP.

How to teach this
=================

Suggested changes to the :mod:`typing` module documentation, in line with current practice:

* Add this PEP to the others listed.
* Add ``typing.ReadOnly``, linked to TypedDict and this PEP.
* Add the following text to the TypedDict entry:

The ``ReadOnly`` type qualifier indicates that an item declared in a ``TypedDict`` definition may be read but not mutated (added, modified or removed). This is useful when the exact type of the value is not known yet, and so modifying it would break structural subtypes. *insert example*

Reference implementation
========================

`pyright 1.1.333 fully implements this proposal <https://github.com/microsoft/pyright/releases/tag/1.1.333>`_.

Rejected alternatives
=====================

A TypedMapping protocol type
----------------------------

An earlier version of this PEP proposed a ``TypedMapping`` protocol type, behaving much like a read-only TypedDict but without the constraint that the runtime type be a ``dict``. The behavior described in the current version of this PEP could then be obtained by inheriting a TypedDict from a TypedMapping. This has been set aside for now as more complex, without a strong use-case motivating the additional complexity.

A higher-order ReadOnly type
----------------------------

A generalized higher-order type could be added that removes mutator methods from its parameter, e.g. ``ReadOnly[MovieRecord]``. For a TypedDict, this would be like adding ``ReadOnly`` to every item, including those declared in superclasses. This would naturally want to be defined for a wider set of types than just TypedDict subclasses, and also raises questions about whether and how it applies to nested types. We decided to keep the scope of this PEP narrower.

Calling the type ``Readonly``
-----------------------------

``Read-only`` is generally hyphenated, and it appears to be common convention to put initial caps onto words separated by a dash when converting to CamelCase. This appears consistent with the definition of CamelCase on Wikipedia: CamelCase uppercases the first letter of each word. That said, Python examples or counter-examples, ideally from the core Python libraries, or better explicit guidance on the convention, would be greatly appreciated.

Reusing the ``Final`` annotation
--------------------------------

The :class:`~typing.Final` annotation prevents an attribute from being modified, like the proposed ``ReadOnly`` qualifier does for ``TypedDict`` items. However, it is also documented as preventing redefinition in subclasses too; from :pep:`591`:

    The ``typing.Final`` type qualifier is used to indicate that a variable or attribute should not be reassigned, redefined, or overridden.

This does not fit with the intended use of ``ReadOnly``. Rather than introduce confusion by having ``Final`` behave differently in different contexts, we chose to introduce a new qualifier.

A readonly flag
---------------

Earlier versions of this PEP introduced a boolean flag that would ensure all items in a TypedDict were read-only::

    class Movie(TypedDict, readonly=True):
        name: str
        year: NotRequired[int | None]

    movie: Movie = { "name": "A Clockwork Orange" }
    movie["year"] = 1971  # Type check error: "year" is read-only

However, this led to confusion when inheritance was introduced::

    class A(TypedDict):
        key1: int

    class B(A, TypedDict, readonly=True):
        key2: int

    b: B = { "key1": 1, "key2": 2 }
    b["key1"] = 4  # Accepted by type checker: "key1" is not read-only

It would be reasonable for someone familiar with ``frozen`` (from :mod:`dataclasses`), on seeing just the definition of B, to assume that the whole type was read-only. On the other hand, it would be reasonable for someone familiar with ``total`` to assume that read-only only applies to the current type.

The original proposal attempted to eliminate this ambiguity by making it both a type check and a runtime error to define ``B`` in this way. This was still a source of surprise to people expecting it to work like ``total``.

Given that no extra types could be expressed with the ``readonly`` flag, it has been removed from the proposal to avoid ambiguity and surprise.

Supporting type-checked removal of read-only qualifier via copy and other methods
---------------------------------------------------------------------------------

An earlier version of this PEP mandated that code like the following be supported by type-checkers::

    class A(TypedDict):
        x: ReadOnly[int]

    class B(TypedDict):
        x: ReadOnly[str]

    class C(TypedDict):
        x: int | str

    def copy_and_modify(a: A) -> C:
        c: C = copy.copy(a)
        if not c['x']:
            c['x'] = "N/A"
        return c

    def merge_and_modify(a: A, b: B) -> C:
        c: C = a | b
        if not c['x']:
            c['x'] = "N/A"
        return c

However, there is currently no way to express this in the typeshed, meaning type-checkers would be forced to special-case these functions. There is already a way to code these operations that mypy and pyright do support, though arguably this is less readable::

    copied: C = { **a }
    merged: C = { **a, **b }

While not as flexible as would be ideal, the current typeshed stubs are sound, and remain so if this PEP is accepted. Updating the typeshed would require new typing features, like a type constructor to express the type resulting from merging two or more dicts, and a type qualifier to indicate a returned value is not shared (so may have type constraints like read-only and invariance of generics loosened in specific ways), plus details of how type-checkers would be expected to interpret these features. These could be valuable additions to the language, but are outside the scope of this PEP.

Given this, we have deferred any update of the typeshed stubs.

Preventing unspecified keys in TypedDicts
-----------------------------------------

Consider the following "type discrimination" code::

    class A(TypedDict):
      foo: int

    class B(TypedDict):
      bar: int

    def get_field(d: A | B) -> int:
      if "foo" in d:
        return d["foo"]  # !!!
      else:
        return d["bar"]

This is a common idiom, and other languages like Typescript allow it. Technically, however, this code is unsound: ``B`` does not declare ``foo``, but instances of ``B`` may still have the key present, and the associated value may be of any type::

    class C(TypedDict):
      foo: str
      bar: int

    c: C = { "foo": "hi", "bar" 3 }
    b: B = c  # OK: C is structurally compatible with B
    v = get_field(b)  # Returns a string at runtime, not an int!

mypy rejects the definition of ``get_field`` on the marked line with the error ``TypedDict "B" has no key "foo"``, which is a rather confusing error message, but is caused by this unsoundness.

One option for correcting this would be to explicitly prevent ``B`` from holding a ``foo``::

    class B(TypedDict):
      foo: NotRequired[Never]
      bar: int

    b: B = c  # Type check error: key "foo" not allowed in B

However, this requires every possible key that might be used to discriminate on to be explicitly declared in every type, which is not generally feasible. A better option would be to have a way of preventing all unspecified keys from being included in ``B``. mypy supports this using the ``@final`` decorator from :pep:`591`::

    @final
    class B(TypedDict):
      bar: int

The reasoning here is that this prevents ``C`` or any other type from being considered a "subclass" of ``B``, so instances of ``B`` can now be relied on to never hold the key ``foo``, even though it is not explicitly declared to be of bottom type.

With the introduction of read-only items, however, this reasoning would imply type-checkers should ban the following::

    @final
    class D(TypedDict):
      field: ReadOnly[Collection[str]]

    @final
    class E(TypedDict):
      field: list[str]

    e: E = { "field": ["value1", "value2"] }
    d: D = e  # Error?

The conceptual problem here is that TypedDicts are structural types: they cannot really be subclassed. As such, using ``@final`` on them is not well-defined; it is certainly not mentioned in :pep:`591`.

An earlier version of this PEP proposed resolving this by adding a new flag to ``TypedDict`` that would explicitly prevent other keys from being used, but not other kinds of structural compatibility::

    class B(TypedDict, other_keys=Never):
      bar: int

    b: B = c  # Type check error: key "foo" not allowed in B

However, during the process of drafting, the situation changed:

* pyright, which previously worked similarly to mypy in this type discrimination case, `changed to allow the original example without error <https://github.com/microsoft/pyright/commit/6a25a7bf0b5cb3721a06d0e0d6245b2ebfbf053b>`_, despite the unsoundness, due to it being a common idiom
* mypy has `an open issue <https://github.com/python/mypy/issues/15697>`_ to follow the lead of pyright and Typescript and permit the idiom as well
* a `draft of PEP-728 <https://github.com/python/peps/pull/3441>`_ was created that is a superset of the ``other_keys`` functionality

As such, there is less urgency to address this issue in this PEP, and it has been deferred to PEP-728.


Copyright
=========
This document is placed in the public domain or under the
CC0-1.0-Universal license, whichever is more permissive.
````

</details>

<details><summary><b>Step 8 — final</b> (3273 words)</summary>

````text
.. canonical-typing-spec:: :ref:`typing:readonly` and
                           :external+py3.13:data:`typing.ReadOnly`

Abstract
========

:pep:`589` defines the structural type :class:`~typing.TypedDict` for dictionaries with a fixed set of keys.
As ``TypedDict`` is a mutable type, it is difficult to correctly annotate methods which accept read-only parameters in a way that doesn't prevent valid inputs.

This PEP proposes a new type qualifier, ``typing.ReadOnly``, to support these usages. It makes no Python grammar changes. Correct usage of read-only keys of TypedDicts is intended to be enforced only by static type checkers, and will not be enforced by Python itself at runtime.

Motivation
==========

Representing structured data using (potentially nested) dictionaries with string keys is a common pattern in Python programs. :pep:`589` allows these values to be type checked when the exact type is known up-front, but it is hard to write read-only code that accepts more specific variants: for instance, where values may be subtypes or restrict a union of possible types. This is an especially common issue when writing APIs for services, which may support a wide range of input structures, and typically do not need to modify their input.

Pure functions
--------------

Consider trying to add type hints to a function ``movie_string``::

    def movie_string(movie: Movie) -> str:
        if movie.get("year") is None:
            return movie["name"]
        else:
            return f'{movie["name"]} ({movie["year"]})'

We could define this ``Movie`` type using a ``TypedDict``::

    from typing import NotRequired, TypedDict

    class Movie(TypedDict):
        name: str
        year: NotRequired[int | None]

But suppose we have another type where year is required::

    class MovieRecord(TypedDict):
        name: str
        year: int

Attempting to pass a ``MovieRecord`` into ``movie_string`` results in the error (using mypy):

.. code-block:: text

    Argument 1 to "movie_string" has incompatible type "MovieRecord"; expected "Movie"

This particular use case should be type-safe, but the type checker correctly stops the
user from passing a ``MovieRecord`` into a ``Movie`` parameter in the general case, because
the ``Movie`` class has mutator methods that could potentially allow the function to break
the type constraints in ``MovieRecord`` (e.g. with ``movie["year"] = None`` or ``del movie["year"]``).
The problem disappears if we don't have mutator methods in ``Movie``. This could be achieved by defining an immutable interface using a :pep:`544` :class:`~typing.Protocol`::

    from typing import Literal, Protocol, overload

    class Movie(Protocol):
        @overload
        def get(self, key: Literal["name"]) -> str: ...

        @overload
        def get(self, key: Literal["year"]) -> int | None: ...

        @overload
        def __getitem__(self, key: Literal["name"]) -> str: ...

        @overload
        def __getitem__(self, key: Literal["year"]) -> int | None: ...

This is very repetitive, easy to get wrong, and is still missing important method definitions like ``__contains__()`` and ``keys()``.

Updating nested dicts
---------------------

The structural typing of ``TypedDict`` is supposed to permit writing update functions that only constrain the types of items they modify::

    class HasTimestamp(TypedDict):
        timestamp: float

    class Logs(TypedDict):
        timestamp: float
        loglines: list[str]

    def update_timestamp(d: HasTimestamp) -> None:
        d["timestamp"] = now()

    def add_logline(logs: Logs, logline: str) -> None:
        logs["loglines"].append(logline)
        update_timestamp(logs)  # Accepted by type checker

However, this no longer works once you start nesting dictionaries::

    class HasTimestampedMetadata(TypedDict):
        metadata: HasTimestamp

    class UserAudit(TypedDict):
        name: str
        metadata: Logs

    def update_metadata_timestamp(d: HasTimestampedMetadata) -> None:
        d["metadata"]["timestamp"] = now()

    def rename_user(d: UserAudit, name: str) -> None:
        d["name"] = name
        update_metadata_timestamp(d)  # Type check error: "metadata" is not of type HasTimestamp

This looks like an error, but is simply due to the (unwanted) ability to overwrite the ``metadata`` item held by the ``HasTimestampedMetadata`` instance with a different ``HasTimestamp`` instance, that may no longer be a ``Logs`` instance.

It is possible to work around this issue with generics (as of Python 3.11), but it is very complicated, requiring a type parameter for every nested dict.


Rationale
=========

These problems can be resolved by removing the ability to update one or more of the items in a ``TypedDict``. This does not mean the items are immutable: a reference to the underlying dictionary could still exist with a different but compatible type in which those items have mutator operations. These items are "read-only", and we introduce a new ``typing.ReadOnly`` type qualifier for this purpose.

The ``movie_string`` function in the first motivating example can then be typed as follows::

    from typing import NotRequired, ReadOnly, TypedDict

    class Movie(TypedDict):
        name: ReadOnly[str]
        year: ReadOnly[NotRequired[int | None]]

    def movie_string(movie: Movie) -> str:
        if movie.get("year") is None:
            return movie["name"]
        else:
            return f'{movie["name"]} ({movie["year"]})'

A mixture of read-only and non-read-only items is permitted, allowing the second motivating example to be correctly annotated::

    class HasTimestamp(TypedDict):
        timestamp: float

    class HasTimestampedMetadata(TypedDict):
        metadata: ReadOnly[HasTimestamp]

    def update_metadata_timestamp(d: HasTimestampedMetadata) -> None:
        d["metadata"]["timestamp"] = now()

    class Logs(HasTimestamp):
        loglines: list[str]

    class UserAudit(TypedDict):
        name: str
        metadata: Logs

    def rename_user(d: UserAudit, name: str) -> None:
        d["name"] = name
        update_metadata_timestamp(d)  # Now OK

In addition to these benefits, by flagging arguments of a function as read-only (by using a ``TypedDict`` like ``Movie`` with read-only items), it makes explicit not just to typecheckers but also to users that the function is not going to modify its inputs, which is usually a desirable property of a function interface.

This PEP proposes making ``ReadOnly`` valid only in a ``TypedDict``. A possible future extension would be to support it in additional contexts, such as in protocols.


Specification
=============

A new ``typing.ReadOnly`` type qualifier is added.

``typing.ReadOnly`` type qualifier
----------------------------------

The ``typing.ReadOnly`` type qualifier is used to indicate that an item declared in a ``TypedDict`` definition may not be mutated (added, modified, or removed)::

    from typing import ReadOnly

    class Band(TypedDict):
        name: str
        members: ReadOnly[list[str]]

    blur: Band = {"name": "blur", "members": []}
    blur["name"] = "Blur"  # OK: "name" is not read-only
    blur["members"] = ["Damon Albarn"]  # Type check error: "members" is read-only
    blur["members"].append("Damon Albarn")  # OK: list is mutable

Alternative functional syntax
-----------------------------

The :pep:`alternative functional syntax <589#alternative-syntax>` for TypedDict also supports the new type qualifier::

   Band = TypedDict("Band", {"name": str, "members": ReadOnly[list[str]]})

Interaction with other special types
------------------------------------

``ReadOnly[]`` can be used with ``Required[]``, ``NotRequired[]`` and ``Annotated[]``, in any nesting order:

::

    class Movie(TypedDict):
        title: ReadOnly[Required[str]]  # OK
        year: ReadOnly[NotRequired[Annotated[int, ValueRange(-9999, 9999)]]]  # OK

::

    class Movie(TypedDict):
        title: Required[ReadOnly[str]]  # OK
        year: Annotated[NotRequired[ReadOnly[int]], ValueRange(-9999, 9999)]  # OK

This is consistent with the behavior introduced in :pep:`655`.

Inheritance
-----------

Subclasses can redeclare read-only items as non-read-only, allowing them to be mutated::

    class NamedDict(TypedDict):
        name: ReadOnly[str]

    class Album(NamedDict):
        name: str
        year: int

    album: Album = { "name": "Flood", "year": 1990 }
    album["year"] = 1973
    album["name"] = "Dark Side Of The Moon"  # OK: "name" is not read-only in Album

If a read-only item is not redeclared, it remains read-only::

    class Album(NamedDict):
        year: int

    album: Album = { "name": "Flood", "year": 1990 }
    album["name"] = "Dark Side Of The Moon"  # Type check error: "name" is read-only in Album

Subclasses can narrow value types of read-only items::

    class AlbumCollection(TypedDict):
        albums: ReadOnly[Collection[Album]]

    class RecordShop(AlbumCollection):
        name: str
        albums: ReadOnly[list[Album]]  # OK: "albums" is read-only in AlbumCollection

Subclasses can require items that are read-only but not required in the superclass::

    class OptionalName(TypedDict):
        name: ReadOnly[NotRequired[str]]

    class RequiredName(OptionalName):
        name: ReadOnly[Required[str]]

    d: RequiredName = {}  # Type check error: "name" required

Subclasses can combine these rules::

    class OptionalIdent(TypedDict):
        ident: ReadOnly[NotRequired[str | int]]

    class User(OptionalIdent):
        ident: str  # Required, mutable, and not an int

Note that these are just consequences of structural typing, but they are highlighted here as the behavior now differs from the rules specified in :pep:`589`.

Type consistency
----------------

*This section updates the type consistency rules introduced in* :pep:`589` *to cover the new feature in this PEP. In particular, any pair of types that do not use the new feature will be consistent under these new rules if (and only if) they were already consistent.*

A TypedDict type ``A`` is consistent with TypedDict ``B`` if ``A`` is structurally compatible with ``B``. This is true if and only if all of the following are satisfied:

* For each item in ``B``, ``A`` has the corresponding key, unless the item in ``B`` is read-only, not required, and of top value type (``ReadOnly[NotRequired[object]]``).
* For each item in ``B``, if ``A`` has the corresponding key, the corresponding value type in ``A`` is consistent with the value type in ``B``.
* For each non-read-only item in ``B``, its value type is consistent with the corresponding value type in ``A``.
* For each required key in ``B``, the corresponding key is required in ``A``.
* For each non-required key in ``B``, if the item is not read-only in ``B``, the corresponding key is not required in ``A``.

Discussion:

* All non-specified items in a TypedDict implicitly have value type ``ReadOnly[NotRequired[object]]``.

* Read-only items behave covariantly, as they cannot be mutated. This is similar to container types such as ``Sequence``, and different from non-read-only items, which behave invariantly. Example::

    class A(TypedDict):
        x: ReadOnly[int | None]

    class B(TypedDict):
        x: int

    def f(a: A) -> None:
        print(a["x"] or 0)

    b: B = {"x": 1}
    f(b)  # Accepted by type checker

* A TypedDict type ``A`` with no explicit key ``'x'`` is not consistent with a TypedDict type ``B`` with a non-required key ``'x'``, since at runtime the key ``'x'`` could be present and have an incompatible type (which may not be visible through ``A`` due to structural subtyping). The only exception to this rule is if the item in ``B`` is read-only, and the value type is of top type (``object``). For example::

    class A(TypedDict):
        x: int

    class B(TypedDict):
        x: int
        y: ReadOnly[NotRequired[object]]

    a: A = { "x": 1 }
    b: B = a  # Accepted by type checker

Update method
-------------

In addition to existing type checking rules, type checkers should error if a TypedDict with a read-only item is updated with another TypedDict that declares that key::

    class A(TypedDict):
        x: ReadOnly[int]
        y: int

    a1: A = { "x": 1, "y": 2 }
    a2: A = { "x": 3, "y": 4 }
    a1.update(a2)  # Type check error: "x" is read-only in A

Unless the declared value is of bottom type (:data:`~typing.Never`)::

    class B(TypedDict):
        x: NotRequired[typing.Never]
        y: ReadOnly[int]

    def update_a(a: A, b: B) -> None:
        a.update(b)  # Accepted by type checker: "x" cannot be set on b

Note: Nothing will ever match the ``Never`` type, so an item annotated with it must be absent.

Keyword argument typing
-----------------------

:pep:`692` introduced ``Unpack`` to annotate ``**kwargs`` with a ``TypedDict``. Marking one or more of the items of a ``TypedDict`` used in this way as read-only will have no effect on the type signature of the method. However, it *will* prevent the item from being modified in the body of the function::

    class Args(TypedDict):
        key1: int
        key2: str

    class ReadOnlyArgs(TypedDict):
        key1: ReadOnly[int]
        key2: ReadOnly[str]

    class Function(Protocol):
        def __call__(self, **kwargs: Unpack[Args]) -> None: ...

    def impl(**kwargs: Unpack[ReadOnlyArgs]) -> None:
        kwargs["key1"] = 3  # Type check error: key1 is readonly

    fn: Function = impl  # Accepted by type checker: function signatures are identical

Runtime behavior
----------------

``TypedDict`` types will gain two new attributes, ``__readonly_keys__`` and ``__mutable_keys__``, which will be frozensets containing all read-only and non-read-only keys, respectively::

    class Example(TypedDict):
        a: int
        b: ReadOnly[int]
        c: int
        d: ReadOnly[int]

    assert Example.__readonly_keys__ == frozenset({'b', 'd'})
    assert Example.__mutable_keys__ == frozenset({'a', 'c'})

``typing.get_type_hints`` will strip out any ``ReadOnly`` type qualifiers, unless ``include_extras`` is ``True``::

    assert get_type_hints(Example)['b'] == int
    assert get_type_hints(Example, include_extras=True)['b'] == ReadOnly[int]

``typing.get_origin`` and ``typing.get_args`` will be updated to recognize ``ReadOnly``::

    assert get_origin(ReadOnly[int]) is ReadOnly
    assert get_args(ReadOnly[int]) == (int,)


Backwards compatibility
=======================

This PEP adds a new feature to ``TypedDict``, so code that inspects ``TypedDict`` types will have to change to support types using it. This is expected to mainly affect type-checkers.

Security implications
=====================

There are no known security consequences arising from this PEP.

How to teach this
=================

Suggested changes to the :mod:`typing` module documentation, in line with current practice:

* Add this PEP to the others listed.
* Add ``typing.ReadOnly``, linked to TypedDict and this PEP.
* Add the following text to the TypedDict entry:

The ``ReadOnly`` type qualifier indicates that an item declared in a ``TypedDict`` definition may be read but not mutated (added, modified or removed). This is useful when the exact type of the value is not known yet, and so modifying it would break structural subtypes. *insert example*

Reference implementation
========================

`pyright 1.1.333 fully implements this proposal <https://github.com/microsoft/pyright/releases/tag/1.1.333>`_.

Rejected alternatives
=====================

A TypedMapping protocol type
----------------------------

An earlier version of this PEP proposed a ``TypedMapping`` protocol type, behaving much like a read-only TypedDict but without the constraint that the runtime type be a ``dict``. The behavior described in the current version of this PEP could then be obtained by inheriting a TypedDict from a TypedMapping. This has been set aside for now as more complex, without a strong use-case motivating the additional complexity.

A higher-order ReadOnly type
----------------------------

A generalized higher-order type could be added that removes mutator methods from its parameter, e.g. ``ReadOnly[MovieRecord]``. For a TypedDict, this would be like adding ``ReadOnly`` to every item, including those declared in superclasses. This would naturally want to be defined for a wider set of types than just TypedDict subclasses, and also raises questions about whether and how it applies to nested types. We decided to keep the scope of this PEP narrower.

Calling the type ``Readonly``
-----------------------------

``Read-only`` is generally hyphenated, and it appears to be common convention to put initial caps onto words separated by a dash when converting to CamelCase. This appears consistent with the definition of CamelCase on Wikipedia: CamelCase uppercases the first letter of each word. That said, Python examples or counter-examples, ideally from the core Python libraries, or better explicit guidance on the convention, would be greatly appreciated.

Reusing the ``Final`` annotation
--------------------------------

The :class:`~typing.Final` annotation prevents an attribute from being modified, like the proposed ``ReadOnly`` qualifier does for ``TypedDict`` items. However, it is also documented as preventing redefinition in subclasses too; from :pep:`591`:

    The ``typing.Final`` type qualifier is used to indicate that a variable or attribute should not be reassigned, redefined, or overridden.

This does not fit with the intended use of ``ReadOnly``. Rather than introduce confusion by having ``Final`` behave differently in different contexts, we chose to introduce a new qualifier.

A readonly flag
---------------

Earlier versions of this PEP introduced a boolean flag that would ensure all items in a TypedDict were read-only::

    class Movie(TypedDict, readonly=True):
        name: str
        year: NotRequired[int | None]

    movie: Movie = { "name": "A Clockwork Orange" }
    movie["year"] = 1971  # Type check error: "year" is read-only

However, this led to confusion when inheritance was introduced::

    class A(TypedDict):
        key1: int

    class B(A, TypedDict, readonly=True):
        key2: int

    b: B = { "key1": 1, "key2": 2 }
    b["key1"] = 4  # Accepted by type checker: "key1" is not read-only

It would be reasonable for someone familiar with ``frozen`` (from :mod:`dataclasses`), on seeing just the definition of B, to assume that the whole type was read-only. On the other hand, it would be reasonable for someone familiar with ``total`` to assume that read-only only applies to the current type.

The original proposal attempted to eliminate this ambiguity by making it both a type check and a runtime error to define ``B`` in this way. This was still a source of surprise to people expecting it to work like ``total``.

Given that no extra types could be expressed with the ``readonly`` flag, it has been removed from the proposal to avoid ambiguity and surprise.

Supporting type-checked removal of read-only qualifier via copy and other methods
---------------------------------------------------------------------------------

An earlier version of this PEP mandated that code like the following be supported by type-checkers::

    class A(TypedDict):
        x: ReadOnly[int]

    class B(TypedDict):
        x: ReadOnly[str]

    class C(TypedDict):
        x: int | str

    def copy_and_modify(a: A) -> C:
        c: C = copy.copy(a)
        if not c['x']:
            c['x'] = "N/A"
        return c

    def merge_and_modify(a: A, b: B) -> C:
        c: C = a | b
        if not c['x']:
            c['x'] = "N/A"
        return c

However, there is currently no way to express this in the typeshed, meaning type-checkers would be forced to special-case these functions. There is already a way to code these operations that mypy and pyright do support, though arguably this is less readable::

    copied: C = { **a }
    merged: C = { **a, **b }

While not as flexible as would be ideal, the current typeshed stubs are sound, and remain so if this PEP is accepted. Updating the typeshed would require new typing features, like a type constructor to express the type resulting from merging two or more dicts, and a type qualifier to indicate a returned value is not shared (so may have type constraints like read-only and invariance of generics loosened in specific ways), plus details of how type-checkers would be expected to interpret these features. These could be valuable additions to the language, but are outside the scope of this PEP.

Given this, we have deferred any update of the typeshed stubs.

Preventing unspecified keys in TypedDicts
-----------------------------------------

Consider the following "type discrimination" code::

    class A(TypedDict):
      foo: int

    class B(TypedDict):
      bar: int

    def get_field(d: A | B) -> int:
      if "foo" in d:
        return d["foo"]  # !!!
      else:
        return d["bar"]

This is a common idiom, and other languages like Typescript allow it. Technically, however, this code is unsound: ``B`` does not declare ``foo``, but instances of ``B`` may still have the key present, and the associated value may be of any type::

    class C(TypedDict):
      foo: str
      bar: int

    c: C = { "foo": "hi", "bar" 3 }
    b: B = c  # OK: C is structurally compatible with B
    v = get_field(b)  # Returns a string at runtime, not an int!

mypy rejects the definition of ``get_field`` on the marked line with the error ``TypedDict "B" has no key "foo"``, which is a rather confusing error message, but is caused by this unsoundness.

One option for correcting this would be to explicitly prevent ``B`` from holding a ``foo``::

    class B(TypedDict):
      foo: NotRequired[Never]
      bar: int

    b: B = c  # Type check error: key "foo" not allowed in B

However, this requires every possible key that might be used to discriminate on to be explicitly declared in every type, which is not generally feasible. A better option would be to have a way of preventing all unspecified keys from being included in ``B``. mypy supports this using the ``@final`` decorator from :pep:`591`::

    @final
    class B(TypedDict):
      bar: int

The reasoning here is that this prevents ``C`` or any other type from being considered a "subclass" of ``B``, so instances of ``B`` can now be relied on to never hold the key ``foo``, even though it is not explicitly declared to be of bottom type.

With the introduction of read-only items, however, this reasoning would imply type-checkers should ban the following::

    @final
    class D(TypedDict):
      field: ReadOnly[Collection[str]]

    @final
    class E(TypedDict):
      field: list[str]

    e: E = { "field": ["value1", "value2"] }
    d: D = e  # Error?

The conceptual problem here is that TypedDicts are structural types: they cannot really be subclassed. As such, using ``@final`` on them is not well-defined; it is certainly not mentioned in :pep:`591`.

An earlier version of this PEP proposed resolving this by adding a new flag to ``TypedDict`` that would explicitly prevent other keys from being used, but not other kinds of structural compatibility::

    class B(TypedDict, other_keys=Never):
      bar: int

    b: B = c  # Type check error: key "foo" not allowed in B

However, during the process of drafting, the situation changed:

* pyright, which previously worked similarly to mypy in this type discrimination case, `changed to allow the original example without error <https://github.com/microsoft/pyright/commit/6a25a7bf0b5cb3721a06d0e0d6245b2ebfbf053b>`_, despite the unsoundness, due to it being a common idiom
* mypy has `an open issue <https://github.com/python/mypy/issues/15697>`_ to follow the lead of pyright and Typescript and permit the idiom as well
* a `draft of PEP-728 <https://github.com/python/peps/pull/3441>`_ was created that is a superset of the ``other_keys`` functionality

As such, there is less urgency to address this issue in this PEP, and it has been deferred to PEP-728.


Copyright
=========
This document is placed in the public domain or under the
CC0-1.0-Universal license, whichever is more permissive.
````

</details>
