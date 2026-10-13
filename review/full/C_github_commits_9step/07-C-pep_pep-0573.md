# 7. Python PEP: Module State Access from C Extension Methods

`C-pep_pep-0573` · [full/C_github_commits_9step](README.md)

Source: <https://github.com/python/peps/blob/545c670f1e986162eb7161d63c944108e504bd09/peps/pep-0573.rst> · License: Public domain / CC0-1.0 (PEP text) · 26 commits touching the file; 14 distinct versions

| step | name | words | citations | similarity to final | provenance |
|---|---|---|---|---|---|
| 0 | title | 7 | 0 | 0.00 | source_title |
| 1 | revision_1 | 2518 | 0 | 0.62 | commit 65aa281f0c (2018-03-27) |
| 2 | revision_2 | 2807 | 0 | 0.64 | commit cfb7bd74db (2019-07-03) |
| 3 | revision_3 | 2339 | 0 | 0.80 | commit b4495fd347 (2019-09-12) |
| 4 | revision_4 | 2238 | 0 | 0.82 | commit 01ee996ad2 (2019-09-13) |
| 5 | revision_5 | 2274 | 0 | 0.83 | commit 34343da45d (2020-01-03) |
| 6 | revision_6 | 2344 | 0 | 0.99 | commit 2758332c1e (2020-01-16) |
| 7 | revision_7 | 2332 | 0 | 1.00 | commit 113e490701 (2022-01-21) |
| 8 | final | 2315 | 0 | 1.00 | commit b199a29c8a (2023-07-31) |

<details><summary><b>Step 0 — title</b> (7 words)</summary>

````text
Module State Access from C Extension Methods
````

</details>

<details><summary><b>Step 1 — revision_1</b> (2518 words)</summary>

````text
Abstract
========

This PEP proposes to add a way for CPython extension methods to access context such as
the state of the modules they are defined in.

This will allow extension methods to use direct pointer dereferences
rather than PyState_FindModule for looking up module state, reducing or eliminating the
performance cost of using module-scoped state over process global state.

This fixes one of the remaining roadblocks for adoption of PEP 3121 (Extension
module initialization and finalization) and PEP 489
(Multi-phase extension module initialization).

Additionaly, support for easier creation of immutable exception classes is added.
This removes the need for keeping per-module state if it would only be used
for exception classes.

While this PEP takes an additional step towards fully solving the problems that PEP 3121 and PEP 489 started
tackling, it does not attempt to resolve *all* remaining concerns. In particular, accessing the module state from slot methods (``nb_add``, etc) remains slower than accessing that state from other extension methods.


Terminology
===========

Process-Global State
--------------------

C-level static variables. Since this is very low-level
memory storage, it must be managed carefully.

(XXX Use this term everywhere)

Per-module State
----------------

State local to a module object, allocated dynamically as part of a
module object's initialization. This isolates the state from other
instances of the module (including those in other subinterpreters).

Accessed by ``PyModule_GetState()``.


Static Type
-----------

A type object defined as a C-level static variable, i.e. a compiled-in type object.

A static type needs to be shared between module instances and has no
information of what module it belongs to.
Static types do not have ``__dict__`` (although their instances might).

Heap Type
---------

A type object created at run time.


Rationale
=========

PEP 489 introduced a new way to initialize extension modules, which brings
several advantages to extensions that implement it:

    * The extension modules behave more like their Python counterparts.
    * The extension modules can easily support loading into pre-existing
      module objects, which paves the way for extension module support for
      ``runpy`` or for systems that enable extension module reloading.
    * Loading multiple modules from the same extension is possible, which
      makes testing module isolation (a key feature for proper sub-interpreter
      support) possible from a single interpreter.

The biggest hurdle for adoption of PEP 489 is allowing access to module state
from methods of extension types.
Currently, the way to access this state from extension methods is by looking up the module via
``PyState_FindModule`` (in contrast to module level functions in extension modules, which
receive a module reference as an argument).
However, ``PyState_FindModule`` queries the thread-local state, making it relatively
costly compared to C level process global access and consequently deterring module authors from using it.

Also, ``PyState_FindModule`` relies on the assumption that in each
subinterpreter, there is at most one module corresponding to
a given ``PyModuleDef``.  This does not align well with Python's import
machinery.  Since PEP 489 aimed to fix that,  the assumption does
not hold for modules that use multi-phase initialization, so
``PyState_FindModule`` is unavailable for these modules.

A faster, safer way of accessing module-level state from extension methods
is needed.


Immutable Exception Types
-------------------------

For isolated modules to work, any class whose methods touch module state
must be a heap type, so that each instance of a module can have its own
type object.  With the changes proposed in this PEP, heap type instances will
have access to module state without global registration.  But, to create
instances of heap types, one will need the module state in order to
get the type object corresponding to the appropriate module.
In short, heap types are "viral" – anything that “touches” them must itself be
a heap type.

Curently, most exception types, apart from the ones in ``builtins``, are
heap types.  This is likely simply because there is a convenient way
to create them: ``PyErr_NewException``. 
Heap types generally have a mutable ``__dict__``.
In most cases, this mutability is harmful.  For example, exception types
from the ``sqlite`` module are mutable and shared across subinterpreters.
This allows "smuggling" values to other subinterpreters via attributes of
``sqlite3.Error``.

Moreover, since raising exceptions is a common operation, and heap types
will be "viral", ``PyErr_NewException`` will tend to "infect" the module
with "heap-type-ness" – at least if the module decides play well with
subinterpreters/isolation.
Many modules could go without module state
entirely if the exception classes were immutable.

To solve this problem, a new function for creating immutable exception types
is proposed.


Background
===========

The implementation of a Python method may need access to one or more of
the following pieces of information:

   * The instance it is called on (``self``)
   * The underlying function
   * The class the method was defined in
   * The corresponding module
   * The module state

In Python code, the Python-level equivalents may be retrieved as::

    import sys

    class Foo:
        def meth(self):
            instance = self
            module_globals = globals()
            module_object = sys.modules[__name__]
            underlying_function = Foo.meth
            defining_class = Foo

.. note::

    The defining class is not ``type(self)``, since ``type(self)`` might
    be a subclass of ``Foo``.

Implicitly, the last three of those rely on name-based lookup via the function's ``__globals__``:
either the ``Foo`` attribute to access the defining class and Python function object, or ``__name__`` to find the module object in ``sys.modules``.
In Python code, this is feasible, as ``__globals__`` is set appropriately when the function definition is executed, and
even if the namespace has been manipulated to return a different object, at worst an exception will be raised.

By contrast, extension methods are typically implemented as normal C functions.
This means that they only have access to their arguments and C level thread-local
and process-global states. Traditionally, many extension modules have stored
their shared state in C-level process globals, causing problems when:
    
    * running multiple initialize/finalize cycles in the same process
    * reloading modules (e.g. to test conditional imports)
    * loading extension modules in subinterpreters

PEP 3121 attempted to resolve this by offering the ``PyState_FindModule`` API, but this still has significant problems when it comes to extension methods (rather than module level functions):

    * it is markedly slower than directly accessing C-level process-global state
    * there is still some inherent reliance on process global state that means it still doesn't reliably handle module reloading

It's also the case that when looking up a C-level struct such as module state, supplying
an unexpected object layout can crash the interpreter, so it's significantly more important to ensure that extension
methods receive the kind of object they expect.

Proposal
========

Currently, a bound extension method (``PyCFunction`` or ``PyCFunctionWithKeywords``) receives only
``self``, and (if applicable) the supplied positional and keyword arguments. 

While module-level extension functions already receive access to the defining module object via their
``self`` argument, methods of extension types don't have that luxury: they receive the bound instance
via ``self``, and hence have no direct access to the defining class or the module level state.

The additional module level context described above can be made available with two changes.
Both additions are optional; extension authors need to opt in to start
using them:

    * Add a pointer to the module to heap type objects.

    * Pass the defining class to the underlying C function.

      The defining class is readily available at the time built-in
      method object (``PyCFunctionObject``) is created, so it can be stored
      in a new struct that extends ``PyCFunctionObject``.

The module state can then be retrieved from the module object via
``PyModule_GetState``.

Note that this proposal implies that any type whose method needs to access
per-module state must be a heap type, rather than a static type.

This is necessary to support loading multiple module objects from a single
extension: a static type, as a C-level global, has no information about
which module it belongs to.


Slot methods
------------

The above changes don't cover slot methods, such as ``tp_iter`` or ``nb_add``.

The problem with slot methods is that their C API is fixed, so we can't
simply add a new argument to pass in the defining class.
Two possible solutions have been proposed to this problem:

    * Look up the class through walking the MRO.
      This is potentially expensive, but will be useful if performance is not
      a problem (such as when raising a module-level exception).
    * Storing a pointer to the defining class of each slot in a separate table,
      ``__typeslots__`` [#typeslots-mail]_.  This is technically feasible and fast,
      but quite invasive.

Due to the invasiveness of the latter approach, this PEP proposes adding a MRO walking helper for use in slot method implementations, deferring the more complex alternative as a potential future optimisation.


Immutable Exception Types
-------------------------

To faciliate creating static exception classes, a new function is proposed:
``PyErr_PrepareImmutableException``. It will work similarly to ``PyErr_NewExceptionWithDoc``
but will take a ``PyTypeObject **`` pointer, which points to a ``PyTypeObject *`` that is
either ``NULL`` or an initialized ``PyTypeObject``.
This pointer may be declared in process-global state. The function will then
allocate the object and will keep in mind that already existing exception
should not be overwritten.

(XXX: Update function name in the implementation)

The extra indirection makes it possible to make ``PyErr_PrepareImmutableException``
part of the stable ABI by having the Python interpreter, rather than extension code,
allocate the ``PyTypeObject``.


Specification
=============

Adding module references to heap types
--------------------------------------

The ``PyHeapTypeObject`` struct will get a new member, ``PyObject *ht_module``,
that can store a pointer to the module object for which the type was defined.
It will be ``NULL`` by default, and should not be modified after the type
object is created.

A new factory method will be added for creating modules::

    PyObject* PyType_FromModuleAndSpec(PyObject *module,
                                       PyType_Spec *spec,
                                       PyObject *bases)

This acts the same as ``PyType_FromSpecWithBases``, and additionally sets
``ht_module`` to the provided module object.

Additionally, an accessor, ``PyObject * PyType_GetModule(PyTypeObject *)``
will be provided.
It will return the ``ht_module`` if a heap type with module pointer set
is passed in, otherwise it will set a SystemError and return NULL.

Usually, creating a class with ``ht_module`` set will create a reference
cycle involving the class and the module.
This is not a problem, as tearing down modules is not a performance-sensitive
operation (and module-level functions typically also create reference cycles).
The existing "set all module globals to None" code that breaks function cycles
through ``f_globals`` will also break the new cycles through ``ht_module``.


Passing the defining class to extension methods
-----------------------------------------------

A new style of C-level functions will be added to the current selection of
``PyCFunction`` and ``PyCFunctionWithKeywords``::

    PyObject *PyCMethod(PyObject *self,
                        PyTypeObject *defining_class,
                        PyObject *args, PyObject *kwargs)

A new method object flag, ``METH_METHOD``, will be added to signal that
the underlying C function is ``PyCMethod``.

To hold the extra information, a new structure extending ``PyCFunctionObject``
will be added::

    typedef struct {
        PyCFunctionObject func;
        PyTypeObject *mm_class; /* Passed as 'defining_class' arg to the C func */
    } PyCMethodObject;

Method construction and calling code and will be updated to honor
``METH_METHOD``.


Argument Clinic
---------------

To support passing the defining class to methods using Argument Clinic,
a new converter will be added to clinic.py: ``defining_class``.

Each method may only have one argument using this converter, and it must
appear after ``self``, or, if ``self`` is not used, as the first argument.
The argument will be of type ``PyTypeObject *``.

When used, Argument Clinic will select ``METH_METHOD`` as the calling
convention.
The argument will not appear in ``__text_signature__``.

This will be compatible with ``__init__`` and ``__new__`` methods, where an
MRO walker will be used to pass the defining class from clinic generated
code to the user's function.


Slot methods
------------

To allow access to per-module state from slot methods, an MRO walker
will be implemented::

    PyTypeObject *PyType_DefiningTypeFromSlotFunc(PyTypeObject *type,
                                                  int slot, void *func)

The walker will go through bases of heap-allocated ``type``
and search for class that defines ``func`` at its ``slot``.

The ``func`` needs not to be inherited by ``type``, only requirement
for the walker to find the defining class is that the defining class
must be heap-allocated.

On failure, exception is set and NULL is returned.


Static exceptions
-----------------

A new function will be added::

    int PyErr_PrepareImmutableException(PyTypeObject **exc,
                                     const char *name,
                                     const char *doc,
                                     PyObject *base)

Creates an immutable exception type which can be shared
across multiple module objects.
If the type already exists (determined by a process-global pointer,
``*exc``), skip the initialization and only ``INCREF`` it.

If ``*exc`` is NULL, the function will
allocate a new exception type and initialize it using given parameters
the same way ``PyType_FromSpecAndBases`` would.
The ``doc`` and ``base`` arguments may be ``NULL``, defaulting to a
missing docstring and ``PyExc_Exception`` base class, respectively.
The exception type's ``tp_flags`` will be set to values common to
built-in exceptions and the ``Py_TPFLAGS_HEAP_IMMUTABLE`` flag (see below)
will be set.
On failure, ``PyErr_PrepareImmutableException`` will set an exception
and return -1.

If called with an initialized exception type (``*exc``
is non-NULL), the function will do nothing but incref ``*exc``.

(XXX: Support and test multiple inheritance)

A new flag, ``Py_TPFLAGS_HEAP_IMMUTABLE``, will be added to prevent
mutation of the type object. This makes it possible to
share the object safely between multiple interpreters.
This flag is checked in setattr (XXX: name of C function?) and blocks
setting of attributes when set, similar to built-in types.

A new pointer, ``ht_moduleptr``, will be added to heap types to store ``exc``.

(XXX: better name? Update implementation)

On deinitialization of the exception type, ``*exc`` will be set to ``NULL``.
This makes it safe for
``PyErr_PrepareImmutableException`` to check if the exception
was already initialized.


Helpers
-------

XXX: I'd like to port a bunch of modules to see what helpers would be convenient

XXX: Helper for getting module state directly from defining class


Modules Converted in the Initial Implementation
-----------------------------------------------

To validate the approach, several modules will be modified during
the initial implementation:

The ``zipimport``, ``_io``, ``_elementtree``, and ``_csv`` modules
will be ported to PEP 489 multiphase initialization.


Summary of API Changes and Additions
====================================

XXX, see above for now


Backwards Compatibility
=======================

Two new pointers are added to all heap types.
All other changes are adding new functions, structures and a type flag.

The new ``PyErr_PrepareImmutableException`` function changes encourages
modules to switch from using heap-type Exception classes to static ones,
and a number of modules will be switched in the initial implementation.
This change will prevent adding class attributes to such types.
For example, the following will raise AttributeError::

    sqlite.OperationalError.foo = None

Instances and subclasses of such exceptions will not be affected.

Implementation
==============

An initial implementation is available in a Github repository [#gh-repo]_;
a patchset is at [#gh-patch]_.


Possible Future Extensions
==========================

Easy creation of types with module references
---------------------------------------------

It would be possible to add a PEP 489 execution slot type to make
creating heap types significantly easier than calling
``PyType_FromModuleAndSpec``.
This is left to a future PEP.


Optimization
------------

CPython optimizes calls to methods that have restricted signatures,
such as not allowing keyword arguments.

As proposed here, methods defined with the ``METH_METHOD`` flag do not support
these optimizations.


References
==========

.. [#typeslots-mail] [Import-SIG] On singleton modules, heap types, and subinterpreters
   (https://mail.python.org/pipermail/import-sig/2015-July/001035.html)

.. [#gh-repo]
   https://github.com/Traceur759/cpython/commits/pep-c

.. [#gh-patch]
   https://github.com/Traceur759/cpython/compare/master...Traceur759:pep-c.patch


Copyright
=========

This document has been placed in the public domain.



..
   Local Variables:
   mode: indented-text
   indent-tabs-mode: nil
   sentence-end-double-space: t
   fill-column: 70
   coding: utf-8
   End:
````

</details>

<details><summary><b>Step 2 — revision_2</b> (2807 words)</summary>

````text
Abstract
========

This PEP proposes to add a way for CPython extension methods to access context such as
the state of the modules they are defined in.

This will allow extension methods to use direct pointer dereferences
rather than PyState_FindModule for looking up module state, reducing or eliminating the
performance cost of using module-scoped state over process global state.

This fixes one of the remaining roadblocks for adoption of PEP 3121 (Extension
module initialization and finalization) and PEP 489
(Multi-phase extension module initialization).

Additionally, support for easier creation of immutable exception classes is added.
This removes the need for keeping per-module state if it would only be used
for exception classes.

While this PEP takes an additional step towards fully solving the problems that PEP 3121 and PEP 489 started
tackling, it does not attempt to resolve *all* remaining concerns. In particular, accessing the module state from slot methods (``nb_add``, etc) remains slower than accessing that state from other extension methods.


Terminology
===========

Process-Global State
--------------------

C-level static variables. Since this is very low-level
memory storage, it must be managed carefully.

Per-module State
----------------

State local to a module object, allocated dynamically as part of a
module object's initialization. This isolates the state from other
instances of the module (including those in other subinterpreters).

Accessed by ``PyModule_GetState()``.


Static Type
-----------

A type object defined as a C-level static variable, i.e. a compiled-in type object.

A static type needs to be shared between module instances and has no
information of what module it belongs to.
Static types do not have ``__dict__`` (although their instances might).

Heap Type
---------

A type object created at run time.


Rationale
=========

PEP 489 introduced a new way to initialize extension modules, which brings
several advantages to extensions that implement it:

    * The extension modules behave more like their Python counterparts.
    * The extension modules can easily support loading into pre-existing
      module objects, which paves the way for extension module support for
      ``runpy`` or for systems that enable extension module reloading.
    * Loading multiple modules from the same extension is possible, which
      makes testing module isolation (a key feature for proper sub-interpreter
      support) possible from a single interpreter.

The biggest hurdle for adoption of PEP 489 is allowing access to module state
from methods of extension types.
Currently, the way to access this state from extension methods is by looking up the module via
``PyState_FindModule`` (in contrast to module level functions in extension modules, which
receive a module reference as an argument).
However, ``PyState_FindModule`` queries the thread-local state, making it relatively
costly compared to C level process global access and consequently deterring module authors from using it.

Also, ``PyState_FindModule`` relies on the assumption that in each
subinterpreter, there is at most one module corresponding to
a given ``PyModuleDef``.  This does not align well with Python's import
machinery.  Since PEP 489 aimed to fix that,  the assumption does
not hold for modules that use multi-phase initialization, so
``PyState_FindModule`` is unavailable for these modules.

A faster, safer way of accessing module-level state from extension methods
is needed.


Immutable Exception Types
-------------------------

For isolated modules to work, any class whose methods touch module state
must be a heap type, so that each instance of a module can have its own
type object.  With the changes proposed in this PEP, heap type instances will
have access to module state without global registration.  But, to create
instances of heap types, one will need the module state in order to
get the type object corresponding to the appropriate module.
In short, heap types are "viral" – anything that “touches” them must itself be
a heap type.

Currently, most exception types, apart from the ones in ``builtins``, are
heap types.  This is likely simply because there is a convenient way
to create them: ``PyErr_NewException``.
Heap types generally have a mutable ``__dict__``.
In most cases, this mutability is harmful.  For example, exception types
from the ``sqlite`` module are mutable and shared across subinterpreters.
This allows "smuggling" values to other subinterpreters via attributes of
``sqlite3.Error``.

Moreover, since raising exceptions is a common operation, and heap types
will be "viral", ``PyErr_NewException`` will tend to "infect" the module
with "heap type-ness" – at least if the module decides play well with
subinterpreters/isolation.
Many modules could go without module state
entirely if the exception classes were immutable.

To solve this problem, a new function for creating immutable exception types
is proposed.


Background
===========

The implementation of a Python method may need access to one or more of
the following pieces of information:

   * The instance it is called on (``self``)
   * The underlying function
   * The class the method was defined in
   * The corresponding module
   * The module state

In Python code, the Python-level equivalents may be retrieved as::

    import sys

        def meth(self):
            instance = self
            module_globals = globals()
            module_object = sys.modules[__name__]  # (1)
            underlying_function = Foo.meth         # (1)
            defining_class = Foo                   # (1)
            defining_class = __class__             # (2)

.. note::

    The defining class is not ``type(self)``, since ``type(self)`` might
    be a subclass of ``Foo``.

The statements marked (1) implicitly rely on name-based lookup via the function's ``__globals__``:
either the ``Foo`` attribute to access the defining class and Python function object, or ``__name__`` to find the module object in ``sys.modules``.
In Python code, this is feasible, as ``__globals__`` is set appropriately when the function definition is executed, and
even if the namespace has been manipulated to return a different object, at worst an exception will be raised.

The ``__class__`` closure, (2), is a safer way to get the defining class, but it still relies on ``__closure__`` being set appropriately.

By contrast, extension methods are typically implemented as normal C functions.
This means that they only have access to their arguments and C level thread-local
and process-global states. Traditionally, many extension modules have stored
their shared state in C-level process globals, causing problems when:

    * running multiple initialize/finalize cycles in the same process
    * reloading modules (e.g. to test conditional imports)
    * loading extension modules in subinterpreters

PEP 3121 attempted to resolve this by offering the ``PyState_FindModule`` API, but this still has significant problems when it comes to extension methods (rather than module level functions):

    * it is markedly slower than directly accessing C-level process-global state
    * there is still some inherent reliance on process global state that means it still doesn't reliably handle module reloading

It's also the case that when looking up a C-level struct such as module state, supplying
an unexpected object layout can crash the interpreter, so it's significantly more important to ensure that extension
methods receive the kind of object they expect.

Proposal
========

Currently, a bound extension method (``PyCFunction`` or ``PyCFunctionWithKeywords``) receives only
``self``, and (if applicable) the supplied positional and keyword arguments.

While module-level extension functions already receive access to the defining module object via their
``self`` argument, methods of extension types don't have that luxury: they receive the bound instance
via ``self``, and hence have no direct access to the defining class or the module level state.

The additional module level context described above can be made available with two changes.
Both additions are optional; extension authors need to opt in to start
using them:

    * Add a pointer to the module to heap type objects.

    * Pass the defining class to the underlying C function.

      The defining class is readily available at the time built-in
      method object (``PyCFunctionObject``) is created, so it can be stored
      in a new struct that extends ``PyCFunctionObject``.

The module state can then be retrieved from the module object via
``PyModule_GetState``.

Note that this proposal implies that any type whose method needs to access
per-module state must be a heap type, rather than a static type.

This is necessary to support loading multiple module objects from a single
extension: a static type, as a C-level global, has no information about
which module it belongs to.


Slot methods
------------

The above changes don't cover slot methods, such as ``tp_iter`` or ``nb_add``.

The problem with slot methods is that their C API is fixed, so we can't
simply add a new argument to pass in the defining class.
Two possible solutions have been proposed to this problem:

    * Look up the class through walking the MRO.
      This is potentially expensive, but will be useful if performance is not
      a problem (such as when raising a module-level exception).
    * Storing a pointer to the defining class of each slot in a separate table,
      ``__typeslots__`` [#typeslots-mail]_.  This is technically feasible and fast,
      but quite invasive.

Due to the invasiveness of the latter approach, this PEP proposes adding an MRO walking
helper for use in slot method implementations, deferring the more complex alternative
as a potential future optimisation. Modules affected by this concern also have the
option of using thread-local state or PEP 567 context variables, or else defining their
own reload-friendly lookup caching scheme.


Immutable Exception Types
-------------------------

To facilitate creating static exception classes, a new function is proposed:
``PyErr_PrepareImmutableException``. It will work similarly to ``PyErr_NewExceptionWithDoc``
but will take a ``PyTypeObject **`` pointer, which points to a ``PyTypeObject *`` that is
either ``NULL`` or an initialized ``PyTypeObject``.
This pointer may be declared in process-global state. The function will then
allocate the object and will keep in mind that already existing exception
should not be overwritten.

The extra indirection makes it possible to make ``PyErr_PrepareImmutableException``
part of the stable ABI by having the Python interpreter, rather than extension code,
allocate the ``PyTypeObject``.


Specification
=============

Adding module references to heap types
--------------------------------------

The ``PyHeapTypeObject`` struct will get a new member, ``PyObject *ht_module``,
that can store a pointer to the module object for which the type was defined.
It will be ``NULL`` by default, and should not be modified after the type
object is created.

A new factory method will be added for creating modules::

    PyObject* PyType_FromModuleAndSpec(PyObject *module,
                                       PyType_Spec *spec,
                                       PyObject *bases)

This acts the same as ``PyType_FromSpecWithBases``, and additionally sets
``ht_module`` to the provided module object.

Additionally, an accessor, ``PyObject * PyType_GetModule(PyTypeObject *)``
will be provided.
It will return the ``ht_module`` if a heap type with module pointer set
is passed in, otherwise it will set a SystemError and return NULL.

Usually, creating a class with ``ht_module`` set will create a reference
cycle involving the class and the module.
This is not a problem, as tearing down modules is not a performance-sensitive
operation (and module-level functions typically also create reference cycles).
The existing "set all module globals to None" code that breaks function cycles
through ``f_globals`` will also break the new cycles through ``ht_module``.


Passing the defining class to extension methods
-----------------------------------------------

A new style of C-level functions will be added to the current selection of
``PyCFunction`` and ``PyCFunctionWithKeywords``::

    PyObject *PyCMethod(PyObject *self,
                        PyTypeObject *defining_class,
                        PyObject *args, PyObject *kwargs)

A new method object flag, ``METH_METHOD``, will be added to signal that
the underlying C function is ``PyCMethod``.

To hold the extra information, a new structure extending ``PyCFunctionObject``
will be added::

    typedef struct {
        PyCFunctionObject func;
        PyTypeObject *mm_class; /* Passed as 'defining_class' arg to the C func */
    } PyCMethodObject;

To allow passing the defining class to the underlying C function, a change
to private API is required, now ``_PyMethodDef_RawFastCallDict`` and
``_PyMethodDef_RawFastCallKeywords`` will receive ``PyTypeObject *cls``
as one of their arguments.

A new macro ``PyCFunction_GET_CLASS(cls)`` will be added for easier access to mm_class.

Method construction and calling code and will be updated to honor
``METH_METHOD``.


Argument Clinic
---------------

To support passing the defining class to methods using Argument Clinic,
a new converter will be added to clinic.py: ``defining_class``.

Each method may only have one argument using this converter, and it must
appear after ``self``, or, if ``self`` is not used, as the first argument.
The argument will be of type ``PyTypeObject *``.

When used, Argument Clinic will select ``METH_METHOD`` as the calling
convention.
The argument will not appear in ``__text_signature__``.

This will be compatible with ``__init__`` and ``__new__`` methods, where an
MRO walker will be used to pass the defining class from clinic generated
code to the user's function.


Slot methods
------------

To allow access to per-module state from slot methods, an MRO walker
will be implemented::

    PyTypeObject *PyType_DefiningTypeFromSlotFunc(PyTypeObject *type,
                                                  int slot, void *func)

The walker will go through bases of heap-allocated ``type``
and search for class that defines ``func`` at its ``slot``.

The ``func`` needs not to be inherited by ``type``, only requirement
for the walker to find the defining class is that the defining class
must be heap-allocated.

On failure, exception is set and NULL is returned.


Static exceptions
-----------------

A new function will be added::

    int PyErr_PrepareImmutableException(PyTypeObject **exc,
                                     const char *name,
                                     const char *doc,
                                     PyObject *base)

Creates an immutable exception type which can be shared
across multiple module objects.
If the type already exists (determined by a process-global pointer,
``*exc``), skip the initialization and only ``INCREF`` it.

If ``*exc`` is NULL, the function will
allocate a new exception type and initialize it using given parameters
the same way ``PyType_FromSpecAndBases`` would.
The ``doc`` and ``base`` arguments may be ``NULL``, defaulting to a
missing docstring and ``PyExc_Exception`` base class, respectively.
The exception type's ``tp_flags`` will be set to values common to
built-in exceptions and the ``Py_TPFLAGS_HEAP_IMMUTABLE`` flag (see below)
will be set.
On failure, ``PyErr_PrepareImmutableException`` will set an exception
and return -1.

If called with an initialized exception type (``*exc``
is non-NULL), the function will do nothing but incref ``*exc``.

A new flag, ``Py_TPFLAGS_HEAP_IMMUTABLE``, will be added to prevent
mutation of the type object. This makes it possible to
share the object safely between multiple interpreters.
This flag is checked in ``type_setattro`` and blocks
setting of attributes when set, similar to built-in types.

A new pointer, ``ht_moduleptr``, will be added to heap types to store ``exc``.

On deinitialization of the exception type, ``*exc`` will be set to ``NULL``.
This makes it safe for ``PyErr_PrepareImmutableException`` to check if
the exception was already initialized.

PyType_offsets
--------------

Some extension types are using instances with ``__dict__`` or ``__weakref__``
allocated. Currently, there is no way of passing offsets of these through
``PyType_Spec``. To allow this, a new structure and a spec slot are proposed.

A new structure, ``PyType_offsets``, will have two members containing the
offsets of ``__dict__`` and ``__weakref__``::

    typedef struct {
        Py_ssize_t dict;
        Py_ssize_t weaklist;
    } PyType_offsets;

The new slot, ``Py_offsets``, will be used to pass a ``PyType_offsets *``
structure containing the mentioned data.


Helpers
-------

Getting to per-module state from a heap type is a very common task. To make this
easier, a helper will be added::

    void *PyType_GetModuleState(PyObject *type)

This function takes a heap type and on success, it returns pointer to state of the
module that the heap type belongs to.

On failure, two scenarios may occur. When a type without a module is passed in,
``SystemError`` is set and ``NULL`` returned. If the module is found, pointer
to the state, which may be ``NULL``, is returned without setting any exception.


Modules Converted in the Initial Implementation
-----------------------------------------------

To validate the approach, several modules will be modified during
the initial implementation:

The ``zipimport``, ``_io``, ``_elementtree``, and ``_csv`` modules
will be ported to PEP 489 multiphase initialization.


Summary of API Changes and Additions
====================================

New functions:

* PyType_GetModule
* PyType_DefiningTypeFromSlotFunc
* PyType_GetModuleState
* PyErr_PrepareImmutableException

New macros:

* PyCFunction_GET_CLASS

New types:

* PyCMethodObject

New structures:

* PyType_offsets

Modified functions:

* _PyMethodDef_RawFastCallDict now receives ``PyTypeObject *cls``.
* _PyMethodDef_RawFastCallKeywords now receives ``PyTypeObject *cls``.

Modified structures:

* _heaptypeobject - added ht_module and ht_moduleptr

Other changes:

* METH_METHOD call flag
* defining_class converter in clinic
* Py_TPFLAGS_HEAP_IMMUTABLE flag
* Py_offsets type spec slot


Backwards Compatibility
=======================

Two new pointers are added to all heap types.
All other changes are adding new functions, structures and a type flag.

The new ``PyErr_PrepareImmutableException`` function changes encourages
modules to switch from using heap type Exception classes to immutable ones,
and a number of modules will be switched in the initial implementation.
This change will prevent adding class attributes to such types.
For example, the following will raise AttributeError::

    sqlite.OperationalError.foo = None

Instances and subclasses of such exceptions will not be affected.

Implementation
==============

An initial implementation is available in a Github repository [#gh-repo]_;
a patchset is at [#gh-patch]_.


Possible Future Extensions
==========================

Easy creation of types with module references
---------------------------------------------

It would be possible to add a PEP 489 execution slot type to make
creating heap types significantly easier than calling
``PyType_FromModuleAndSpec``.
This is left to a future PEP.


Optimization
------------

CPython optimizes calls to methods that have restricted signatures,
such as not allowing keyword arguments.

As proposed here, methods defined with the ``METH_METHOD`` flag do not support
these optimizations.

Optimized calls still have the option of accessing per-module state
the same way slot methods do.


References
==========

.. [#typeslots-mail] [Import-SIG] On singleton modules, heap types, and subinterpreters
   (https://mail.python.org/pipermail/import-sig/2015-July/001035.html)

.. [#gh-repo]
   https://github.com/Traceur759/cpython/commits/pep-c

.. [#gh-patch]
   https://github.com/Traceur759/cpython/compare/master...Traceur759:pep-c.patch


Copyright
=========

This document has been placed in the public domain.



..
   Local Variables:
   mode: indented-text
   indent-tabs-mode: nil
   sentence-end-double-space: t
   fill-column: 70
   coding: utf-8
   End:
````

</details>

<details><summary><b>Step 3 — revision_3</b> (2339 words)</summary>

````text
Abstract
========

This PEP proposes to add a way for CPython extension methods to access context such as
the state of the modules they are defined in.

This will allow extension methods to use direct pointer dereferences
rather than PyState_FindModule for looking up module state, reducing or eliminating the
performance cost of using module-scoped state over process global state.

This fixes one of the remaining roadblocks for adoption of PEP 3121 (Extension
module initialization and finalization) and PEP 489
(Multi-phase extension module initialization).

While this PEP takes an additional step towards fully solving the problems that PEP 3121 and PEP 489 started
tackling, it does not attempt to resolve *all* remaining concerns. In particular, accessing the module state from slot methods (``nb_add``, etc) remains slower than accessing that state from other extension methods.


Terminology
===========

Process-Global State
--------------------

C-level static variables. Since this is very low-level
memory storage, it must be managed carefully.

.. _per-module state:

Per-module State
----------------

State local to a module object, allocated dynamically as part of a
module object's initialization. This isolates the state from other
instances of the module (including those in other subinterpreters).

Accessed by ``PyModule_GetState()``.


Static Type
-----------

A type object defined as a C-level static variable, i.e. a compiled-in type object.

A static type needs to be shared between module instances and has no
information of what module it belongs to.
Static types do not have ``__dict__`` (although their instances might).

Heap Type
---------

A type object created at run time.


Rationale
=========

PEP 489 introduced a new way to initialize extension modules, which brings
several advantages to extensions that implement it:

* The extension modules behave more like their Python counterparts.
* The extension modules can easily support loading into pre-existing
  module objects, which paves the way for extension module support for
  ``runpy`` or for systems that enable extension module reloading.
* Loading multiple modules from the same extension is possible, which
  makes testing module isolation (a key feature for proper sub-interpreter
  support) possible from a single interpreter.

The biggest hurdle for adoption of PEP 489 is allowing access to module state
from methods of extension types.
Currently, the way to access this state from extension methods is by looking up the module via
``PyState_FindModule`` (in contrast to module level functions in extension modules, which
receive a module reference as an argument).
However, ``PyState_FindModule`` queries the thread-local state, making it relatively
costly compared to C level process global access and consequently deterring module authors from using it.

Also, ``PyState_FindModule`` relies on the assumption that in each
subinterpreter, there is at most one module corresponding to
a given ``PyModuleDef``.  This does not align well with Python's import
machinery.  Since PEP 489 aimed to fix that,  the assumption does
not hold for modules that use multi-phase initialization, so
``PyState_FindModule`` is unavailable for these modules.

A faster, safer way of accessing module-level state from extension methods
is needed.


Background
===========

The implementation of a Python method may need access to one or more of
the following pieces of information:

* The instance it is called on (``self``)
* The underlying function
* The class the method was defined in
* The corresponding module
* The module state

In Python code, the Python-level equivalents may be retrieved as::

    import sys

    class Foo:
        def meth(self):
            instance = self
            module_globals = globals()
            module_object = sys.modules[__name__]  # (1)
            underlying_function = Foo.meth         # (1)
            defining_class = Foo                   # (1)
            defining_class = __class__             # (2)

.. note::

    The defining class is not ``type(self)``, since ``type(self)`` might
    be a subclass of ``Foo``.

The statements marked (1) implicitly rely on name-based lookup via the function's ``__globals__``:
either the ``Foo`` attribute to access the defining class and Python function object, or ``__name__`` to find the module object in ``sys.modules``.
In Python code, this is feasible, as ``__globals__`` is set appropriately when the function definition is executed, and
even if the namespace has been manipulated to return a different object, at worst an exception will be raised.

The ``__class__`` closure, (2), is a safer way to get the defining class, but it still relies on ``__closure__`` being set appropriately.

By contrast, extension methods are typically implemented as normal C functions.
This means that they only have access to their arguments and C level thread-local
and process-global states. Traditionally, many extension modules have stored
their shared state in C-level process globals, causing problems when:

* running multiple initialize/finalize cycles in the same process
* reloading modules (e.g. to test conditional imports)
* loading extension modules in subinterpreters

PEP 3121 attempted to resolve this by offering the ``PyState_FindModule`` API, but this still has significant problems when it comes to extension methods (rather than module level functions):

* it is markedly slower than directly accessing C-level process-global state
* there is still some inherent reliance on process global state that means it still doesn't reliably handle module reloading

It's also the case that when looking up a C-level struct such as module state, supplying
an unexpected object layout can crash the interpreter, so it's significantly more important to ensure that extension
methods receive the kind of object they expect.

Proposal
========

Currently, a bound extension method (``PyCFunction`` or ``PyCFunctionWithKeywords``) receives only
``self``, and (if applicable) the supplied positional and keyword arguments.

While module-level extension functions already receive access to the defining module object via their
``self`` argument, methods of extension types don't have that luxury: they receive the bound instance
via ``self``, and hence have no direct access to the defining class or the module level state.

The additional module level context described above can be made available with two changes.
Both additions are optional; extension authors need to opt in to start
using them:

* Add a pointer to the module to heap type objects.

* Pass the defining class to the underlying C function.

  The defining class is readily available at the time built-in
  method object (``PyCFunctionObject``) is created, so it can be stored
  in a new struct that extends ``PyCFunctionObject``.

The module state can then be retrieved from the module object via
``PyModule_GetState``.

Note that this proposal implies that any type whose method needs to access
`per-module state`_ must be a heap type, rather than a static type.

This is necessary to support loading multiple module objects from a single
extension: a static type, as a C-level global, has no information about
which module object it belongs to.


Slot methods
------------

The above changes don't cover slot methods, such as ``tp_iter`` or ``nb_add``.

The problem with slot methods is that their C API is fixed, so we can't
simply add a new argument to pass in the defining class.
Two possible solutions have been proposed to this problem:

* Look up the class through walking the MRO.
  This is potentially expensive, but will be useful if performance is not
  a problem (such as when raising a module-level exception).
* Storing a pointer to the defining class of each slot in a separate table,
  ``__typeslots__`` [#typeslots-mail]_.  This is technically feasible and fast,
  but quite invasive.

Due to the invasiveness of the latter approach, this PEP proposes adding an MRO walking
helper for use in slot method implementations, deferring the more complex alternative
as a potential future optimisation. Modules affected by this concern also have the
option of using thread-local state or PEP 567 context variables, or else defining their
own reload-friendly lookup caching scheme.


Specification
=============

Adding module references to heap types
--------------------------------------

The ``PyHeapTypeObject`` struct will get a new member, ``PyObject *ht_module``,
that can store a pointer to the module object for which the type was defined.
It will be ``NULL`` by default, and should not be modified after the type
object is created.

A new factory method will be added for creating modules::

    PyObject* PyType_FromModuleAndSpec(PyObject *module,
                                       PyType_Spec *spec,
                                       PyObject *bases)

This acts the same as ``PyType_FromSpecWithBases``, and additionally sets
``ht_module`` to the provided module object.

Additionally, an accessor, ``PyObject * PyType_GetModule(PyTypeObject *)``
will be provided.
It will return the ``ht_module`` if a heap type with module pointer set
is passed in, otherwise it will set a SystemError and return NULL.

Usually, creating a class with ``ht_module`` set will create a reference
cycle involving the class and the module.
This is not a problem, as tearing down modules is not a performance-sensitive
operation (and module-level functions typically also create reference cycles).
The existing "set all module globals to None" code that breaks function cycles
through ``f_globals`` will also break the new cycles through ``ht_module``.


Passing the defining class to extension methods
-----------------------------------------------

Since PEP 590 [#pep-590]_ was accepted for Python 3.8, ``PyCFunction``
implements the vectorcall protocol.
This PEP builds on top of PEP 590 to provide C implemented methods with
context about their defining class (and thus their defining module).

A new signature flag, ``METH_METHOD``, will be added. Conceptually, it adds
``defining_class`` to the function signature.
To make the initial implementation easier, the flag can only be used as
``(METH_FASTCALL | METH_KEYWORDS | METH_METHOD)``.
(It can't be used with other flags like ``METH_O`` or bare ``METH_FASTCALL``,
though it may be combined with ``METH_CLASS`` or ``METH_STATIC``).

A corresponding new C signature, ``PyCMethod``, is added to the ``PyCFunction``
set of signatures::

    PyObject *PyCMethod(PyObject *self,
                        PyTypeObject *defining_class,
                        PyObject *const *args,
                        size_t nargsf,
                        PyObject *kwnames)

Additional combinations like ``(METH_VARARGS | METH_METHOD)`` may be added
in the future (or even in the initial implementation of this PEP).
However, ``METH_METHOD`` should always be an *additional* flag, i.e., the
defining class should only be passed in if needed.

To hold the extra information, a new structure extending ``PyCFunctionObject``
will be added::

    typedef struct {
        PyCFunctionObject func;
        PyTypeObject *mm_class; /* Passed as 'defining_class' arg to the C func */
    } PyCMethodObject;

The ``PyCFunction`` implementation will pass ``mm_class`` into a
``PyCMethod`` C function when it finds the ``METH_METHOD`` flag being set.
A new macro ``PyCFunction_GET_CLASS(cls)`` will be added for easier access
to ``mm_class``.

C methods may continue to use the other ``METH_*`` signatures if they do
not require access to their defining class/module.
If ``METH_METHOD`` is not set, casting to ``PyCMethodObject`` is invalid.


Argument Clinic
---------------

To support passing the defining class to methods using Argument Clinic,
a new converter will be added to clinic.py: ``defining_class``.

Each method may only have one argument using this converter, and it must
appear after ``self``, or, if ``self`` is not used, as the first argument.
The argument will be of type ``PyTypeObject *``.

When used, Argument Clinic will select
``METH_FASTCALL | METH_KEYWORDS | METH_METHOD`` as the calling convention.
The argument will not appear in ``__text_signature__``.

This will be compatible with ``__init__`` and ``__new__`` methods, where an
MRO walker will be used to pass the defining class from clinic generated
code to the user's function.


Slot methods
------------

To allow access to `per-module state`_ from slot methods, an MRO walker
will be implemented::

    PyTypeObject *PyType_DefiningTypeFromSlotFunc(PyTypeObject *type,
                                                  int slot, void *func)

The walker will go through bases of heap-allocated ``type``
and search for class that defines ``func`` at its ``slot``.

The ``func`` needs not to be inherited by ``type``. The only requirement
for the walker to find the defining class is that the defining class
must be heap-allocated.

On failure, exception is set and NULL is returned.


PyType_offsets
--------------

Some extension types are using instances with ``__dict__`` or ``__weakref__``
allocated. Currently, there is no way of passing offsets of these through
``PyType_Spec``. To allow this, a new structure and a spec slot are proposed.

A new structure, ``PyType_offsets``, will have two members containing the
offsets of ``__dict__`` and ``__weakref__``::

    typedef struct {
        Py_ssize_t dict;
        Py_ssize_t weaklist;
    } PyType_offsets;

The new slot, ``Py_offsets``, will be used to pass a ``PyType_offsets *``
structure containing the mentioned data.


Helpers
-------

Getting to `per-module state`_ from a heap type is a very common task. To make
this easier, a helper will be added::

    void *PyType_GetModuleState(PyObject *type)

This function takes a heap type and on success, it returns pointer to state of the
module that the heap type belongs to.

On failure, two scenarios may occur. When a type without a module is passed in,
``SystemError`` is set and ``NULL`` returned. If the module is found, pointer
to the state, which may be ``NULL``, is returned without setting any exception.


Modules Converted in the Initial Implementation
-----------------------------------------------

To validate the approach, several modules will be modified during
the initial implementation:

The ``zipimport``, ``_io``, ``_elementtree``, and ``_csv`` modules
will be ported to PEP 489 multiphase initialization.


Summary of API Changes and Additions
====================================

New functions:

* ``PyType_GetModule``
* ``PyType_DefiningTypeFromSlotFunc``
* ``PyType_GetModuleState``

New macros:

* ``PyCFunction_GET_CLASS``

New types:

* ``PyCMethodObject``

New structures:

* ``PyType_offsets``

Modified functions:

* ``_PyMethodDef_RawFastCallDict`` now receives ``PyTypeObject *cls``.
* ``_PyMethodDef_RawFastCallKeywords`` now receives ``PyTypeObject *cls``.

Modified structures:

* _heaptypeobject - added ``ht_module`` and ``ht_moduleptr``

Other changes:

* ``METH_METHOD`` call flag
* ``defining_class`` converter in clinic
* ``Py_TPFLAGS_HEAP_IMMUTABLE`` flag
* ``Py_offsets`` type spec slot


Backwards Compatibility
=======================

Two new pointers are added to all heap types.
All other changes are adding new functions, structures and a type flag,
or changes to private implementation details.

Implementation
==============

An initial implementation is available in a Github repository [#gh-repo]_;
a patchset is at [#gh-patch]_.


Possible Future Extensions
==========================

Easy creation of types with module references
---------------------------------------------

It would be possible to add a PEP 489 execution slot type to make
creating heap types significantly easier than calling
``PyType_FromModuleAndSpec``.
This is left to a future PEP.

It may be good to add a good way to create static exception types from the
limited API. Such exception types could be shared between subinterpreters,
but instantiated without needing specific module state.
This is also left to possible future discussions.


Optimization
------------

As proposed here, methods defined with the ``METH_METHOD`` flag only support
one specific signature.

If it turns out that other signatures are needed for performance reasons,
they may be added.


References
==========

.. [#typeslots-mail] [Import-SIG] On singleton modules, heap types, and subinterpreters
   (https://mail.python.org/pipermail/import-sig/2015-July/001035.html)

.. [#gh-repo]
   https://github.com/Dormouse759/cpython/tree/pep-c-rebase_newer

.. [#gh-patch]
   https://github.com/Dormouse759/cpython/compare/master...Dormouse759:pep-c-rebase_newer

.. [#pep-590]
   https://www.python.org/dev/peps/pep-0590/


Copyright
=========

This document has been placed in the public domain.



..
   Local Variables:
   mode: indented-text
   indent-tabs-mode: nil
   sentence-end-double-space: t
   fill-column: 70
   coding: utf-8
   End:
````

</details>

<details><summary><b>Step 4 — revision_4</b> (2238 words)</summary>

````text
Abstract
========

This PEP proposes to add a way for CPython extension methods to access context such as
the state of the modules they are defined in.

This will allow extension methods to use direct pointer dereferences
rather than PyState_FindModule for looking up module state, reducing or eliminating the
performance cost of using module-scoped state over process global state.

This fixes one of the remaining roadblocks for adoption of PEP 3121 (Extension
module initialization and finalization) and PEP 489
(Multi-phase extension module initialization).

While this PEP takes an additional step towards fully solving the problems that PEP 3121 and PEP 489 started
tackling, it does not attempt to resolve *all* remaining concerns. In particular, accessing the module state from slot methods (``nb_add``, etc) remains slower than accessing that state from other extension methods.


Terminology
===========

Process-Global State
--------------------

C-level static variables. Since this is very low-level
memory storage, it must be managed carefully.

.. _per-module state:

Per-module State
----------------

State local to a module object, allocated dynamically as part of a
module object's initialization. This isolates the state from other
instances of the module (including those in other subinterpreters).

Accessed by ``PyModule_GetState()``.


Static Type
-----------

A type object defined as a C-level static variable, i.e. a compiled-in type object.

A static type needs to be shared between module instances and has no
information of what module it belongs to.
Static types do not have ``__dict__`` (although their instances might).

Heap Type
---------

A type object created at run time.


Rationale
=========

PEP 489 introduced a new way to initialize extension modules, which brings
several advantages to extensions that implement it:

* The extension modules behave more like their Python counterparts.
* The extension modules can easily support loading into pre-existing
  module objects, which paves the way for extension module support for
  ``runpy`` or for systems that enable extension module reloading.
* Loading multiple modules from the same extension is possible, which
  makes testing module isolation (a key feature for proper sub-interpreter
  support) possible from a single interpreter.

The biggest hurdle for adoption of PEP 489 is allowing access to module state
from methods of extension types.
Currently, the way to access this state from extension methods is by looking up the module via
``PyState_FindModule`` (in contrast to module level functions in extension modules, which
receive a module reference as an argument).
However, ``PyState_FindModule`` queries the thread-local state, making it relatively
costly compared to C level process global access and consequently deterring module authors from using it.

Also, ``PyState_FindModule`` relies on the assumption that in each
subinterpreter, there is at most one module corresponding to
a given ``PyModuleDef``.  This does not align well with Python's import
machinery.  Since PEP 489 aimed to fix that,  the assumption does
not hold for modules that use multi-phase initialization, so
``PyState_FindModule`` is unavailable for these modules.

A faster, safer way of accessing module-level state from extension methods
is needed.


Background
===========

The implementation of a Python method may need access to one or more of
the following pieces of information:

* The instance it is called on (``self``)
* The underlying function
* The class the method was defined in
* The corresponding module
* The module state

In Python code, the Python-level equivalents may be retrieved as::

    import sys

    class Foo:
        def meth(self):
            instance = self
            module_globals = globals()
            module_object = sys.modules[__name__]  # (1)
            underlying_function = Foo.meth         # (1)
            defining_class = Foo                   # (1)
            defining_class = __class__             # (2)

.. note::

    The defining class is not ``type(self)``, since ``type(self)`` might
    be a subclass of ``Foo``.

The statements marked (1) implicitly rely on name-based lookup via the function's ``__globals__``:
either the ``Foo`` attribute to access the defining class and Python function object, or ``__name__`` to find the module object in ``sys.modules``.
In Python code, this is feasible, as ``__globals__`` is set appropriately when the function definition is executed, and
even if the namespace has been manipulated to return a different object, at worst an exception will be raised.

The ``__class__`` closure, (2), is a safer way to get the defining class, but it still relies on ``__closure__`` being set appropriately.

By contrast, extension methods are typically implemented as normal C functions.
This means that they only have access to their arguments and C level thread-local
and process-global states. Traditionally, many extension modules have stored
their shared state in C-level process globals, causing problems when:

* running multiple initialize/finalize cycles in the same process
* reloading modules (e.g. to test conditional imports)
* loading extension modules in subinterpreters

PEP 3121 attempted to resolve this by offering the ``PyState_FindModule`` API, but this still has significant problems when it comes to extension methods (rather than module level functions):

* it is markedly slower than directly accessing C-level process-global state
* there is still some inherent reliance on process global state that means it still doesn't reliably handle module reloading

It's also the case that when looking up a C-level struct such as module state, supplying
an unexpected object layout can crash the interpreter, so it's significantly more important to ensure that extension
methods receive the kind of object they expect.

Proposal
========

Currently, a bound extension method (``PyCFunction`` or ``PyCFunctionWithKeywords``) receives only
``self``, and (if applicable) the supplied positional and keyword arguments.

While module-level extension functions already receive access to the defining module object via their
``self`` argument, methods of extension types don't have that luxury: they receive the bound instance
via ``self``, and hence have no direct access to the defining class or the module level state.

The additional module level context described above can be made available with two changes.
Both additions are optional; extension authors need to opt in to start
using them:

* Add a pointer to the module to heap type objects.

* Pass the defining class to the underlying C function.

  The defining class is readily available at the time built-in
  method object (``PyCFunctionObject``) is created, so it can be stored
  in a new struct that extends ``PyCFunctionObject``.

The module state can then be retrieved from the module object via
``PyModule_GetState``.

Note that this proposal implies that any type whose method needs to access
`per-module state`_ must be a heap type, rather than a static type.

This is necessary to support loading multiple module objects from a single
extension: a static type, as a C-level global, has no information about
which module object it belongs to.


Slot methods
------------

The above changes don't cover slot methods, such as ``tp_iter`` or ``nb_add``.

The problem with slot methods is that their C API is fixed, so we can't
simply add a new argument to pass in the defining class.
Two possible solutions have been proposed to this problem:

* Look up the class through walking the MRO.
  This is potentially expensive, but will be useful if performance is not
  a problem (such as when raising a module-level exception).
* Storing a pointer to the defining class of each slot in a separate table,
  ``__typeslots__`` [#typeslots-mail]_.  This is technically feasible and fast,
  but quite invasive.

Due to the invasiveness of the latter approach, this PEP proposes adding an MRO walking
helper for use in slot method implementations, deferring the more complex alternative
as a potential future optimisation. Modules affected by this concern also have the
option of using thread-local state or PEP 567 context variables, or else defining their
own reload-friendly lookup caching scheme.


Specification
=============

Adding module references to heap types
--------------------------------------

The ``PyHeapTypeObject`` struct will get a new member, ``PyObject *ht_module``,
that can store a pointer to the module object for which the type was defined.
It will be ``NULL`` by default, and should not be modified after the type
object is created.

A new factory method will be added for creating modules::

    PyObject* PyType_FromModuleAndSpec(PyObject *module,
                                       PyType_Spec *spec,
                                       PyObject *bases)

This acts the same as ``PyType_FromSpecWithBases``, and additionally sets
``ht_module`` to the provided module object.

Additionally, an accessor, ``PyObject * PyType_GetModule(PyTypeObject *)``
will be provided.
It will return the ``ht_module`` if a heap type with module pointer set
is passed in, otherwise it will set a SystemError and return NULL.

Usually, creating a class with ``ht_module`` set will create a reference
cycle involving the class and the module.
This is not a problem, as tearing down modules is not a performance-sensitive
operation (and module-level functions typically also create reference cycles).
The existing "set all module globals to None" code that breaks function cycles
through ``f_globals`` will also break the new cycles through ``ht_module``.


Passing the defining class to extension methods
-----------------------------------------------

Since PEP 590 [#pep-590]_ was accepted for Python 3.8, ``PyCFunction``
implements the vectorcall protocol.
This PEP builds on top of PEP 590 to provide C implemented methods with
context about their defining class (and thus their defining module).

A new signature flag, ``METH_METHOD``, will be added. Conceptually, it adds
``defining_class`` to the function signature.
To make the initial implementation easier, the flag can only be used as
``(METH_FASTCALL | METH_KEYWORDS | METH_METHOD)``.
(It can't be used with other flags like ``METH_O`` or bare ``METH_FASTCALL``,
though it may be combined with ``METH_CLASS`` or ``METH_STATIC``).

A corresponding new C signature, ``PyCMethod``, is added to the ``PyCFunction``
set of signatures::

    PyObject *PyCMethod(PyObject *self,
                        PyTypeObject *defining_class,
                        PyObject *const *args,
                        size_t nargsf,
                        PyObject *kwnames)

Additional combinations like ``(METH_VARARGS | METH_METHOD)`` may be added
in the future (or even in the initial implementation of this PEP).
However, ``METH_METHOD`` should always be an *additional* flag, i.e., the
defining class should only be passed in if needed.

To hold the extra information, a new structure extending ``PyCFunctionObject``
will be added::

    typedef struct {
        PyCFunctionObject func;
        PyTypeObject *mm_class; /* Passed as 'defining_class' arg to the C func */
    } PyCMethodObject;

The ``PyCFunction`` implementation will pass ``mm_class`` into a
``PyCMethod`` C function when it finds the ``METH_METHOD`` flag being set.
A new macro ``PyCFunction_GET_CLASS(cls)`` will be added for easier access
to ``mm_class``.

C methods may continue to use the other ``METH_*`` signatures if they do
not require access to their defining class/module.
If ``METH_METHOD`` is not set, casting to ``PyCMethodObject`` is invalid.


Argument Clinic
---------------

To support passing the defining class to methods using Argument Clinic,
a new converter will be added to clinic.py: ``defining_class``.

Each method may only have one argument using this converter, and it must
appear after ``self``, or, if ``self`` is not used, as the first argument.
The argument will be of type ``PyTypeObject *``.

When used, Argument Clinic will select
``METH_FASTCALL | METH_KEYWORDS | METH_METHOD`` as the calling convention.
The argument will not appear in ``__text_signature__``.

This will be compatible with ``__init__`` and ``__new__`` methods, where an
MRO walker will be used to pass the defining class from clinic generated
code to the user's function.


Slot methods
------------

To allow access to `per-module state`_ from slot methods, an MRO walker
will be implemented::

    PyTypeObject *PyType_DefiningTypeFromSlotFunc(PyTypeObject *type,
                                                  int slot, void *func)

The walker will go through bases of heap-allocated ``type``
and search for class that defines ``func`` at its ``slot``.

The ``func`` needs not to be inherited by ``type``. The only requirement
for the walker to find the defining class is that the defining class
must be heap-allocated.

On failure, exception is set and NULL is returned.


Helpers
-------

Getting to `per-module state`_ from a heap type is a very common task. To make
this easier, a helper will be added::

    void *PyType_GetModuleState(PyObject *type)

This function takes a heap type and on success, it returns pointer to state of the
module that the heap type belongs to.

On failure, two scenarios may occur. When a type without a module is passed in,
``SystemError`` is set and ``NULL`` returned. If the module is found, pointer
to the state, which may be ``NULL``, is returned without setting any exception.


Modules Converted in the Initial Implementation
-----------------------------------------------

To validate the approach, several modules will be modified during
the initial implementation:

The ``zipimport``, ``_io``, ``_elementtree``, and ``_csv`` modules
will be ported to PEP 489 multiphase initialization.


Summary of API Changes and Additions
====================================

New functions:

* ``PyType_GetModule``
* ``PyType_DefiningTypeFromSlotFunc``
* ``PyType_GetModuleState``

New macros:

* ``PyCFunction_GET_CLASS``

New types:

* ``PyCMethodObject``

Modified structures:

* _heaptypeobject - added ``ht_module``

Other changes:

* ``METH_METHOD`` call flag
* ``defining_class`` converter in clinic


Backwards Compatibility
=======================

Two new pointers are added to all heap types.
All other changes are adding new functions and structures,
or changes to private implementation details.

Implementation
==============

An initial implementation is available in a Github repository [#gh-repo]_;
a patchset is at [#gh-patch]_.


Possible Future Extensions
==========================

Easy creation of types with module references
---------------------------------------------

It would be possible to add a PEP 489 execution slot type to make
creating heap types significantly easier than calling
``PyType_FromModuleAndSpec``.
This is left to a future PEP.

It may be good to add a good way to create static exception types from the
limited API. Such exception types could be shared between subinterpreters,
but instantiated without needing specific module state.
This is also left to possible future discussions.


Optimization
------------

As proposed here, methods defined with the ``METH_METHOD`` flag only support
one specific signature.

If it turns out that other signatures are needed for performance reasons,
they may be added.


References
==========

.. [#typeslots-mail] [Import-SIG] On singleton modules, heap types, and subinterpreters
   (https://mail.python.org/pipermail/import-sig/2015-July/001035.html)

.. [#gh-repo]
   https://github.com/Dormouse759/cpython/tree/pep-c-rebase_newer

.. [#gh-patch]
   https://github.com/Dormouse759/cpython/compare/master...Dormouse759:pep-c-rebase_newer

.. [#pep-590]
   https://www.python.org/dev/peps/pep-0590/


Copyright
=========

This document is placed in the public domain or under the
CC0-1.0-Universal license, whichever is more permissive.


..
   Local Variables:
   mode: indented-text
   indent-tabs-mode: nil
   sentence-end-double-space: t
   fill-column: 70
   coding: utf-8
   End:
````

</details>

<details><summary><b>Step 5 — revision_5</b> (2274 words)</summary>

````text
Abstract
========

This PEP proposes to add a way for CPython extension methods to access context,
such as the state of the modules they are defined in.

This will allow extension methods to use direct pointer dereferences
rather than PyState_FindModule for looking up module state, reducing or
eliminating the performance cost of using module-scoped state over process
global state.

This fixes one of the remaining roadblocks for adoption of PEP 3121 (Extension
module initialization and finalization) and PEP 489
(Multi-phase extension module initialization).

While this PEP takes an additional step towards fully solving the problems that
PEP 3121 and PEP 489 started tackling, it does not attempt to resolve *all*
remaining concerns. In particular, at least the first access to the module state
from slot methods (``nb_add``, etc) remains slower than accessing that state
from other extension methods. Standard caching techniques can be used to speed
up subsequent access.


Terminology
===========

Process-Global State
--------------------

C-level static variables. Since this is very low-level
memory storage, it must be managed carefully.

.. _per-module state:

Per-module State
----------------

State local to a module object, allocated dynamically as part of a
module object's initialization. This isolates the state from other
instances of the module (including those in other subinterpreters).

Accessed by ``PyModule_GetState()``.


Static Type
-----------

A type object defined as a C-level static variable, i.e. a compiled-in type
object.

A static type needs to be shared between module instances and has no
information of what module it belongs to.
Static types do not have ``__dict__`` (although their instances might).


Heap Type
---------

A type object created at run time.


Rationale
=========

PEP 489 introduced a new way to initialize extension modules, which brings
several advantages to extensions that implement it:

* The extension modules behave more like their Python counterparts.
* The extension modules can easily support loading into pre-existing
  module objects, which paves the way for extension module support for
  ``runpy`` or for systems that enable extension module reloading.
* Loading multiple modules from the same extension is possible, which
  makes it possible to test module isolation (a key feature for proper
  sub-interpreter support) from a single interpreter.

The biggest hurdle for adoption of PEP 489 is allowing access to module state
from methods of extension types.
Currently, the way to access this state from extension methods is by looking up
the module via ``PyState_FindModule`` (in contrast to module level functions in
extension modules, which receive a module reference as an argument).
However, ``PyState_FindModule`` queries the thread-local state, making it
relatively costly compared to C level process global access and consequently
deterring module authors from using it.

Also, ``PyState_FindModule`` relies on the assumption that in each
subinterpreter, there is at most one module corresponding to
a given ``PyModuleDef``.  This assumption does not hold for modules that use
PEP 489's multi-phase initialization, so ``PyState_FindModule`` is unavailable
for these modules.

A faster, safer way of accessing module-level state from extension methods
is needed.


Background
===========

The implementation of a Python method may need access to one or more of
the following pieces of information:

* The instance it is called on (``self``)
* The underlying function
* The class the method was defined in
* The corresponding module
* The module state

In Python code, the Python-level equivalents may be retrieved as::

    import sys

    class Foo:
        def meth(self):
            instance = self
            module_globals = globals()
            module_object = sys.modules[__name__]  # (1)
            underlying_function = Foo.meth         # (1)
            defining_class = Foo                   # (1)
            defining_class = __class__             # (2)

.. note::

    The defining class is not ``type(self)``, since ``type(self)`` might
    be a subclass of ``Foo``.

The statements marked (1) implicitly rely on name-based lookup via the
function's ``__globals__``: either the ``Foo`` attribute to access the defining
class and Python function object, or ``__name__`` to find the module object in
``sys.modules``.

In Python code, this is feasible, as ``__globals__`` is set appropriately when
the function definition is executed, and even if the namespace has been
manipulated to return a different object, at worst an exception will be raised.

The ``__class__`` closure, (2), is a safer way to get the defining class, but it
still relies on ``__closure__`` being set appropriately.

By contrast, extension methods are typically implemented as normal C functions.
This means that they only have access to their arguments and C level thread-local
and process-global states. Traditionally, many extension modules have stored
their shared state in C-level process globals, causing problems when:

* running multiple initialize/finalize cycles in the same process
* reloading modules (e.g. to test conditional imports)
* loading extension modules in subinterpreters

PEP 3121 attempted to resolve this by offering the ``PyState_FindModule`` API,
but this still has significant problems when it comes to extension methods
(rather than module level functions):

* it is markedly slower than directly accessing C-level process-global state
* there is still some inherent reliance on process global state that means it
  still doesn't reliably handle module reloading

It's also the case that when looking up a C-level struct such as module state,
supplying an unexpected object layout can crash the interpreter, so it's
significantly more important to ensure that extension methods receive the kind
of object they expect.


Proposal
========

Currently, a bound extension method (``PyCFunction`` or
``PyCFunctionWithKeywords``) receives only ``self``, and (if applicable) the
supplied positional and keyword arguments.

While module-level extension functions already receive access to the defining
module object via their ``self`` argument, methods of extension types don't have
that luxury: they receive the bound instance via ``self``, and hence have no
direct access to the defining class or the module level state.

The additional module level context described above can be made available with
two changes.
Both additions are optional; extension authors need to opt in to start
using them:

* Add a pointer to the module to heap type objects.

* Pass the defining class to the underlying C function.

  The defining class is readily available at the time the built-in
  method object (``PyCFunctionObject``) is created, so it can be stored
  in a new struct that extends ``PyCFunctionObject``.

The module state can then be retrieved from the module object via
``PyModule_GetState``.

Note that this proposal implies that any type whose methods need to access
`per-module state`_ must be a heap type, rather than a static type. This is
necessary to support loading multiple module objects from a single
extension: a static type, as a C-level global, has no information about
which module object it belongs to.


Slot methods
------------

The above changes don't cover slot methods, such as ``tp_iter`` or ``nb_add``.

The problem with slot methods is that their C API is fixed, so we can't
simply add a new argument to pass in the defining class.
Two possible solutions have been proposed to this problem:

* Look up the class through walking the MRO.
  This is potentially expensive, but will be usable if performance is not
  a problem (such as when raising a module-level exception).
* Storing a pointer to the defining class of each slot in a separate table,
  ``__typeslots__`` [#typeslots-mail]_.  This is technically feasible and fast,
  but quite invasive.

Due to the invasiveness of the latter approach, this PEP proposes adding an MRO
walking helper for use in slot method implementations, deferring the more complex
alternative as a potential future optimisation.

Modules affected by this concern also have the option of using
`thread-local state`_ or `PEP 567 context variables`_ as a caching mechanism, or
else defining their own reload-friendly lookup caching scheme.

.. _thread-local state: https://docs.python.org/3/c-api/init.html#thread-local-storage-support
.. _PEP 567 context variables: https://docs.python.org/3/c-api/contextvars.html


Specification
=============

Adding module references to heap types
--------------------------------------

The ``PyHeapTypeObject`` struct will get a new member, ``PyObject *ht_module``,
that can store a pointer to the module object for which the type was defined.
It will be ``NULL`` by default, and should not be modified after the type
object is created.

A new factory method will be added for creating modules::

    PyObject* PyType_FromModuleAndSpec(PyObject *module,
                                       PyType_Spec *spec,
                                       PyObject *bases)

This acts the same as ``PyType_FromSpecWithBases``, and additionally sets
``ht_module`` to the provided module object.

Additionally, an accessor, ``PyObject * PyType_GetModule(PyTypeObject *)``
will be provided.
It will return the ``ht_module`` if a heap type with module pointer set
is passed in, otherwise it will set ``TypeError`` and return NULL.

Usually, creating a class with ``ht_module`` set will create a reference
cycle involving the class and the module.
This is not a problem, as tearing down modules is not a performance-sensitive
operation, and module-level functions typically also create reference cycles.
The existing "set all module globals to None" code that breaks function cycles
through ``f_globals`` will also break the new cycles through ``ht_module``.


Passing the defining class to extension methods
-----------------------------------------------

Since PEP 590 [#pep-590]_ was accepted for Python 3.8, ``PyCFunction``
implements the vectorcall protocol.
This PEP builds on top of PEP 590 to provide C implemented methods with
context about their defining class (and thus their defining module).

A new signature flag, ``METH_METHOD``, will be added. Conceptually, it adds
``defining_class`` to the function signature.
To make the initial implementation easier, the flag can only be used as
``(METH_FASTCALL | METH_KEYWORDS | METH_METHOD)``.
(It can't be used with other flags like ``METH_O`` or bare ``METH_FASTCALL``,
though it may be combined with ``METH_CLASS`` or ``METH_STATIC``).

A corresponding new C signature, ``PyCMethod``, is added to the ``PyCFunction``
set of signatures::

    PyObject *PyCMethod(PyObject *self,
                        PyTypeObject *defining_class,
                        PyObject *const *args,
                        size_t nargsf,
                        PyObject *kwnames)

Additional combinations like ``(METH_VARARGS | METH_METHOD)`` may be added
in the future (or even in the initial implementation of this PEP).
However, ``METH_METHOD`` should always be an *additional* flag, i.e., the
defining class should only be passed in if needed.

To hold the extra information, a new structure extending ``PyCFunctionObject``
will be added::

    typedef struct {
        PyCFunctionObject func;
        PyTypeObject *mm_class; /* Passed as 'defining_class' arg to the C func */
    } PyCMethodObject;

The ``PyCFunction`` implementation will pass ``mm_class`` into a
``PyCMethod`` C function when it finds the ``METH_METHOD`` flag being set.
A new macro ``PyCFunction_GET_CLASS(cls)`` will be added for easier access
to ``mm_class``.

C methods may continue to use the other ``METH_*`` signatures if they do
not require access to their defining class/module.
If ``METH_METHOD`` is not set, casting to ``PyCMethodObject`` is invalid.


Argument Clinic
---------------

To support passing the defining class to methods using Argument Clinic,
a new converter will be added to clinic.py: ``defining_class``.

Each method may only have one argument using this converter, and it must
appear after ``self``, or, if ``self`` is not used, as the first argument.
The argument will be of type ``PyTypeObject *``.

When used, Argument Clinic will select
``METH_FASTCALL | METH_KEYWORDS | METH_METHOD`` as the calling convention.
The argument will not appear in ``__text_signature__``.

This will be compatible with ``__init__`` and ``__new__`` methods, where an
MRO walker will be used to pass the defining class from clinic generated
code to the user's function.


Slot methods
------------

To allow access to `per-module state`_ from slot methods, an MRO walker
will be implemented::

    PyTypeObject *PyType_DefiningTypeFromSlotFunc(PyTypeObject *type,
                                                  int slot, void *func)

The walker will go through bases of heap-allocated ``type``
and search for class that defines ``func`` at its ``slot``.

The ``func`` does not need to be inherited by ``type`` (i.e. it may have been
overridden in a subclass). The only requirement for the walker to find the
defining class is that the defining class must be heap-allocated.

On failure, exception is set and NULL is returned.


Helpers
-------

Getting to `per-module state`_ from a heap type is a very common task. To make
this easier, a helper will be added::

    void *PyType_GetModuleState(PyObject *type)

This function takes a heap type and on success, it returns pointer to the state
of the module that the heap type belongs to.

On failure, two scenarios may occur. When a non-type object, or a type without a
module is passed in, ``TypeError`` is set and ``NULL`` returned. If the module
is found, the pointer to the state, which may be ``NULL``, is returned without
setting any exception.


Modules Converted in the Initial Implementation
-----------------------------------------------

To validate the approach, several modules will be modified during
the initial implementation:

The ``zipimport``, ``_io``, ``_elementtree``, and ``_csv`` modules
will be ported to PEP 489 multiphase initialization.


Summary of API Changes and Additions
====================================

New functions:

* ``PyType_FromModuleAndSpec``
* ``PyType_GetModule``
* ``PyType_GetModuleState``
* ``PyType_DefiningTypeFromSlotFunc``

New macros:

* ``PyCFunction_GET_CLASS``

New types:

* ``PyCMethodObject``

Modified structures:

* _heaptypeobject - added ``ht_module``

Other changes:

* ``METH_METHOD`` call flag
* ``defining_class`` converter in clinic


Backwards Compatibility
=======================

One new pointer is added to all heap types.
All other changes are adding new functions and structures,
or changes to private implementation details.

Implementation
==============

An initial implementation is available in a Github repository [#gh-repo]_;
a patchset is at [#gh-patch]_.


Possible Future Extensions
==========================

Easy creation of types with module references
---------------------------------------------

It would be possible to add a PEP 489 execution slot type to make
creating heap types significantly easier than calling
``PyType_FromModuleAndSpec``.
This is left to a future PEP.

It may be good to add a good way to create static exception types from the
limited API. Such exception types could be shared between subinterpreters,
but instantiated without needing specific module state.
This is also left to possible future discussions.


Optimization
------------

As proposed here, methods defined with the ``METH_METHOD`` flag only support
one specific signature.

If it turns out that other signatures are needed for performance reasons,
they may be added.


References
==========

.. [#typeslots-mail] [Import-SIG] On singleton modules, heap types, and subinterpreters
   (https://mail.python.org/pipermail/import-sig/2015-July/001035.html)

.. [#gh-repo]
   https://github.com/Dormouse759/cpython/tree/pep-c-rebase_newer

.. [#gh-patch]
   https://github.com/Dormouse759/cpython/compare/master...Dormouse759:pep-c-rebase_newer

.. [#pep-590]
   https://www.python.org/dev/peps/pep-0590/


Copyright
=========

This document is placed in the public domain or under the
CC0-1.0-Universal license, whichever is more permissive.


..
   Local Variables:
   mode: indented-text
   indent-tabs-mode: nil
   sentence-end-double-space: t
   fill-column: 70
   coding: utf-8
   End:
````

</details>

<details><summary><b>Step 6 — revision_6</b> (2344 words)</summary>

````text
Abstract
========

This PEP proposes to add a way for CPython extension methods to access context,
such as the state of the modules they are defined in.

This will allow extension methods to use direct pointer dereferences
rather than PyState_FindModule for looking up module state, reducing or
eliminating the performance cost of using module-scoped state over process
global state.

This fixes one of the remaining roadblocks for adoption of PEP 3121 (Extension
module initialization and finalization) and PEP 489
(Multi-phase extension module initialization).

While this PEP takes an additional step towards fully solving the problems that
PEP 3121 and PEP 489 started tackling, it does not attempt to resolve *all*
remaining concerns. In particular, access to the module state
from slot methods (``nb_add``, etc) is not solved.


Terminology
===========

Process-Global State
--------------------

C-level static variables. Since this is very low-level
memory storage, it must be managed carefully.

.. _per-module state:

Per-module State
----------------

State local to a module object, allocated dynamically as part of a
module object's initialization. This isolates the state from other
instances of the module (including those in other subinterpreters).

Accessed by ``PyModule_GetState()``.


Static Type
-----------

A type object defined as a C-level static variable, i.e. a compiled-in type
object.

A static type needs to be shared between module instances and has no
information of what module it belongs to.
Static types do not have ``__dict__`` (although their instances might).


Heap Type
---------

A type object created at run time.


Defining Class
--------------

The defining class of a method (either bound or unbound) is the class on which
the method was defined.
A class that merely inherits the method from its base is not the defining class.

For example, ``int`` is the defining class of ``True.to_bytes``,
``True.__floor__`` and ``int.__repr__``.

In C, the defining class is the one defined with the corresponding
``tp_methods`` or "tp slots" [#tp-slots]_ entry.
For methods defined in Python, the defining class is saved in the
`__class__` closure cell.


C-API
-----

The "Python/C API" as described in Python documentation.
CPython implements the C-API, but other implementations exist.


Rationale
=========

PEP 489 introduced a new way to initialize extension modules, which brings
several advantages to extensions that implement it:

* The extension modules behave more like their Python counterparts.
* The extension modules can easily support loading into pre-existing
  module objects, which paves the way for extension module support for
  ``runpy`` or for systems that enable extension module reloading.
* Loading multiple modules from the same extension is possible, which
  makes it possible to test module isolation (a key feature for proper
  sub-interpreter support) from a single interpreter.

The biggest hurdle for adoption of PEP 489 is allowing access to module state
from methods of extension types.
Currently, the way to access this state from extension methods is by looking up
the module via ``PyState_FindModule`` (in contrast to module level functions in
extension modules, which receive a module reference as an argument).
However, ``PyState_FindModule`` queries the thread-local state, making it
relatively costly compared to C level process global access and consequently
deterring module authors from using it.

Also, ``PyState_FindModule`` relies on the assumption that in each
subinterpreter, there is at most one module corresponding to
a given ``PyModuleDef``.  This assumption does not hold for modules that use
PEP 489's multi-phase initialization, so ``PyState_FindModule`` is unavailable
for these modules.

A faster, safer way of accessing module-level state from extension methods
is needed.


Background
===========

The implementation of a Python method may need access to one or more of
the following pieces of information:

* The instance it is called on (``self``)
* The underlying function
* The *defining class*, i. e. the class the method was defined in
* The corresponding module
* The module state

In Python code, the Python-level equivalents may be retrieved as::

    import sys

    class Foo:
        def meth(self):
            instance = self
            module_globals = globals()
            module_object = sys.modules[__name__]  # (1)
            underlying_function = Foo.meth         # (1)
            defining_class = Foo                   # (1)
            defining_class = __class__             # (2)

.. note::

    The defining class is not ``type(self)``, since ``type(self)`` might
    be a subclass of ``Foo``.

The statements marked (1) implicitly rely on name-based lookup via the
function's ``__globals__``: either the ``Foo`` attribute to access the defining
class and Python function object, or ``__name__`` to find the module object in
``sys.modules``.

In Python code, this is feasible, as ``__globals__`` is set appropriately when
the function definition is executed, and even if the namespace has been
manipulated to return a different object, at worst an exception will be raised.

The ``__class__`` closure, (2), is a safer way to get the defining class, but it
still relies on ``__closure__`` being set appropriately.

By contrast, extension methods are typically implemented as normal C functions.
This means that they only have access to their arguments and C level thread-local
and process-global states. Traditionally, many extension modules have stored
their shared state in C-level process globals, causing problems when:

* running multiple initialize/finalize cycles in the same process
* reloading modules (e.g. to test conditional imports)
* loading extension modules in subinterpreters

PEP 3121 attempted to resolve this by offering the ``PyState_FindModule`` API,
but this still has significant problems when it comes to extension methods
(rather than module level functions):

* it is markedly slower than directly accessing C-level process-global state
* there is still some inherent reliance on process global state that means it
  still doesn't reliably handle module reloading

It's also the case that when looking up a C-level struct such as module state,
supplying an unexpected object layout can crash the interpreter, so it's
significantly more important to ensure that extension methods receive the kind
of object they expect.


Proposal
========

Currently, a bound extension method (``PyCFunction`` or
``PyCFunctionWithKeywords``) receives only ``self``, and (if applicable) the
supplied positional and keyword arguments.

While module-level extension functions already receive access to the defining
module object via their ``self`` argument, methods of extension types don't have
that luxury: they receive the bound instance via ``self``, and hence have no
direct access to the defining class or the module level state.

The additional module level context described above can be made available with
two changes.
Both additions are optional; extension authors need to opt in to start
using them:

* Add a pointer to the module to heap type objects.

* Pass the defining class to the underlying C function.

  In CPython, the defining class is readily available at the time the built-in
  method object (``PyCFunctionObject``) is created, so it can be stored
  in a new struct that extends ``PyCFunctionObject``.

The module state can then be retrieved from the module object via
``PyModule_GetState``.

Note that this proposal implies that any type whose methods need to access
`per-module state`_ must be a heap type, rather than a static type. This is
necessary to support loading multiple module objects from a single
extension: a static type, as a C-level global, has no information about
which module object it belongs to.


Slot methods
------------

The above changes don't cover slot methods, such as ``tp_iter`` or ``nb_add``.

The problem with slot methods is that their C API is fixed, so we can't
simply add a new argument to pass in the defining class.
Two possible solutions have been proposed to this problem:

* Look up the class through walking the MRO.
  This is potentially expensive, but will be usable if performance is not
  a problem (such as when raising a module-level exception).
* Storing a pointer to the defining class of each slot in a separate table,
  ``__typeslots__`` [#typeslots-mail]_.  This is technically feasible and fast,
  but quite invasive.

Modules affected by this concern also have the option of using
`thread-local state`_ or `PEP 567 context variables`_ as a caching mechanism, or
else defining their own reload-friendly lookup caching scheme.

Solving the issue generally is deferred to a future PEP.

.. _thread-local state: https://docs.python.org/3/c-api/init.html#thread-local-storage-support
.. _PEP 567 context variables: https://docs.python.org/3/c-api/contextvars.html


Specification
=============

Adding module references to heap types
--------------------------------------

A new factory method will be added to the C-API for creating modules::

    PyObject* PyType_FromModuleAndSpec(PyObject *module,
                                       PyType_Spec *spec,
                                       PyObject *bases)

This acts the same as ``PyType_FromSpecWithBases``, and additionally associates
the provided module object with the new type. (In CPython, this will set
``ht_module`` described below.)

Additionally, an accessor, ``PyObject * PyType_GetModule(PyTypeObject *)``
will be provided.
It will return the type's associated module if one is set,
otherwise it will set ``TypeError`` and return NULL.
When given a static type, it will always set ``TypeError`` and return NULL.

To implement this in CPython, the ``PyHeapTypeObject`` struct will get a
new member, ``PyObject *ht_module``, that will store a pointer to the
associated module.
It will be ``NULL`` by default and should not be modified after the type
object is created.

The ``ht_module`` member will not be inherited by subclasses; it needs to be
set using ``PyType_FromSpecWithBases`` for each individual type that needs it.

Usually, creating a class with ``ht_module`` set will create a reference
cycle involving the class and the module.
This is not a problem, as tearing down modules is not a performance-sensitive
operation, and module-level functions typically also create reference cycles.
The existing "set all module globals to None" code that breaks function cycles
through ``f_globals`` will also break the new cycles through ``ht_module``.


Passing the defining class to extension methods
-----------------------------------------------

A new signature flag, ``METH_METHOD``, will be added for use in
``PyMethodDef.ml_flags``. Conceptually, it adds ``defining_class``
to the function signature.
To make the initial implementation easier, the flag can only be used as
``(METH_FASTCALL | METH_KEYWORDS | METH_METHOD)``.
(It can't be used with other flags like ``METH_O`` or bare ``METH_FASTCALL``,
though it may be combined with ``METH_CLASS`` or ``METH_STATIC``).

C functions for methods defined using this flag combination will be called
using a new C signature called ``PyCMethod``::

    PyObject *PyCMethod(PyObject *self,
                        PyTypeObject *defining_class,
                        PyObject *const *args,
                        size_t nargsf,
                        PyObject *kwnames)

Additional combinations like ``(METH_VARARGS | METH_METHOD)`` may be added
in the future (or even in the initial implementation of this PEP).
However, ``METH_METHOD`` should always be an *additional* flag, i.e., the
defining class should only be passed in if needed.

In CPython, a new structure extending ``PyCFunctionObject`` will be added
to hold the extra information::

    typedef struct {
        PyCFunctionObject func;
        PyTypeObject *mm_class; /* Passed as 'defining_class' arg to the C func */
    } PyCMethodObject;

The ``PyCFunction`` implementation will pass ``mm_class`` into a
``PyCMethod`` C function when it finds the ``METH_METHOD`` flag being set.
A new macro ``PyCFunction_GET_CLASS(cls)`` will be added for easier access
to ``mm_class``.

C methods may continue to use the other ``METH_*`` signatures if they do
not require access to their defining class/module.
If ``METH_METHOD`` is not set, casting to ``PyCMethodObject`` is invalid.


Argument Clinic
---------------

To support passing the defining class to methods using Argument Clinic,
a new converter called ``defining_class`` will be added to CPython's Argument
Clinic tool.

Each method may only have one argument using this converter, and it must
appear after ``self``, or, if ``self`` is not used, as the first argument.
The argument will be of type ``PyTypeObject *``.

When used, Argument Clinic will select
``METH_FASTCALL | METH_KEYWORDS | METH_METHOD`` as the calling convention.
The argument will not appear in ``__text_signature__``.

The new converter will initially not be compatible with ``__init__`` and
``__new__`` methods, which cannot use the ``METH_METHOD`` convention.


Helpers
-------

Getting to `per-module state`_ from a heap type is a very common task. To make
this easier, a helper will be added::

    void *PyType_GetModuleState(PyObject *type)

This function takes a heap type and on success, it returns pointer to the state
of the module that the heap type belongs to.

On failure, two scenarios may occur. When a non-type object, or a type without a
module is passed in, ``TypeError`` is set and ``NULL`` returned. If the module
is found, the pointer to the state, which may be ``NULL``, is returned without
setting any exception.


Modules Converted in the Initial Implementation
-----------------------------------------------

To validate the approach, the ``_elementtree`` module will be modified during
the initial implementation.


Summary of API Changes and Additions
====================================

The following will be added to Python C-API:

   * ``PyType_FromModuleAndSpec`` function
   * ``PyType_GetModule`` function
   * ``PyType_GetModuleState`` function
   * ``METH_METHOD`` call flag
   * ``PyCMethod`` function signature

The following additions will be added as CPython implementation details,
and won't be documented:

   * ``PyCFunction_GET_CLASS`` macro
   * ``PyCMethodObject`` struct
   * ``ht_module`` member of ``_heaptypeobject``
   * ``defining_class`` converter in Argument Clinic


Backwards Compatibility
=======================

One new pointer is added to all heap types.
All other changes are adding new functions and structures,
or changes to private implementation details.

Implementation
==============

An initial implementation is available in a Github repository [#gh-repo]_;
a patchset is at [#gh-patch]_.


Possible Future Extensions
==========================

Slot methods
------------

A way of passing defining class (or module state) to slot methods may be
added in the future.

A previous version of this PEP proposed a helper function that would determine
a defining class by searching the MRO for a class that defines a slot to a
particular function. However, this approach would fail if a class is mutated
(which is, for heap types, possible from Python code).
Solving this problem is left to future discussions.


Easy creation of types with module references
---------------------------------------------

It would be possible to add a PEP 489 execution slot type to make
creating heap types significantly easier than calling
``PyType_FromModuleAndSpec``.
This is left to a future PEP.

It may be good to add a good way to create static exception types from the
limited API. Such exception types could be shared between subinterpreters,
but instantiated without needing specific module state.
This is also left to possible future discussions.


Optimization
------------

As proposed here, methods defined with the ``METH_METHOD`` flag only support
one specific signature.

If it turns out that other signatures are needed for performance reasons,
they may be added.


References
==========

.. [#tp-slots] https://docs.python.org/3/c-api/typeobj.html#tp-slots

.. [#typeslots-mail] [Import-SIG] On singleton modules, heap types, and subinterpreters
   (https://mail.python.org/pipermail/import-sig/2015-July/001035.html)

.. [#gh-repo]
   https://github.com/Dormouse759/cpython/tree/pep-c-rebase_newer

.. [#gh-patch]
   https://github.com/Dormouse759/cpython/compare/master...Dormouse759:pep-c-rebase_newer

.. [#pep-590]
   https://www.python.org/dev/peps/pep-0590/


Copyright
=========

This document is placed in the public domain or under the
CC0-1.0-Universal license, whichever is more permissive.


..
   Local Variables:
   mode: indented-text
   indent-tabs-mode: nil
   sentence-end-double-space: t
   fill-column: 70
   coding: utf-8
   End:
````

</details>

<details><summary><b>Step 7 — revision_7</b> (2332 words)</summary>

````text
Abstract
========

This PEP proposes to add a way for CPython extension methods to access context,
such as the state of the modules they are defined in.

This will allow extension methods to use direct pointer dereferences
rather than PyState_FindModule for looking up module state, reducing or
eliminating the performance cost of using module-scoped state over process
global state.

This fixes one of the remaining roadblocks for adoption of :pep:`3121` (Extension
module initialization and finalization) and :pep:`489`
(Multi-phase extension module initialization).

While this PEP takes an additional step towards fully solving the problems that
:pep:`3121` and :pep:`489` started tackling, it does not attempt to resolve *all*
remaining concerns. In particular, access to the module state
from slot methods (``nb_add``, etc) is not solved.


Terminology
===========

Process-Global State
--------------------

C-level static variables. Since this is very low-level
memory storage, it must be managed carefully.

.. _per-module state:

Per-module State
----------------

State local to a module object, allocated dynamically as part of a
module object's initialization. This isolates the state from other
instances of the module (including those in other subinterpreters).

Accessed by ``PyModule_GetState()``.


Static Type
-----------

A type object defined as a C-level static variable, i.e. a compiled-in type
object.

A static type needs to be shared between module instances and has no
information of what module it belongs to.
Static types do not have ``__dict__`` (although their instances might).


Heap Type
---------

A type object created at run time.


Defining Class
--------------

The defining class of a method (either bound or unbound) is the class on which
the method was defined.
A class that merely inherits the method from its base is not the defining class.

For example, ``int`` is the defining class of ``True.to_bytes``,
``True.__floor__`` and ``int.__repr__``.

In C, the defining class is the one defined with the corresponding
``tp_methods`` or "tp slots" [#tp-slots]_ entry.
For methods defined in Python, the defining class is saved in the
``__class__`` closure cell.


C-API
-----

The "Python/C API" as described in Python documentation.
CPython implements the C-API, but other implementations exist.


Rationale
=========

:pep:`489` introduced a new way to initialize extension modules, which brings
several advantages to extensions that implement it:

* The extension modules behave more like their Python counterparts.
* The extension modules can easily support loading into pre-existing
  module objects, which paves the way for extension module support for
  ``runpy`` or for systems that enable extension module reloading.
* Loading multiple modules from the same extension is possible, which
  makes it possible to test module isolation (a key feature for proper
  sub-interpreter support) from a single interpreter.

The biggest hurdle for adoption of :pep:`489` is allowing access to module state
from methods of extension types.
Currently, the way to access this state from extension methods is by looking up
the module via ``PyState_FindModule`` (in contrast to module level functions in
extension modules, which receive a module reference as an argument).
However, ``PyState_FindModule`` queries the thread-local state, making it
relatively costly compared to C level process global access and consequently
deterring module authors from using it.

Also, ``PyState_FindModule`` relies on the assumption that in each
subinterpreter, there is at most one module corresponding to
a given ``PyModuleDef``.  This assumption does not hold for modules that use
:pep:`489`'s multi-phase initialization, so ``PyState_FindModule`` is unavailable
for these modules.

A faster, safer way of accessing module-level state from extension methods
is needed.


Background
===========

The implementation of a Python method may need access to one or more of
the following pieces of information:

* The instance it is called on (``self``)
* The underlying function
* The *defining class*, i. e. the class the method was defined in
* The corresponding module
* The module state

In Python code, the Python-level equivalents may be retrieved as::

    import sys

    class Foo:
        def meth(self):
            instance = self
            module_globals = globals()
            module_object = sys.modules[__name__]  # (1)
            underlying_function = Foo.meth         # (1)
            defining_class = Foo                   # (1)
            defining_class = __class__             # (2)

.. note::

    The defining class is not ``type(self)``, since ``type(self)`` might
    be a subclass of ``Foo``.

The statements marked (1) implicitly rely on name-based lookup via the
function's ``__globals__``: either the ``Foo`` attribute to access the defining
class and Python function object, or ``__name__`` to find the module object in
``sys.modules``.

In Python code, this is feasible, as ``__globals__`` is set appropriately when
the function definition is executed, and even if the namespace has been
manipulated to return a different object, at worst an exception will be raised.

The ``__class__`` closure, (2), is a safer way to get the defining class, but it
still relies on ``__closure__`` being set appropriately.

By contrast, extension methods are typically implemented as normal C functions.
This means that they only have access to their arguments and C level thread-local
and process-global states. Traditionally, many extension modules have stored
their shared state in C-level process globals, causing problems when:

* running multiple initialize/finalize cycles in the same process
* reloading modules (e.g. to test conditional imports)
* loading extension modules in subinterpreters

:pep:`3121` attempted to resolve this by offering the ``PyState_FindModule`` API,
but this still has significant problems when it comes to extension methods
(rather than module level functions):

* it is markedly slower than directly accessing C-level process-global state
* there is still some inherent reliance on process global state that means it
  still doesn't reliably handle module reloading

It's also the case that when looking up a C-level struct such as module state,
supplying an unexpected object layout can crash the interpreter, so it's
significantly more important to ensure that extension methods receive the kind
of object they expect.


Proposal
========

Currently, a bound extension method (``PyCFunction`` or
``PyCFunctionWithKeywords``) receives only ``self``, and (if applicable) the
supplied positional and keyword arguments.

While module-level extension functions already receive access to the defining
module object via their ``self`` argument, methods of extension types don't have
that luxury: they receive the bound instance via ``self``, and hence have no
direct access to the defining class or the module level state.

The additional module level context described above can be made available with
two changes.
Both additions are optional; extension authors need to opt in to start
using them:

* Add a pointer to the module to heap type objects.

* Pass the defining class to the underlying C function.

  In CPython, the defining class is readily available at the time the built-in
  method object (``PyCFunctionObject``) is created, so it can be stored
  in a new struct that extends ``PyCFunctionObject``.

The module state can then be retrieved from the module object via
``PyModule_GetState``.

Note that this proposal implies that any type whose methods need to access
`per-module state`_ must be a heap type, rather than a static type. This is
necessary to support loading multiple module objects from a single
extension: a static type, as a C-level global, has no information about
which module object it belongs to.


Slot methods
------------

The above changes don't cover slot methods, such as ``tp_iter`` or ``nb_add``.

The problem with slot methods is that their C API is fixed, so we can't
simply add a new argument to pass in the defining class.
Two possible solutions have been proposed to this problem:

* Look up the class through walking the MRO.
  This is potentially expensive, but will be usable if performance is not
  a problem (such as when raising a module-level exception).
* Storing a pointer to the defining class of each slot in a separate table,
  ``__typeslots__`` [#typeslots-mail]_.  This is technically feasible and fast,
  but quite invasive.

Modules affected by this concern also have the option of using
`thread-local state`_ or `PEP 567 context variables`_ as a caching mechanism, or
else defining their own reload-friendly lookup caching scheme.

Solving the issue generally is deferred to a future PEP.

.. _thread-local state: https://docs.python.org/3/c-api/init.html#thread-local-storage-support
.. _PEP 567 context variables: https://docs.python.org/3/c-api/contextvars.html


Specification
=============

Adding module references to heap types
--------------------------------------

A new factory method will be added to the C-API for creating modules::

    PyObject* PyType_FromModuleAndSpec(PyObject *module,
                                       PyType_Spec *spec,
                                       PyObject *bases)

This acts the same as ``PyType_FromSpecWithBases``, and additionally associates
the provided module object with the new type. (In CPython, this will set
``ht_module`` described below.)

Additionally, an accessor, ``PyObject * PyType_GetModule(PyTypeObject *)``
will be provided.
It will return the type's associated module if one is set,
otherwise it will set ``TypeError`` and return NULL.
When given a static type, it will always set ``TypeError`` and return NULL.

To implement this in CPython, the ``PyHeapTypeObject`` struct will get a
new member, ``PyObject *ht_module``, that will store a pointer to the
associated module.
It will be ``NULL`` by default and should not be modified after the type
object is created.

The ``ht_module`` member will not be inherited by subclasses; it needs to be
set using ``PyType_FromSpecWithBases`` for each individual type that needs it.

Usually, creating a class with ``ht_module`` set will create a reference
cycle involving the class and the module.
This is not a problem, as tearing down modules is not a performance-sensitive
operation, and module-level functions typically also create reference cycles.
The existing "set all module globals to None" code that breaks function cycles
through ``f_globals`` will also break the new cycles through ``ht_module``.


Passing the defining class to extension methods
-----------------------------------------------

A new signature flag, ``METH_METHOD``, will be added for use in
``PyMethodDef.ml_flags``. Conceptually, it adds ``defining_class``
to the function signature.
To make the initial implementation easier, the flag can only be used as
``(METH_FASTCALL | METH_KEYWORDS | METH_METHOD)``.
(It can't be used with other flags like ``METH_O`` or bare ``METH_FASTCALL``,
though it may be combined with ``METH_CLASS`` or ``METH_STATIC``).

C functions for methods defined using this flag combination will be called
using a new C signature called ``PyCMethod``::

    PyObject *PyCMethod(PyObject *self,
                        PyTypeObject *defining_class,
                        PyObject *const *args,
                        size_t nargsf,
                        PyObject *kwnames)

Additional combinations like ``(METH_VARARGS | METH_METHOD)`` may be added
in the future (or even in the initial implementation of this PEP).
However, ``METH_METHOD`` should always be an *additional* flag, i.e., the
defining class should only be passed in if needed.

In CPython, a new structure extending ``PyCFunctionObject`` will be added
to hold the extra information::

    typedef struct {
        PyCFunctionObject func;
        PyTypeObject *mm_class; /* Passed as 'defining_class' arg to the C func */
    } PyCMethodObject;

The ``PyCFunction`` implementation will pass ``mm_class`` into a
``PyCMethod`` C function when it finds the ``METH_METHOD`` flag being set.
A new macro ``PyCFunction_GET_CLASS(cls)`` will be added for easier access
to ``mm_class``.

C methods may continue to use the other ``METH_*`` signatures if they do
not require access to their defining class/module.
If ``METH_METHOD`` is not set, casting to ``PyCMethodObject`` is invalid.


Argument Clinic
---------------

To support passing the defining class to methods using Argument Clinic,
a new converter called ``defining_class`` will be added to CPython's Argument
Clinic tool.

Each method may only have one argument using this converter, and it must
appear after ``self``, or, if ``self`` is not used, as the first argument.
The argument will be of type ``PyTypeObject *``.

When used, Argument Clinic will select
``METH_FASTCALL | METH_KEYWORDS | METH_METHOD`` as the calling convention.
The argument will not appear in ``__text_signature__``.

The new converter will initially not be compatible with ``__init__`` and
``__new__`` methods, which cannot use the ``METH_METHOD`` convention.


Helpers
-------

Getting to `per-module state`_ from a heap type is a very common task. To make
this easier, a helper will be added::

    void *PyType_GetModuleState(PyObject *type)

This function takes a heap type and on success, it returns pointer to the state
of the module that the heap type belongs to.

On failure, two scenarios may occur. When a non-type object, or a type without a
module is passed in, ``TypeError`` is set and ``NULL`` returned. If the module
is found, the pointer to the state, which may be ``NULL``, is returned without
setting any exception.


Modules Converted in the Initial Implementation
-----------------------------------------------

To validate the approach, the ``_elementtree`` module will be modified during
the initial implementation.


Summary of API Changes and Additions
====================================

The following will be added to Python C-API:

   * ``PyType_FromModuleAndSpec`` function
   * ``PyType_GetModule`` function
   * ``PyType_GetModuleState`` function
   * ``METH_METHOD`` call flag
   * ``PyCMethod`` function signature

The following additions will be added as CPython implementation details,
and won't be documented:

   * ``PyCFunction_GET_CLASS`` macro
   * ``PyCMethodObject`` struct
   * ``ht_module`` member of ``_heaptypeobject``
   * ``defining_class`` converter in Argument Clinic


Backwards Compatibility
=======================

One new pointer is added to all heap types.
All other changes are adding new functions and structures,
or changes to private implementation details.

Implementation
==============

An initial implementation is available in a Github repository [#gh-repo]_;
a patchset is at [#gh-patch]_.


Possible Future Extensions
==========================

Slot methods
------------

A way of passing defining class (or module state) to slot methods may be
added in the future.

A previous version of this PEP proposed a helper function that would determine
a defining class by searching the MRO for a class that defines a slot to a
particular function. However, this approach would fail if a class is mutated
(which is, for heap types, possible from Python code).
Solving this problem is left to future discussions.


Easy creation of types with module references
---------------------------------------------

It would be possible to add a :pep:`489` execution slot type to make
creating heap types significantly easier than calling
``PyType_FromModuleAndSpec``.
This is left to a future PEP.

It may be good to add a good way to create static exception types from the
limited API. Such exception types could be shared between subinterpreters,
but instantiated without needing specific module state.
This is also left to possible future discussions.


Optimization
------------

As proposed here, methods defined with the ``METH_METHOD`` flag only support
one specific signature.

If it turns out that other signatures are needed for performance reasons,
they may be added.


References
==========

.. [#tp-slots] https://docs.python.org/3/c-api/typeobj.html#tp-slots

.. [#typeslots-mail] [Import-SIG] On singleton modules, heap types, and subinterpreters
   (https://mail.python.org/pipermail/import-sig/2015-July/001035.html)

.. [#gh-repo]
   https://github.com/Dormouse759/cpython/tree/pep-c-rebase_newer

.. [#gh-patch]
   https://github.com/Dormouse759/cpython/compare/master...Dormouse759:pep-c-rebase_newer


Copyright
=========

This document is placed in the public domain or under the
CC0-1.0-Universal license, whichever is more permissive.


..
   Local Variables:
   mode: indented-text
   indent-tabs-mode: nil
   sentence-end-double-space: t
   fill-column: 70
   coding: utf-8
   End:
````

</details>

<details><summary><b>Step 8 — final</b> (2315 words)</summary>

````text
Abstract
========

This PEP proposes to add a way for CPython extension methods to access context,
such as the state of the modules they are defined in.

This will allow extension methods to use direct pointer dereferences
rather than PyState_FindModule for looking up module state, reducing or
eliminating the performance cost of using module-scoped state over process
global state.

This fixes one of the remaining roadblocks for adoption of :pep:`3121` (Extension
module initialization and finalization) and :pep:`489`
(Multi-phase extension module initialization).

While this PEP takes an additional step towards fully solving the problems that
:pep:`3121` and :pep:`489` started tackling, it does not attempt to resolve *all*
remaining concerns. In particular, access to the module state
from slot methods (``nb_add``, etc) is not solved.


Terminology
===========

Process-Global State
--------------------

C-level static variables. Since this is very low-level
memory storage, it must be managed carefully.

Per-module State
----------------

State local to a module object, allocated dynamically as part of a
module object's initialization. This isolates the state from other
instances of the module (including those in other subinterpreters).

Accessed by ``PyModule_GetState()``.


Static Type
-----------

A type object defined as a C-level static variable, i.e. a compiled-in type
object.

A static type needs to be shared between module instances and has no
information of what module it belongs to.
Static types do not have ``__dict__`` (although their instances might).


Heap Type
---------

A type object created at run time.


Defining Class
--------------

The defining class of a method (either bound or unbound) is the class on which
the method was defined.
A class that merely inherits the method from its base is not the defining class.

For example, ``int`` is the defining class of ``True.to_bytes``,
``True.__floor__`` and ``int.__repr__``.

In C, the defining class is the one defined with the corresponding
``tp_methods`` or "tp slots" [#tp-slots]_ entry.
For methods defined in Python, the defining class is saved in the
``__class__`` closure cell.


C-API
-----

The "Python/C API" as described in Python documentation.
CPython implements the C-API, but other implementations exist.


Rationale
=========

:pep:`489` introduced a new way to initialize extension modules, which brings
several advantages to extensions that implement it:

* The extension modules behave more like their Python counterparts.
* The extension modules can easily support loading into pre-existing
  module objects, which paves the way for extension module support for
  ``runpy`` or for systems that enable extension module reloading.
* Loading multiple modules from the same extension is possible, which
  makes it possible to test module isolation (a key feature for proper
  sub-interpreter support) from a single interpreter.

The biggest hurdle for adoption of :pep:`489` is allowing access to module state
from methods of extension types.
Currently, the way to access this state from extension methods is by looking up
the module via ``PyState_FindModule`` (in contrast to module level functions in
extension modules, which receive a module reference as an argument).
However, ``PyState_FindModule`` queries the thread-local state, making it
relatively costly compared to C level process global access and consequently
deterring module authors from using it.

Also, ``PyState_FindModule`` relies on the assumption that in each
subinterpreter, there is at most one module corresponding to
a given ``PyModuleDef``.  This assumption does not hold for modules that use
:pep:`489`'s multi-phase initialization, so ``PyState_FindModule`` is unavailable
for these modules.

A faster, safer way of accessing module-level state from extension methods
is needed.


Background
===========

The implementation of a Python method may need access to one or more of
the following pieces of information:

* The instance it is called on (``self``)
* The underlying function
* The *defining class*, i. e. the class the method was defined in
* The corresponding module
* The module state

In Python code, the Python-level equivalents may be retrieved as::

    import sys

    class Foo:
        def meth(self):
            instance = self
            module_globals = globals()
            module_object = sys.modules[__name__]  # (1)
            underlying_function = Foo.meth         # (1)
            defining_class = Foo                   # (1)
            defining_class = __class__             # (2)

.. note::

    The defining class is not ``type(self)``, since ``type(self)`` might
    be a subclass of ``Foo``.

The statements marked (1) implicitly rely on name-based lookup via the
function's ``__globals__``: either the ``Foo`` attribute to access the defining
class and Python function object, or ``__name__`` to find the module object in
``sys.modules``.

In Python code, this is feasible, as ``__globals__`` is set appropriately when
the function definition is executed, and even if the namespace has been
manipulated to return a different object, at worst an exception will be raised.

The ``__class__`` closure, (2), is a safer way to get the defining class, but it
still relies on ``__closure__`` being set appropriately.

By contrast, extension methods are typically implemented as normal C functions.
This means that they only have access to their arguments and C level thread-local
and process-global states. Traditionally, many extension modules have stored
their shared state in C-level process globals, causing problems when:

* running multiple initialize/finalize cycles in the same process
* reloading modules (e.g. to test conditional imports)
* loading extension modules in subinterpreters

:pep:`3121` attempted to resolve this by offering the ``PyState_FindModule`` API,
but this still has significant problems when it comes to extension methods
(rather than module level functions):

* it is markedly slower than directly accessing C-level process-global state
* there is still some inherent reliance on process global state that means it
  still doesn't reliably handle module reloading

It's also the case that when looking up a C-level struct such as module state,
supplying an unexpected object layout can crash the interpreter, so it's
significantly more important to ensure that extension methods receive the kind
of object they expect.


Proposal
========

Currently, a bound extension method (``PyCFunction`` or
``PyCFunctionWithKeywords``) receives only ``self``, and (if applicable) the
supplied positional and keyword arguments.

While module-level extension functions already receive access to the defining
module object via their ``self`` argument, methods of extension types don't have
that luxury: they receive the bound instance via ``self``, and hence have no
direct access to the defining class or the module level state.

The additional module level context described above can be made available with
two changes.
Both additions are optional; extension authors need to opt in to start
using them:

* Add a pointer to the module to heap type objects.

* Pass the defining class to the underlying C function.

  In CPython, the defining class is readily available at the time the built-in
  method object (``PyCFunctionObject``) is created, so it can be stored
  in a new struct that extends ``PyCFunctionObject``.

The module state can then be retrieved from the module object via
``PyModule_GetState``.

Note that this proposal implies that any type whose methods need to access
`per-module state`_ must be a heap type, rather than a static type. This is
necessary to support loading multiple module objects from a single
extension: a static type, as a C-level global, has no information about
which module object it belongs to.


Slot methods
------------

The above changes don't cover slot methods, such as ``tp_iter`` or ``nb_add``.

The problem with slot methods is that their C API is fixed, so we can't
simply add a new argument to pass in the defining class.
Two possible solutions have been proposed to this problem:

* Look up the class through walking the MRO.
  This is potentially expensive, but will be usable if performance is not
  a problem (such as when raising a module-level exception).
* Storing a pointer to the defining class of each slot in a separate table,
  ``__typeslots__`` [#typeslots-mail]_.  This is technically feasible and fast,
  but quite invasive.

Modules affected by this concern also have the option of using
`thread-local state`_ or `PEP 567 context variables`_ as a caching mechanism, or
else defining their own reload-friendly lookup caching scheme.

Solving the issue generally is deferred to a future PEP.

.. _thread-local state: https://docs.python.org/3/c-api/init.html#thread-local-storage-support
.. _PEP 567 context variables: https://docs.python.org/3/c-api/contextvars.html


Specification
=============

Adding module references to heap types
--------------------------------------

A new factory method will be added to the C-API for creating modules::

    PyObject* PyType_FromModuleAndSpec(PyObject *module,
                                       PyType_Spec *spec,
                                       PyObject *bases)

This acts the same as ``PyType_FromSpecWithBases``, and additionally associates
the provided module object with the new type. (In CPython, this will set
``ht_module`` described below.)

Additionally, an accessor, ``PyObject * PyType_GetModule(PyTypeObject *)``
will be provided.
It will return the type's associated module if one is set,
otherwise it will set ``TypeError`` and return NULL.
When given a static type, it will always set ``TypeError`` and return NULL.

To implement this in CPython, the ``PyHeapTypeObject`` struct will get a
new member, ``PyObject *ht_module``, that will store a pointer to the
associated module.
It will be ``NULL`` by default and should not be modified after the type
object is created.

The ``ht_module`` member will not be inherited by subclasses; it needs to be
set using ``PyType_FromSpecWithBases`` for each individual type that needs it.

Usually, creating a class with ``ht_module`` set will create a reference
cycle involving the class and the module.
This is not a problem, as tearing down modules is not a performance-sensitive
operation, and module-level functions typically also create reference cycles.
The existing "set all module globals to None" code that breaks function cycles
through ``f_globals`` will also break the new cycles through ``ht_module``.


Passing the defining class to extension methods
-----------------------------------------------

A new signature flag, ``METH_METHOD``, will be added for use in
``PyMethodDef.ml_flags``. Conceptually, it adds ``defining_class``
to the function signature.
To make the initial implementation easier, the flag can only be used as
``(METH_FASTCALL | METH_KEYWORDS | METH_METHOD)``.
(It can't be used with other flags like ``METH_O`` or bare ``METH_FASTCALL``,
though it may be combined with ``METH_CLASS`` or ``METH_STATIC``).

C functions for methods defined using this flag combination will be called
using a new C signature called ``PyCMethod``::

    PyObject *PyCMethod(PyObject *self,
                        PyTypeObject *defining_class,
                        PyObject *const *args,
                        size_t nargsf,
                        PyObject *kwnames)

Additional combinations like ``(METH_VARARGS | METH_METHOD)`` may be added
in the future (or even in the initial implementation of this PEP).
However, ``METH_METHOD`` should always be an *additional* flag, i.e., the
defining class should only be passed in if needed.

In CPython, a new structure extending ``PyCFunctionObject`` will be added
to hold the extra information::

    typedef struct {
        PyCFunctionObject func;
        PyTypeObject *mm_class; /* Passed as 'defining_class' arg to the C func */
    } PyCMethodObject;

The ``PyCFunction`` implementation will pass ``mm_class`` into a
``PyCMethod`` C function when it finds the ``METH_METHOD`` flag being set.
A new macro ``PyCFunction_GET_CLASS(cls)`` will be added for easier access
to ``mm_class``.

C methods may continue to use the other ``METH_*`` signatures if they do
not require access to their defining class/module.
If ``METH_METHOD`` is not set, casting to ``PyCMethodObject`` is invalid.


Argument Clinic
---------------

To support passing the defining class to methods using Argument Clinic,
a new converter called ``defining_class`` will be added to CPython's Argument
Clinic tool.

Each method may only have one argument using this converter, and it must
appear after ``self``, or, if ``self`` is not used, as the first argument.
The argument will be of type ``PyTypeObject *``.

When used, Argument Clinic will select
``METH_FASTCALL | METH_KEYWORDS | METH_METHOD`` as the calling convention.
The argument will not appear in ``__text_signature__``.

The new converter will initially not be compatible with ``__init__`` and
``__new__`` methods, which cannot use the ``METH_METHOD`` convention.


Helpers
-------

Getting to `per-module state`_ from a heap type is a very common task. To make
this easier, a helper will be added::

    void *PyType_GetModuleState(PyObject *type)

This function takes a heap type and on success, it returns pointer to the state
of the module that the heap type belongs to.

On failure, two scenarios may occur. When a non-type object, or a type without a
module is passed in, ``TypeError`` is set and ``NULL`` returned. If the module
is found, the pointer to the state, which may be ``NULL``, is returned without
setting any exception.


Modules Converted in the Initial Implementation
-----------------------------------------------

To validate the approach, the ``_elementtree`` module will be modified during
the initial implementation.


Summary of API Changes and Additions
====================================

The following will be added to Python C-API:

   * ``PyType_FromModuleAndSpec`` function
   * ``PyType_GetModule`` function
   * ``PyType_GetModuleState`` function
   * ``METH_METHOD`` call flag
   * ``PyCMethod`` function signature

The following additions will be added as CPython implementation details,
and won't be documented:

   * ``PyCFunction_GET_CLASS`` macro
   * ``PyCMethodObject`` struct
   * ``ht_module`` member of ``_heaptypeobject``
   * ``defining_class`` converter in Argument Clinic


Backwards Compatibility
=======================

One new pointer is added to all heap types.
All other changes are adding new functions and structures,
or changes to private implementation details.

Implementation
==============

An initial implementation is available in a Github repository [#gh-repo]_;
a patchset is at [#gh-patch]_.


Possible Future Extensions
==========================

Slot methods
------------

A way of passing defining class (or module state) to slot methods may be
added in the future.

A previous version of this PEP proposed a helper function that would determine
a defining class by searching the MRO for a class that defines a slot to a
particular function. However, this approach would fail if a class is mutated
(which is, for heap types, possible from Python code).
Solving this problem is left to future discussions.


Easy creation of types with module references
---------------------------------------------

It would be possible to add a :pep:`489` execution slot type to make
creating heap types significantly easier than calling
``PyType_FromModuleAndSpec``.
This is left to a future PEP.

It may be good to add a good way to create static exception types from the
limited API. Such exception types could be shared between subinterpreters,
but instantiated without needing specific module state.
This is also left to possible future discussions.


Optimization
------------

As proposed here, methods defined with the ``METH_METHOD`` flag only support
one specific signature.

If it turns out that other signatures are needed for performance reasons,
they may be added.


References
==========

.. [#tp-slots] https://docs.python.org/3/c-api/typeobj.html#tp-slots

.. [#typeslots-mail] [Import-SIG] On singleton modules, heap types, and subinterpreters
   (https://mail.python.org/pipermail/import-sig/2015-July/001035.html)

.. [#gh-repo]
   https://github.com/Dormouse759/cpython/tree/pep-c-rebase_newer

.. [#gh-patch]
   https://github.com/Dormouse759/cpython/compare/master...Dormouse759:pep-c-rebase_newer


Copyright
=========

This document is placed in the public domain or under the
CC0-1.0-Universal license, whichever is more permissive.
````

</details>
