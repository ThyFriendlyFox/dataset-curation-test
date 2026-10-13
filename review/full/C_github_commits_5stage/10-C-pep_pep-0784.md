# 10. Python PEP: Adding Zstandard to the standard library

`C-pep_pep-0784` · [full/C_github_commits_5stage](README.md)

Source: <https://github.com/python/peps/blob/545c670f1e986162eb7161d63c944108e504bd09/peps/pep-0784.rst> · License: Public domain / CC0-1.0 (PEP text) · 6 commits touching the file; 6 distinct versions

| step | name | words | citations | similarity to final | provenance |
|---|---|---|---|---|---|
| 0 | title | 6 | 0 | 0.00 | source_title |
| 1 | earliest_version | 1745 | 0 | 0.75 | commit 77031b781f (2025-04-07) |
| 2 | early_revision | 1796 | 0 | 0.81 | commit ded32dd213 (2025-04-07) |
| 3 | late_revision | 2251 | 0 | 0.93 | commit f7d669e95c (2025-04-15) |
| 4 | final | 2127 | 0 | 1.00 | commit b8a7cb62b3 (2025-05-23) |

<details><summary><b>Step 0 — title</b> (6 words)</summary>

````text
Adding Zstandard to the standard library
````

</details>

<details><summary><b>Step 1 — earliest_version</b> (1745 words)</summary>

````text
Abstract
========

`Zstandard <https://facebook.github.io/zstd/>`_ is a widely adopted, mature,
and highly efficient compression standard. This PEP proposes adding a new
module to the Python standard library containing a Python wrapper around Meta's
``zstd`` library, the default implementation. Additionally, to avoid name
collisions with packages on PyPI and to present a unified interface to Python
users, compression modules in the standard library will be moved under a
``compression.*`` namespace package.

Motivation
==========

CPython has modules for several different compression formats, such as `zlib
(DEFLATE) <https://docs.python.org/3/library/zlib.html>`_,
`bzip2 <https://docs.python.org/3/library/bz2.html>`_,
and `lzma <https://docs.python.org/3/library/lzma.html>`_, each widely used.
Including popular compression algorithms matches Python's "batteries included"
philosophy of incorporating widely useful standards and utilities. The last
compression module added to the language was ``lzma``, added in Python 3.3.

Since then, Zstandard has become the modern de facto preferred compression
library for both high performance compression and decompression attaining high
compression ratios at reasonable CPU and memory cost. Zstandard achieves a much
higher compression ratio than bzip2 or zlib (DEFLATE) while decompressing
significantly faster than LZMA.

Zstandard has seen `widespread adoption in many different areas of computing
<https://facebook.github.io/zstd/#references>`_. The numerous hardware
implementations demonstrate long-term commitment to Zstandard and an
expectation that Zstandard will stay the de facto choice for compression for
years to come. Zstandard compression is also implemented in both the ZFS and
Btrfs filesystems.

Zstandard's highly efficient compression has supplanted other modern
compression formats, such as brotli, lzo, and ucl due to its highly efficient
compression. While `LZ4 <https://lz4.org/>`_ is still used in very high
throughput scenarios, Zstandard can also be used in some of these contexts.
While inclusion of LZ4 is out of scope, it would be a compelling future
addition to the ``compression`` namespace introduced by this PEP.

There are several bindings to Zstandard for Python available on PyPI, each with
different APIs and choices of how to bind the ``zstd`` library. One goal with
introducing an official module in the standard library is to reduce confusion
for Python users who want simple compression/decompression APIs for Zstandard.
The existing packages can continue providing extended APIs and bindings for
other Python implementations such as PyPy or integrate features from newer
Zstandard versions.

Another reason to add Zstandard support to the standard library is to resolve
a long standing `open issue <https://github.com/python/cpython/issues/81276>`_
requesting Zstandard support in the ``tarfile`` module. This issue has the 5th
most "thumbs up" of open issues on the CPython tracker, and has garnered a
significant amount of discussion and interest. Additionally, the `ZIP format
standardizes a Zstandard compression format ID
<https://pkwaredownloads.blob.core.windows.net/pkware-general/Documentation/APPNOTE-6.3.8.TXT>`_,
and integration with ``zipfile`` would allow opening ZIP archives using
Zstandard compression. The reference implementation for this PEP contains
integration with the ``zipfile``, ``tarfile``, and ``shutil`` modules.

Zstandard compression could also be used to make Python wheel packages smaller
and significantly faster to install. Anaconda found a sizeable speedup when
adopting Zstandard for the conda package format

.. epigraph::

    Conda's download sizes are reduced ~30-40%, and extraction is dramatically faster.
    [...]
    We see approximately a 2.5x overall speedup, almost all thanks to the dramatically faster extraction speed of the zstd compression used in the new file format.

    -- `Anaconda blog on Zstandard adoption <https://www.anaconda.com/blog/how-we-made-conda-faster-4-7>`_

`According to lzbench <https://github.com/inikep/lzbench?tab=readme-ov-file#benchmarks>`_,
a comprehensive benchmark of many different compression libraries and formats,
Zstandard has a significantly higher compression ratio compared to wheel's
existing zlib-based compression. While this PEP does *not* prescribe any
changes to the wheel format or other packaging standards, having Zstandard
bindings in the standard library would enable a future PEP to improve the user
experience for Python wheel packages.

Rationale
=========

Introduction of a ``compression`` namespace
-------------------------------------------

Both the ``zstd`` and ``zstandard`` import names are claimed by projects on
PyPI. To avoid breaking users of one of the existing bindings, this PEP
proposes introducing a new namespace for compression libraries,
``compression``. This name is already reserved on PyPI for use in the
standard library. The new Zstandard module will be ``compression.zstd``.
Other compression modules will be re-exported to the ``compression`` namespace
and their current import names will be deprecated.

Providing a common namespace for compression modules has several advantages.
First, it reduces user confusion about where to find compression modules.
Second, the top level ``compression`` module could provide information on which
compression formats are available, similar to ``hashlib``'s
``algorithms_available``. If :pep:`775` is accepted, a
``compression.algorithms_guaranteed`` could be provided as well, listing
``zlib``. Finally, a ``compression`` namespace prevents future issues with
merging other compression formats into the standard library. New compression
formats will likely be published to PyPI prior to integration into
CPython. Therefore, any new compression format import name will likely already
be claimed by the time a module would be considered for inclusion in CPython.
Putting compression modules under a package prefix prevents issues with
potential future name clashes.

Code that would like to remain compatible across Python versions may use the
following pattern to ensure compatibility::

  try:
      from compression.lzma import LZMAFile
  except ImportError:
      from lzma import LZMAFile

This will use the newer import name when available and fall back to the old
name otherwise.

Implementation based on ``pyzstd``
----------------------------------

The implementation for this PEP is based on the `pyzstd project <https://github.com/Rogdham/pyzstd>`_.
This project was chosen as the code was `originally written to be upstreamed <https://github.com/python/cpython/issues/81276#issuecomment-1093824963>`_
to CPython by Ma Lin, who also wrote the `output buffer implementation used in
the standard library today <https://github.com/python/cpython/commit/f9bedb630e8a0b7d94e1c7e609b20dfaa2b22231>`_.
The project has since been taken over by Rogdham and is published to PyPI. The
APIs in ``pyzstd`` are similar to the APIs for other compression modules in the
standard library such as ``bz2`` and ``lzma``.

Minimum supported Zstandard version
-----------------------------------

The minimum supported Zstandard was chosen as v1.4.5, released in May of 2020.
This version was chosen as a minimum based on reviewing the versions of
Zstandard available in a number of Linux distribution package repositories,
including LTS releases. This version choice is rather conservative to maximize
compatibility with existing LTS Linux distributions, but a newer Zstandard
version could likely be chosen given that newer Python releases are generally
packaged as part of newer distribution releases.

Specification
=============

The ``compression`` namespace
-----------------------------

A new namespace package for compression modules will be introduced named
``compression``. The top-level module for this package will be empty to begin
with, but a standard API for interacting with compression routines may be
added in the future to the toplevel.

The ``compression.zstd`` module
-------------------------------

A new module, ``compression.zstd`` will be introduced with Zstandard
compression APIs that match other compression modules in the standard library,
namely

* ``compress`` / ``decompress`` - APIs for one-shot compression/decompression
* ``ZstdFile`` / ``open`` - APIs for interacting with streams and file-like
  objects
* ``ZstdCompressor`` / ``ZstdDecompressor`` - APIs for incremental compression/
  decompression

It will also contain some Zstandard-specific functionality

* ``ZstdDict`` / ``train_dict`` / ``finalize_dict`` - APIs for interacting with
  Zstandard dictionaries, which are useful for compressing many small chunks of
  similar data

``libzstd`` optional dependency
-------------------------------

The ``libzstd`` library will become an optional dependency of CPython. If the
library is not available, the ``compression.zstd`` module will be unavailable.
This is handled automatically on Unix platforms as part of the normal build
environment detection.

On Windows, ``libzstd`` will be added to
`the source dependencies <https://github.com/python/cpython-source-deps>`_
used to build libraries CPython depends on for Windows.

Other compression modules
-------------------------

New import names ``compression.lzma``, ``compression.bz2``, and
``compression.zlib`` will be introduced in Python 3.14 re-exporting the
contents of the existing ``lzma``, ``bz2``, and ``zlib`` modules respectively.

The ``_compression`` module, given that it is marked private, will be
immediately renamed to ``compression._common.streams``. The new name was
selected due to the current contents of the module being I/O related helpers
for stream APIs (e.g. ``LZMAFile``) in standard library compression modules.

Compression module migration timeline
-------------------------------------

Existing modules will emit a ``DeprecationWarning`` in the Python
release following the last Python without the ``compression`` module leaving
support. For example, if the ``compression`` namespace is introduced in 3.14,
then the ``DeprecationWarnings`` would be emitted in 3.19, the next release
after 3.13 reaches end of life. Following the standard deprecation timeline
specified in :pep:`387`, in Python 3.24 the existing modules will be removed
and code must use the ``compression`` sub-modules. The documentation for these
modules will be updated to discuss the planned deprecation and removal
timelines.


Backwards Compatibility
=======================

The main compatibility concern is usage of existing standard library
compression APIs with the existing import names. These names will be
deprecated in 3.19 and will be removed in 3.24. Given the long coexistance of
the modules and a 5 year deprecation period, most users will likely migrate to
the new import names well before then. Additionally, a libCST codemod can be
provided to automatically rewrite imports, easing the migration.

Security Implications
=====================

As with any new C code, especially code operating on potentially untrusted user
input, there are risks of memory safety issues. The author plans on
contributing integration with libfuzzer to enable fuzzing the ``_zstd`` code
and ensure it is robust. Furthermore, there are a number of tests that exercise
the compression and decompression routines. These tests pass without error when
compiled with AddressSanitizer.

Taking on a new dependency also always has security risks, but the ``zstd``
library is mature, fuzzed on each commit, and `participates in Meta's bug bounty
program <https://github.com/facebook/zstd/blob/dev/SECURITY.md>`_.

How to Teach This
=================

Documentation for the new module is in the reference implementation branch. The
documentation for other modules will be updated to discuss the deprecation of
their existing import names, and how to migrate.

Reference Implementation
========================

The `reference implementation <https://github.com/emmatyping/cpython/tree/zstd>`_
contains the ``_zstd`` C code, the ``compression.zstd`` code, modifications to
``tarfile``, ``shutil``, and ``zipfile``, and tests for each new API and
integration added. It also contains the re-exports of other compression
modules. Deprecations for the existing import names will be added once a
decision is reached regarding the open issues.

Rejected Ideas
==============

Name the module ``libzstd`` and do not make a new ``compression`` namespace
---------------------------------------------------------------------------

One option instead of making a new ``compression`` namespace would be to find
a different name, such as ``libzstd``, as the import name. However, the issue
of existing import names is likely to persist for future compression formats
added to the standard library. LZ4, a common high speed compression format,
has `a package on PyPI <https://pypi.org/project/lz4/>`_, ``lz4``, with the
import name ``lz4``. Instead of solving this issue for each compression format,
it is better to solve it once and for all by using the already-claimed
``compression`` namespace.

Copyright
=========

This document is placed in the public domain or under the
CC0-1.0-Universal license, whichever is more permissive.
````

</details>

<details><summary><b>Step 2 — early_revision</b> (1796 words)</summary>

````text
Abstract
========

`Zstandard`_ is a widely adopted, mature, and highly efficient compression
standard. This PEP proposes adding a new module to the Python standard library
containing a Python wrapper around Meta's |zstd| library, the default
implementation. Additionally, to avoid name collisions with packages on PyPI
and to present a unified interface to Python users, compression modules in the
standard library will be moved under a ``compression.*`` package.

.. |zstd| replace:: ``zstd``
.. _zstd: https://facebook.github.io/zstd/
.. _Zstandard: https://facebook.github.io/zstd/


Motivation
==========

CPython has modules for several different compression formats, such as
:mod:`zlib (DEFLATE) <zlib>`, :mod:`bzip2 <bz2>`, and :mod:`lzma <lzma>`,
each widely used. Including popular compression algorithms matches Python's
"batteries included" philosophy of incorporating widely useful standards and
utilities. :mod:`!lzma` is the most recent such module, added in Python 3.3.

Since then, Zstandard has become the modern *de facto* preferred compression
library for both high performance compression and decompression attaining high
compression ratios at reasonable CPU and memory cost. Zstandard achieves a much
higher compression ratio than bzip2 or zlib (DEFLATE) while decompressing
significantly faster than LZMA.

Zstandard has seen `widespread adoption`_ in many different areas of computing.
The numerous hardware implementations demonstrate long-term commitment to
Zstandard and an expectation that Zstandard will stay the *de facto* choice for
compression for years to come. Zstandard compression is also implemented in
both the ZFS_ and Btrfs_ filesystems.

Zstandard's highly efficient compression has supplanted other modern
compression formats, such as brotli_, lzo_, and ucl_ due to its highly
efficient compression. While `LZ4`_ is still used in very high throughput
scenarios, Zstandard can also be used in some of these contexts.
While inclusion of LZ4 is out of scope, it would be a compelling future
addition to the ``compression`` namespace introduced by this PEP.

There are several bindings to Zstandard for Python available on PyPI, each with
different APIs and choices of how to bind the ``zstd`` library. One goal with
introducing an official module in the standard library is to reduce confusion
for Python users who want simple compression/decompression APIs for Zstandard.
The existing packages can continue providing extended APIs or integrate
features from newer Zstandard versions.

Another reason to add Zstandard support to the standard library is to resolve
a long standing open issue (`python/cpython#81276`_) requesting Zstandard
support in the :mod:`tarfile` module. This issue has the 5th most "thumbs up"
of open issues on the CPython tracker, and has garnered a significant amount of
discussion and interest. Additionally, the ZIP format standardizes a
`Zstandard compression format ID`_, and integration with the :mod:`zipfile`
module would allow opening ZIP archives using Zstandard compression. The
reference implementation for this PEP contains integration with the
:mod:`!zipfile`, :mod:`!tarfile`, and :mod:`shutil` modules.

Zstandard compression could also be used to make Python wheel packages smaller
and significantly faster to install. Anaconda found a sizeable speedup when
adopting Zstandard for the conda package format:

.. epigraph::

    Conda's download sizes are reduced ~30-40%, and extraction is dramatically faster.
    [...]
    We see approximately a 2.5x overall speedup, almost all thanks to the dramatically faster extraction speed of the zstd compression used in the new file format.

    -- `Anaconda blog on Zstandard adoption`_

Zstandard has a significantly higher compression ratio compared to wheel's
existing zlib-based compression, `according to lzbench`_, a comprehensive
benchmark of many different compression libraries and formats.
While this PEP does *not* prescribe any changes to the wheel format or other
packaging standards, having Zstandard bindings in the standard library would
enable a future PEP to improve the user experience for Python wheel packages.

.. _widespread adoption: https://facebook.github.io/zstd/#references
.. _ZFS: https://en.wikipedia.org/wiki/ZFS
.. _Btrfs: https://btrfs.readthedocs.io/
.. _brotli: https://brotli.org/
.. _lzo: https://www.oberhumer.com/opensource/lzo/
.. _ucl: https://www.oberhumer.com/opensource/ucl/
.. _LZ4: https://lz4.org/
.. _python/cpython#81276: https://github.com/python/cpython/issues/81276
.. _Zstandard compression format ID: https://pkwaredownloads.blob.core.windows.net/pkware-general/Documentation/APPNOTE-6.3.8.TXT
.. _according to lzbench: https://github.com/inikep/lzbench#benchmarks
.. _Anaconda blog on Zstandard adoption: https://www.anaconda.com/blog/how-we-made-conda-faster-4-7


Rationale
=========

Introduction of a ``compression`` package
-----------------------------------------

Both the ``zstd`` and ``zstandard`` import names are claimed by projects on
PyPI. To avoid breaking users of one of the existing bindings, this PEP
proposes introducing a new namespace for compression libraries,
``compression``. This name is already reserved on PyPI for use in the
standard library. The new Zstandard module will be ``compression.zstd``.
Other compression modules will be re-exported to the ``compression`` namespace
and their current import names will be deprecated.

Providing a common namespace for compression modules has several advantages.
First, it reduces user confusion about where to find compression modules.
Second, the top level ``compression`` module could provide information on which
compression formats are available, similar to ``hashlib``'s
``algorithms_available``. If :pep:`775` is accepted, a
``compression.algorithms_guaranteed`` could be provided as well, listing
``zlib``. Finally, a ``compression`` namespace prevents future issues with
merging other compression formats into the standard library. New compression
formats will likely be published to PyPI prior to integration into
CPython. Therefore, any new compression format import name will likely already
be claimed by the time a module would be considered for inclusion in CPython.
Putting compression modules under a package prefix prevents issues with
potential future name clashes.

Code that would like to remain compatible across Python versions may use the
following pattern to ensure compatibility::

  try:
      from compression.lzma import LZMAFile
  except ImportError:
      from lzma import LZMAFile

This will use the newer import name when available and fall back to the old
name otherwise.

Implementation based on ``pyzstd``
----------------------------------

The implementation for this PEP is based on the `pyzstd project`_.
This project was chosen as the code was `originally written to be upstreamed`_
to CPython by Ma Lin, who also wrote the `output buffer implementation`_ used in
the standard library today.
The project has since been taken over by Rogdham and is published to PyPI. The
APIs in ``pyzstd`` are similar to the APIs for other compression modules in the
standard library such as :mod:`!bz2` and :mod:`!lzma`.

.. _pyzstd project: https://github.com/Rogdham/pyzstd
.. _originally written to be upstreamed: https://github.com/python/cpython/issues/81276#issuecomment-1093824963
.. _output buffer implementation: https://github.com/python/cpython/commit/f9bedb630e8a0b7d94e1c7e609b20dfaa2b22231

Minimum supported Zstandard version
-----------------------------------

The minimum supported Zstandard was chosen as v1.4.5, released in May of 2020.
This version was chosen as a minimum based on reviewing the versions of
Zstandard available in a number of Linux distribution package repositories,
including LTS releases. This version choice is rather conservative to maximize
compatibility with existing LTS Linux distributions, but a newer Zstandard
version could likely be chosen given that newer Python releases are generally
packaged as part of newer distribution releases.


Specification
=============

The ``compression`` namespace
-----------------------------

A new namespace for compression modules will be introduced named
``compression``. The top-level module for this package will be empty to begin
with, but a standard API for interacting with compression routines may be
added in the future to the toplevel.

The ``compression.zstd`` module
-------------------------------

A new module, ``compression.zstd`` will be introduced with Zstandard
compression APIs that match other compression modules in the standard library,
namely

* :func:`!compress` / :func:`!decompress` - APIs for one-shot compression
  or decompression
* :class:`!ZstdFile` / :func:`!open` - APIs for interacting with streams
  and file-like objects
* :class:`!ZstdCompressor` / :class:`!ZstdDecompressor` - APIs for incremental
  compression or decompression

It will also contain some Zstandard-specific functionality:

* :class:`!ZstdDict` / :func:`!train_dict` / :func:`!finalize_dict` - APIs for
  interacting with Zstandard dictionaries, which are useful for compressing
  many small chunks of similar data

``libzstd`` optional dependency
-------------------------------

The ``libzstd`` library will become an optional dependency of CPython. If the
library is not available, the ``compression.zstd`` module will be unavailable.
This is handled automatically on Unix platforms as part of the normal build
environment detection.

On Windows, ``libzstd`` will be added to
`the source dependencies <https://github.com/python/cpython-source-deps>`_
used to build libraries CPython depends on for Windows.

Other compression modules
-------------------------

New import names ``compression.lzma``, ``compression.bz2``, and
``compression.zlib`` will be introduced in Python 3.14 re-exporting the
contents of the existing ``lzma``, ``bz2``, and ``zlib`` modules respectively.

The ``_compression`` module, given that it is marked private, will be
immediately renamed to ``compression._common.streams``. The new name was
selected due to the current contents of the module being I/O related helpers
for stream APIs (e.g. ``LZMAFile``) in standard library compression modules.

Compression module migration timeline
-------------------------------------

Existing modules will emit a ``DeprecationWarning`` in the Python
release following the last Python without the ``compression`` module leaving
support. For example, if the ``compression`` namespace is introduced in 3.14,
then the ``DeprecationWarnings`` would be emitted in 3.19, the next release
after 3.13 reaches end of life. Following the standard deprecation timeline
specified in :pep:`387`, in Python 3.24 the existing modules will be removed
and code must use the ``compression`` sub-modules. The documentation for these
modules will be updated to discuss the planned deprecation and removal
timelines.


Backwards Compatibility
=======================

The main compatibility concern is usage of existing standard library
compression APIs with the existing import names. These names will be
deprecated in 3.19 and will be removed in 3.24. Given the long coexistence of
the modules and a 5 year deprecation period, most users will likely migrate to
the new import names well before then. Additionally, a libCST codemod can be
provided to automatically rewrite imports, easing the migration.


Security Implications
=====================

As with any new C code, especially code operating on potentially untrusted user
input, there are risks of memory safety issues. The author plans on
contributing integration with libfuzzer to enable fuzzing the ``_zstd`` code
and ensure it is robust. Furthermore, there are a number of tests that exercise
the compression and decompression routines. These tests pass without error when
compiled with AddressSanitizer.

Taking on a new dependency also always has security risks, but the ``zstd``
library is mature, fuzzed on each commit, and `participates in Meta's bug bounty
program <https://github.com/facebook/zstd/blob/dev/SECURITY.md>`_.


How to Teach This
=================

Documentation for the new module is in the reference implementation branch. The
documentation for other modules will be updated to discuss the deprecation of
their existing import names, and how to migrate.


Reference Implementation
========================

The `reference implementation <https://github.com/emmatyping/cpython/tree/zstd>`_
contains the ``_zstd`` C code, the ``compression.zstd`` code, modifications to
``tarfile``, ``shutil``, and ``zipfile``, and tests for each new API and
integration added. It also contains the re-exports of other compression
modules. Deprecations for the existing import names will be added once a
decision is reached regarding the open issues.


Rejected Ideas
==============

Name the module ``libzstd`` and do not make a new ``compression`` namespace
---------------------------------------------------------------------------

One option instead of making a new ``compression`` namespace would be to find
a different name, such as ``libzstd``, as the import name. However, the issue
of existing import names is likely to persist for future compression formats
added to the standard library. LZ4, a common high speed compression format,
has `a package on PyPI <https://pypi.org/project/lz4/>`_, ``lz4``, with the
import name ``lz4``. Instead of solving this issue for each compression format,
it is better to solve it once and for all by using the already-claimed
``compression`` namespace.


Copyright
=========

This document is placed in the public domain or under the
CC0-1.0-Universal license, whichever is more permissive.
````

</details>

<details><summary><b>Step 3 — late_revision</b> (2251 words)</summary>

````text
Abstract
========

`Zstandard`_ is a widely adopted, mature, and highly efficient compression
standard. This PEP proposes adding a new module to the Python standard library
containing a Python wrapper around Meta's |zstd| library, the default
implementation. Additionally, to avoid name collisions with packages on PyPI
and to present a unified interface to Python users, compression modules in the
standard library will be moved under a ``compression.*`` package.

.. |zstd| replace:: ``zstd``
.. _zstd: https://facebook.github.io/zstd/
.. _Zstandard: https://facebook.github.io/zstd/


Motivation
==========

CPython has modules for several different compression formats, such as
:mod:`zlib (DEFLATE) <zlib>`, :mod:`gzip <gzip>`, :mod:`bzip2 <bz2>`, and
:mod:`lzma <lzma>`, each widely used. Including popular compression algorithms
matches Python's "batteries included" philosophy of incorporating widely useful
standards and utilities. :mod:`!lzma` is the most recent such module, added in
Python 3.3.

Since then, Zstandard has become the modern *de facto* preferred compression
library for both high performance compression and decompression attaining high
compression ratios at reasonable CPU and memory cost. Zstandard achieves a much
higher compression ratio than bzip2 or zlib (DEFLATE) while decompressing
significantly faster than LZMA.

Zstandard has seen `widespread adoption`_ in many different areas of computing.
The numerous hardware implementations demonstrate long-term commitment to
Zstandard and an expectation that Zstandard will stay the *de facto* choice for
compression for years to come. This is further evidenced by Zstandard's IETF
standardization in :rfc:`8478`. Zstandard compression is also implemented in
both the ZFS_ and Btrfs_ filesystems.

Zstandard's highly efficient compression has supplanted other modern
compression formats, such as brotli_, lzo_, and ucl_ due to its highly
efficient compression. While `LZ4`_ is still used in very high throughput
scenarios, Zstandard can also be used in some of these contexts.
While inclusion of LZ4 is out of scope, it would be a compelling future
addition to the ``compression`` namespace introduced by this PEP.

There are several bindings to Zstandard for Python available on PyPI, each with
different APIs and choices of how to bind the ``zstd`` library. One goal with
introducing an official module in the standard library is to reduce confusion
for Python users who want simple compression/decompression APIs for Zstandard.
The existing packages can continue providing extended APIs or integrate
features from newer Zstandard versions.

Another reason to add Zstandard support to the standard library is to resolve
a long standing open issue (`python/cpython#81276`_) requesting Zstandard
support in the :mod:`tarfile` module. This issue has the 5th most "thumbs up"
of open issues on the CPython tracker, and has garnered a significant amount of
discussion and interest. Additionally, the ZIP format standardizes a
`Zstandard compression format ID`_, and integration with the :mod:`zipfile`
module would allow opening ZIP archives using Zstandard compression. The
reference implementation for this PEP contains integration with the
:mod:`!zipfile`, :mod:`!tarfile`, and :mod:`shutil` modules.

Zstandard compression could also be used to make Python wheel packages smaller
and significantly faster to install. Anaconda found a sizeable speedup when
adopting Zstandard for the conda package format:

.. epigraph::

    Conda's download sizes are reduced ~30-40%, and extraction is dramatically faster.
    [...]
    We see approximately a 2.5x overall speedup, almost all thanks to the dramatically faster extraction speed of the zstd compression used in the new file format.

    -- `Anaconda blog on Zstandard adoption`_

Zstandard has a significantly higher compression ratio compared to wheel's
existing zlib-based compression, `according to lzbench`_, a comprehensive
benchmark of many different compression libraries and formats.
While this PEP does *not* prescribe any changes to the wheel format or other
packaging standards, having Zstandard bindings in the standard library would
enable a future PEP to improve the user experience for Python wheel packages.

.. _widespread adoption: https://facebook.github.io/zstd/#references
.. _ZFS: https://en.wikipedia.org/wiki/ZFS
.. _Btrfs: https://btrfs.readthedocs.io/
.. _brotli: https://brotli.org/
.. _lzo: https://www.oberhumer.com/opensource/lzo/
.. _ucl: https://www.oberhumer.com/opensource/ucl/
.. _LZ4: https://lz4.org/
.. _python/cpython#81276: https://github.com/python/cpython/issues/81276
.. _Zstandard compression format ID: https://pkwaredownloads.blob.core.windows.net/pkware-general/Documentation/APPNOTE-6.3.8.TXT
.. _according to lzbench: https://github.com/inikep/lzbench#benchmarks
.. _Anaconda blog on Zstandard adoption: https://www.anaconda.com/blog/how-we-made-conda-faster-4-7


Rationale
=========

Introduction of a ``compression`` package
-----------------------------------------

Both the ``zstd`` and ``zstandard`` import names are claimed by projects on
PyPI. To avoid breaking users of one of the existing bindings, this PEP
proposes introducing a new namespace for compression libraries,
``compression``. This name is already reserved on PyPI for use in the
standard library. The new Zstandard module will be ``compression.zstd``.
Other compression modules will be re-exported to the ``compression`` namespace
and their current import names will be deprecated.

Providing a common namespace for compression modules has several advantages.
First, it reduces user confusion about where to find compression modules.
Second, the top level ``compression`` module could provide information on which
compression formats are available, similar to ``hashlib``'s
``algorithms_available``. If :pep:`775` is accepted, a
``compression.algorithms_guaranteed`` could be provided as well, listing
``zlib``. Finally, a ``compression`` namespace prevents future issues with
merging other compression formats into the standard library. New compression
formats will likely be published to PyPI prior to integration into
CPython. Therefore, any new compression format import name will likely already
be claimed by the time a module would be considered for inclusion in CPython.
Putting compression modules under a package prefix prevents issues with
potential future name clashes.

Code that would like to remain compatible across Python versions may use the
following pattern to ensure compatibility::

  try:
      from compression.lzma import LZMAFile
  except ImportError:
      from lzma import LZMAFile

This will use the newer import name when available and fall back to the old
name otherwise.

Implementation based on ``pyzstd``
----------------------------------

The implementation for this PEP is based on the `pyzstd project`_.
This project was chosen as the code was `originally written to be upstreamed`_
to CPython by Ma Lin, who also wrote the `output buffer implementation`_ used in
the standard library today.
The project has since been taken over by Rogdham and is published to PyPI. The
APIs in ``pyzstd`` are similar to the APIs for other compression modules in the
standard library such as :mod:`!bz2` and :mod:`!lzma`.

.. _pyzstd project: https://github.com/Rogdham/pyzstd
.. _originally written to be upstreamed: https://github.com/python/cpython/issues/81276#issuecomment-1093824963
.. _output buffer implementation: https://github.com/python/cpython/commit/f9bedb630e8a0b7d94e1c7e609b20dfaa2b22231

Minimum supported Zstandard version
-----------------------------------

The minimum supported Zstandard was chosen as v1.4.5, released in May of 2020.
This version was chosen as a minimum based on reviewing the versions of
Zstandard available in a number of Linux distribution package repositories,
including LTS releases. This version choice is rather conservative to maximize
compatibility with existing LTS Linux distributions, but a newer Zstandard
version could likely be chosen given that newer Python releases are generally
packaged as part of newer distribution releases.


Specification
=============

The ``compression`` namespace
-----------------------------

A new namespace for compression modules will be introduced named
``compression``. The top-level module for this package will be empty to begin
with, but a standard API for interacting with compression routines may be
added in the future to the toplevel.

The ``compression.zstd`` module
-------------------------------

A new module, ``compression.zstd`` will be introduced with Zstandard
compression APIs that match other compression modules in the standard library,
namely

* :func:`!compress` / :func:`!decompress` - APIs for one-shot compression
  or decompression
* :class:`!ZstdFile` / :func:`!open` - APIs for interacting with streams
  and file-like objects
* :class:`!ZstdCompressor` / :class:`!ZstdDecompressor` - APIs for incremental
  compression or decompression

It will also contain some Zstandard-specific functionality:

* :class:`!ZstdDict` / :func:`!train_dict` / :func:`!finalize_dict` - APIs for
  interacting with Zstandard dictionaries, which are useful for compressing
  many small chunks of similar data

``libzstd`` optional dependency
-------------------------------

The ``libzstd`` library will become an optional dependency of CPython. If the
library is not available, the ``compression.zstd`` module will be unavailable.
This is handled automatically on Unix platforms as part of the normal build
environment detection.

On Windows, ``libzstd`` will be added to
`the source dependencies <https://github.com/python/cpython-source-deps>`_
used to build libraries CPython depends on for Windows.

Other compression modules
-------------------------

New import names ``compression.lzma``, ``compression.bz2``,
``compression.gzip`` and ``compression.zlib`` will be introduced in Python 3.14
re-exporting the contents of the existing ``lzma``, ``bz2``, ``gzip`` and
``zlib`` modules respectively.

The ``_compression`` module, given that it is marked private, will be
immediately renamed to ``compression._common.streams``. The new name was
selected due to the current contents of the module being I/O related helpers
for stream APIs (e.g. ``LZMAFile``) in standard library compression modules.

Compression module migration timeline
-------------------------------------

Existing modules will emit a ``DeprecationWarning`` in the Python
release following the last Python without the ``compression`` module leaving
support. For example, if the ``compression`` namespace is introduced in 3.14,
then the ``DeprecationWarnings`` would be emitted in 3.19, the next release
after 3.13 reaches end of life. These warnings would begin five years after the
introduction of ``compression`` namespace. In accordance with :pep:`387`, in
Python 3.24, five years after the ``DeprecationWarnings`` are added and ten
years after the new ``compression`` namespace is introduced, the existing
modules will be removed and code must use the ``compression`` sub-modules. The
documentation for these modules will be updated to discuss the planned
deprecation and removal timelines.


Backwards Compatibility
=======================

The main compatibility concern is usage of existing standard library
compression APIs with the existing import names. These names will be
deprecated in 3.19 and will be removed in 3.24. Given the long coexistence of
the modules and a 5 year deprecation period, most users will likely migrate to
the new import names well before then. Additionally, a libCST codemod can be
provided to automatically rewrite imports, easing the migration.


Security Implications
=====================

As with any new C code, especially code operating on potentially untrusted user
input, there are risks of memory safety issues. The author plans on
contributing integration with libfuzzer to enable fuzzing the ``_zstd`` code
and ensure it is robust. Furthermore, there are a number of tests that exercise
the compression and decompression routines. These tests pass without error when
compiled with AddressSanitizer.

Taking on a new dependency also always has security risks, but the ``zstd``
library is mature, fuzzed on each commit, and `participates in Meta's bug bounty
program <https://github.com/facebook/zstd/blob/dev/SECURITY.md>`_.


How to Teach This
=================

Documentation for the new module is in the reference implementation branch. The
documentation for other modules will be updated to discuss the deprecation of
their existing import names, and how to migrate.


Reference Implementation
========================

The `reference implementation <https://github.com/emmatyping/cpython/tree/zstd>`_
contains the ``_zstd`` C code, the ``compression.zstd`` code, modifications to
``tarfile``, ``shutil``, and ``zipfile``, and tests for each new API and
integration added. It also contains the re-exports of other compression
modules. Deprecations for the existing import names will be added once a
decision is reached regarding the open issues.


Rejected Ideas
==============

Name the module ``zstdlib`` and do not make a new ``compression`` namespace
---------------------------------------------------------------------------

One option instead of making a new ``compression`` namespace would be to find
a different name, such as ``zstdlib``, as the import name. Several other names,
such as ``zst``, ``libzstd``, and ``zstdcomp`` were proposed as well. In
discussion, the names were found to either be too easy to typo, or unintuitive.
Furthermore, the issue of existing import names is likely to persist for future
compression formats added to the standard library. LZ4, a common high speed
compression format, has `a package on PyPI <https://pypi.org/project/lz4/>`_,
``lz4``, with the import name ``lz4``. Instead of solving this issue for each
compression format, it is better to solve it once and for all by using the
already-claimed ``compression`` namespace.

Introduce an experimental ``_zstd`` package in Python 3.14
----------------------------------------------------------

Since this PEP was published close to the beta cutoff for new features for
Python 3.14, one proposal was to name the package a private module ``_zstd``
so that packaging tools could use it sooner, but not deciding on a name. This
would allow more time for discussion of the final module name during the 3.15
development window. However, introducing a private module was not popular. The
expectations and contract for external usage of a private module in the
standard library are unclear.

Introduce a standard library namespace instead of ``compression``
-----------------------------------------------------------------

One alternative to a ``compression`` namespace would be to introduce a
``std`` namespace for the entire standard library. However, this was seen as
too significant a change for 3.14, with no agreed upon semantics, migration
path, or name for the package. Furthermore, a future PEP introducing a ``std``
namespace could always define that the ``compression`` sub-modules be flattened
into the ``std`` namespace.

Include ``zipfile`` and ``tarfile`` in ``compression``
------------------------------------------------------

Compression is often used with archiving tools, so putting both :mod:`zipfile`
and :mod:`tarfile` under the ``compression`` namespace is appealing. However,
compression can be used beyond just archiving tools. For example, network
requests can be gzip compressed. Furthermore, formats like tar do not include
compression themselves, instead relying on external compression. Therefore,
this PEP does not propose moving :mod:`!zipfile` or :mod:`!tarfile` under
``compression``.

Do not include ``gzip`` under ``compression``
---------------------------------------------

The :rfc:`GZip format RFC <1952>` defines a format which can include multiple
blocks and metadata about its contents. In this way GZip is rather similar to
archive formats like ZIP and tar. Despite that, in usage GZip is often treated
as a compression format rather than an archive format. Looking at how different
languages classify GZip, the prevailing trend is to classify it as a
compression format and not an archiving format.

========== ======================== ==============================================================================
Language   Compression or Archive   Documentation Link
========== ======================== ==============================================================================
Golang     Compression              https://pkg.go.dev/compress/gzip
Ruby       Compression              https://docs.ruby-lang.org/en/master/Zlib/GzipFile.html
Rust       Compression              https://github.com/rust-lang/flate2-rs
Haskell    Compression              https://hackage.haskell.org/package/zlib
C#         Compression              https://learn.microsoft.com/en-us/dotnet/api/system.io.compression.gzipstream
Java       Archive                  https://docs.oracle.com/javase/8/docs/api/java/util/zip/package-summary.html
NodeJS     Compression              https://nodejs.org/api/zlib.html
Web APIs   Compression              https://developer.mozilla.org/en-US/docs/Web/API/Compression_Streams_API
PHP        Compression              https://www.php.net/manual/en/function.gzcompress.php
Perl       Compression              https://perldoc.perl.org/IO::Compress::Gzip
========== ======================== ==============================================================================

In addition, the :mod:`!gzip` module in Python mostly focuses on single block
content and has an API similar to other compression modules, making it a good
fit for the ``compression`` namespace.


Copyright
=========

This document is placed in the public domain or under the
CC0-1.0-Universal license, whichever is more permissive.
````

</details>

<details><summary><b>Step 4 — final</b> (2127 words)</summary>

````text
.. canonical-doc:: :mod:`compression.zstd`


Abstract
========

`Zstandard`_ is a widely adopted, mature, and highly efficient compression
standard. This PEP proposes adding a new module to the Python standard library
containing a Python wrapper around Meta's |zstd| library, the default
implementation. Additionally, to avoid name collisions with packages on PyPI
and to present a unified interface to Python users, compression modules in the
standard library will be moved under a ``compression.*`` package.

.. |zstd| replace:: ``zstd``
.. _zstd: https://facebook.github.io/zstd/
.. _Zstandard: https://facebook.github.io/zstd/


Motivation
==========

CPython has modules for several different compression formats, such as
:mod:`zlib (DEFLATE) <zlib>`, :mod:`gzip <gzip>`, :mod:`bzip2 <bz2>`, and
:mod:`lzma <lzma>`, each widely used. Including popular compression algorithms
matches Python's "batteries included" philosophy of incorporating widely useful
standards and utilities. :mod:`!lzma` is the most recent such module, added in
Python 3.3.

Since then, Zstandard has become the modern *de facto* preferred compression
library for both high performance compression and decompression attaining high
compression ratios at reasonable CPU and memory cost. Zstandard achieves a much
higher compression ratio than bzip2 or zlib (DEFLATE) while decompressing
significantly faster than LZMA.

Zstandard has seen `widespread adoption`_ in many different areas of computing.
The numerous hardware implementations demonstrate long-term commitment to
Zstandard and an expectation that Zstandard will stay the *de facto* choice for
compression for years to come. This is further evidenced by Zstandard's IETF
standardization in :rfc:`8478`. Zstandard compression is also implemented in
both the ZFS_ and Btrfs_ filesystems.

Zstandard's highly efficient compression has supplanted other modern
compression formats, such as brotli_, lzo_, and ucl_ due to its highly
efficient compression. While `LZ4`_ is still used in very high throughput
scenarios, Zstandard can also be used in some of these contexts.
While inclusion of LZ4 is out of scope, it would be a compelling future
addition to the ``compression`` namespace introduced by this PEP.

There are several bindings to Zstandard for Python available on PyPI, each with
different APIs and choices of how to bind the ``zstd`` library. One goal with
introducing an official module in the standard library is to reduce confusion
for Python users who want simple compression/decompression APIs for Zstandard.
The existing packages can continue providing extended APIs or integrate
features from newer Zstandard versions.

Another reason to add Zstandard support to the standard library is to resolve
a long standing open issue (`python/cpython#81276`_) requesting Zstandard
support in the :mod:`tarfile` module. This issue has the 5th most "thumbs up"
of open issues on the CPython tracker, and has garnered a significant amount of
discussion and interest. Additionally, the ZIP format standardizes a
`Zstandard compression format ID`_, and integration with the :mod:`zipfile`
module would allow opening ZIP archives using Zstandard compression. The
reference implementation for this PEP contains integration with the
:mod:`!zipfile`, :mod:`!tarfile`, and :mod:`shutil` modules.

Zstandard compression could also be used to make Python wheel packages smaller
and significantly faster to install. Anaconda found a sizeable speedup when
adopting Zstandard for the conda package format:

.. epigraph::

    Conda's download sizes are reduced ~30-40%, and extraction is dramatically faster.
    [...]
    We see approximately a 2.5x overall speedup, almost all thanks to the dramatically faster extraction speed of the zstd compression used in the new file format.

    -- `Anaconda blog on Zstandard adoption`_

Zstandard has a significantly higher compression ratio compared to wheel's
existing zlib-based compression, `according to lzbench`_, a comprehensive
benchmark of many different compression libraries and formats.
While this PEP does *not* prescribe any changes to the wheel format or other
packaging standards, having Zstandard bindings in the standard library would
enable a future PEP to improve the user experience for Python wheel packages.

.. _widespread adoption: https://facebook.github.io/zstd/#references
.. _ZFS: https://en.wikipedia.org/wiki/ZFS
.. _Btrfs: https://btrfs.readthedocs.io/
.. _brotli: https://brotli.org/
.. _lzo: https://www.oberhumer.com/opensource/lzo/
.. _ucl: https://www.oberhumer.com/opensource/ucl/
.. _LZ4: https://lz4.org/
.. _python/cpython#81276: https://github.com/python/cpython/issues/81276
.. _Zstandard compression format ID: https://pkwaredownloads.blob.core.windows.net/pkware-general/Documentation/APPNOTE-6.3.8.TXT
.. _according to lzbench: https://github.com/inikep/lzbench#benchmarks
.. _Anaconda blog on Zstandard adoption: https://www.anaconda.com/blog/how-we-made-conda-faster-4-7


Rationale
=========

Introduction of a ``compression`` package
-----------------------------------------

Both the ``zstd`` and ``zstandard`` import names are claimed by projects on
PyPI. To avoid breaking users of one of the existing bindings, this PEP
proposes introducing a new namespace for compression libraries,
``compression``. This name is already reserved on PyPI for use in the
standard library. The new Zstandard module will be named ``compression.zstd``.
Other compression modules will be re-exported in the new ``compression`` package.

Providing a common namespace for compression modules has several advantages.
First, it reduces user confusion about where to find compression modules.
Second, the top level ``compression`` module could provide information on which
compression formats are available, similar to ``hashlib``'s
``algorithms_available``. If :pep:`775` is accepted, a
``compression.algorithms_guaranteed`` could be provided as well, listing
``zlib``. Finally, a ``compression`` namespace prevents future issues with
merging other compression formats into the standard library. New compression
formats will likely be published to PyPI prior to integration into
CPython. Therefore, any new compression format import name will likely already
be claimed by the time a module would be considered for inclusion in CPython.
Putting compression modules under a package prefix prevents issues with
potential future name clashes.

Code that would like to remain compatible across Python versions may use the
following pattern to ensure compatibility::

  try:
      from compression.lzma import LZMAFile
  except ImportError:
      from lzma import LZMAFile

This will use the newer import name when available and fall back to the old
name otherwise.

Implementation based on ``pyzstd``
----------------------------------

The implementation for this PEP is based on the `pyzstd project`_.
This project was chosen as the code was `originally written to be upstreamed`_
to CPython by Ma Lin, who also wrote the `output buffer implementation`_ used in
the standard library today.
The project has since been taken over by Rogdham and is published to PyPI. The
APIs in ``pyzstd`` are similar to the APIs for other compression modules in the
standard library such as :mod:`!bz2` and :mod:`!lzma`.

.. _pyzstd project: https://github.com/Rogdham/pyzstd
.. _originally written to be upstreamed: https://github.com/python/cpython/issues/81276#issuecomment-1093824963
.. _output buffer implementation: https://github.com/python/cpython/commit/f9bedb630e8a0b7d94e1c7e609b20dfaa2b22231

Minimum supported Zstandard version
-----------------------------------

The minimum supported Zstandard was chosen as v1.4.5, released in May of 2020.
This version was chosen as a minimum based on reviewing the versions of
Zstandard available in a number of Linux distribution package repositories,
including LTS releases. This version choice is rather conservative to maximize
compatibility with existing LTS Linux distributions, but a newer Zstandard
version could likely be chosen given that newer Python releases are generally
packaged as part of newer distribution releases.


Specification
=============

The ``compression`` namespace
-----------------------------

A new namespace for compression modules will be introduced named
``compression``. The top-level module for this package will be empty to begin
with, but a standard API for interacting with compression routines may be
added in the future to the toplevel.

The ``compression.zstd`` module
-------------------------------

A new module, ``compression.zstd`` will be introduced with Zstandard
compression APIs that match other compression modules in the standard library,
namely

* :func:`!compress` / :func:`!decompress` - APIs for one-shot compression
  or decompression
* :class:`!ZstdFile` / :func:`!open` - APIs for interacting with streams
  and file-like objects
* :class:`!ZstdCompressor` / :class:`!ZstdDecompressor` - APIs for incremental
  compression or decompression

It will also contain some Zstandard-specific functionality:

* :class:`!ZstdDict` / :func:`!train_dict` / :func:`!finalize_dict` - APIs for
  interacting with Zstandard dictionaries, which are useful for compressing
  many small chunks of similar data

``libzstd`` optional dependency
-------------------------------

The ``libzstd`` library will become an optional dependency of CPython. If the
library is not available, the ``compression.zstd`` module will be unavailable.
This is handled automatically on Unix platforms as part of the normal build
environment detection.

On Windows, ``libzstd`` will be added to
`the source dependencies <https://github.com/python/cpython-source-deps>`_
used to build libraries CPython depends on for Windows.

Other compression modules
-------------------------

New import names ``compression.lzma``, ``compression.bz2``,
``compression.gzip`` and ``compression.zlib`` will be introduced in Python 3.14
re-exporting the contents of the existing ``lzma``, ``bz2``, ``gzip`` and
``zlib`` modules respectively. The ``compression`` sub-modules will become
the canonical import names going forward. The use of the new compression names
will be promoted over the original top level module names in the Python
documentation when the minimum supported Python version requirements make
that feasible.

The ``_compression`` module, given that it is marked private, will be
immediately renamed to ``compression._common._streams``. The new name was
selected due to the current contents of the module being I/O related helpers
for stream APIs (e.g. ``LZMAFile``) in standard library compression modules.


Backwards Compatibility
=======================

This PEP introduces no backwards incompatible changes. There are currently no
plans to deprecate or remove the existing compression modules. Any deprecation
or removal of the existing modules is left to a future decision but will occur
no sooner than 5 years from the acceptance of this PEP.


Security Implications
=====================

As with any new C code, especially code operating on potentially untrusted user
input, there are risks of memory safety issues. The author plans on
contributing integration with libfuzzer to enable fuzzing the ``_zstd`` code
and ensure it is robust. Furthermore, there are a number of tests that exercise
the compression and decompression routines. These tests pass without error when
compiled with AddressSanitizer.

Taking on a new dependency also always has security risks, but the ``zstd``
library is mature, fuzzed on each commit, and `participates in Meta's bug bounty
program <https://github.com/facebook/zstd/blob/dev/SECURITY.md>`_.


How to Teach This
=================

Documentation for the new module is in the reference implementation branch. The
documentation for existing modules will be updated to reference the new names
as well.


Reference Implementation
========================

The `reference implementation <https://github.com/emmatyping/cpython/tree/zstd>`_
contains the ``_zstd`` C code, the ``compression.zstd`` code, modifications to
``tarfile``, ``shutil``, and ``zipfile``, and tests for each new API and
integration added. It also contains the re-exports of other compression
modules.


Rejected Ideas
==============

Name the module ``zstdlib`` and do not make a new ``compression`` namespace
---------------------------------------------------------------------------

One option instead of making a new ``compression`` namespace would be to find
a different name, such as ``zstdlib``, as the import name. Several other names,
such as ``zst``, ``libzstd``, and ``zstdcomp`` were proposed as well. In
discussion, the names were found to either be too easy to typo, or unintuitive.
Furthermore, the issue of existing import names is likely to persist for future
compression formats added to the standard library. LZ4, a common high speed
compression format, has `a package on PyPI <https://pypi.org/project/lz4/>`_,
``lz4``, with the import name ``lz4``. Instead of solving this issue for each
compression format, it is better to solve it once and for all by using the
already-claimed ``compression`` namespace.

Introduce an experimental ``_zstd`` package in Python 3.14
----------------------------------------------------------

Since this PEP was published close to the beta cutoff for new features for
Python 3.14, one proposal was to name the package a private module ``_zstd``
so that packaging tools could use it sooner, but not deciding on a name. This
would allow more time for discussion of the final module name during the 3.15
development window. However, introducing a private module was not popular. The
expectations and contract for external usage of a private module in the
standard library are unclear.

Introduce a standard library namespace instead of ``compression``
-----------------------------------------------------------------

One alternative to a ``compression`` namespace would be to introduce a
``std`` namespace for the entire standard library. However, this was seen as
too significant a change for 3.14, with no agreed upon semantics, migration
path, or name for the package. Furthermore, a future PEP introducing a ``std``
namespace could always define that the ``compression`` sub-modules be flattened
into the ``std`` namespace.

Include ``zipfile`` and ``tarfile`` in ``compression``
------------------------------------------------------

Compression is often used with archiving tools, so putting both :mod:`zipfile`
and :mod:`tarfile` under the ``compression`` namespace is appealing. However,
compression can be used beyond just archiving tools. For example, network
requests can be gzip compressed. Furthermore, formats like tar do not include
compression themselves, instead relying on external compression. Therefore,
this PEP does not propose moving :mod:`!zipfile` or :mod:`!tarfile` under
``compression``.

Do not include ``gzip`` under ``compression``
---------------------------------------------

The :rfc:`GZip format RFC <1952>` defines a format which can include multiple
blocks and metadata about its contents. In this way GZip is rather similar to
archive formats like ZIP and tar. Despite that, in usage GZip is often treated
as a compression format rather than an archive format. Looking at how different
languages classify GZip, the prevailing trend is to classify it as a
compression format and not an archiving format.

========== ======================== ==============================================================================
Language   Compression or Archive   Documentation Link
========== ======================== ==============================================================================
Golang     Compression              https://pkg.go.dev/compress/gzip
Ruby       Compression              https://docs.ruby-lang.org/en/master/Zlib/GzipFile.html
Rust       Compression              https://github.com/rust-lang/flate2-rs
Haskell    Compression              https://hackage.haskell.org/package/zlib
C#         Compression              https://learn.microsoft.com/en-us/dotnet/api/system.io.compression.gzipstream
Java       Archive                  https://docs.oracle.com/javase/8/docs/api/java/util/zip/package-summary.html
NodeJS     Compression              https://nodejs.org/api/zlib.html
Web APIs   Compression              https://developer.mozilla.org/en-US/docs/Web/API/Compression_Streams_API
PHP        Compression              https://www.php.net/manual/en/function.gzcompress.php
Perl       Compression              https://perldoc.perl.org/IO::Compress::Gzip
========== ======================== ==============================================================================

In addition, the :mod:`!gzip` module in Python mostly focuses on single block
content and has an API similar to other compression modules, making it a good
fit for the ``compression`` namespace.


Copyright
=========

This document is placed in the public domain or under the
CC0-1.0-Universal license, whichever is more permissive.
````

</details>
