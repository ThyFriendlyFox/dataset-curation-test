# 3. Python PEP: The Locked Buffer Interface

`C-pep_pep-0298` · [full/C_github_commits_9step](README.md)

Source: <https://github.com/python/peps/blob/545c670f1e986162eb7161d63c944108e504bd09/peps/pep-0298.rst> · License: Public domain / CC0-1.0 (PEP text) · 23 commits touching the file; 15 distinct versions

| step | name | words | citations | similarity to final | provenance |
|---|---|---|---|---|---|
| 0 | title | 4 | 0 | 0.00 | source_title |
| 1 | revision_1 | 588 | 3 | 0.53 | commit 135eff8437 (2002-07-29) |
| 2 | revision_2 | 647 | 3 | 0.53 | commit 10d37607c9 (2002-07-30) |
| 3 | revision_3 | 751 | 3 | 0.74 | commit 419b7d99fb (2002-07-31) |
| 4 | revision_4 | 1034 | 3 | 0.94 | commit 7fadff7e8a (2002-08-01) |
| 5 | revision_5 | 1059 | 3 | 0.96 | commit 04a6af2ab1 (2016-07-11) |
| 6 | revision_6 | 1073 | 3 | 0.99 | commit f9a66fe511 (2017-02-06) |
| 7 | revision_7 | 1066 | 2 | 0.99 | commit 113e490701 (2022-01-21) |
| 8 | final | 1054 | 2 | 1.00 | commit 6aa0b6619c (2025-02-01) |

<details><summary><b>Step 0 — title</b> (4 words)</summary>

````text
The Locked Buffer Interface
````

</details>

<details><summary><b>Step 1 — revision_1</b> (588 words)</summary>

````text
Abstract

    This PEP proposes an extension to the buffer interface called the
    'safe buffer interface'.

    The safe buffer interface fixes the flaws of the 'old' buffer
    interface as defined in Python versions up to and including 2.2,
    see [1]:

        The lifetime of the retrieved pointer is clearly defined.

        The buffer size is returned as a 'size_t' data type, which
        allows access to large buffers on platforms where sizeof(int)
        != sizeof(void *).


Specification

    The safe buffer interface exposes new functions which return the
    size and the pointer to the internal memory block of any python
    object which chooses to implement this interface.

    The size and pointer returned must be valid as long as the object
    is alive (has a positive reference count).  So, only objects which
    never reallocate or resize the memory block are allowed to
    implement this interface.

    The safe buffer interface omits the memory segment model which is
    present in the old buffer interface - only a single memory block
    can be exposed.


Implementation

    Define a new flag in Include/object.h:

        /* PyBufferProcs contains bf_getsafereadbuffer
           and bf_getsafewritebuffer */
        #define Py_TPFLAGS_HAVE_GETSAFEBUFFER (1L<<15)


    This flag would be included in Py_TPFLAGS_DEFAULT:

        #define Py_TPFLAGS_DEFAULT  ( \
                             ....
                             Py_TPFLAGS_HAVE_GETSAFEBUFFER | \
                             ....
                            0)


    Extend the PyBufferProcs structure by new fields in
    Include/object.h:

        typedef size_t (*getsafereadbufferproc)(PyObject *, void **);
        typedef size_t (*getsafewritebufferproc)(PyObject *, void **);

        typedef struct {
                getreadbufferproc bf_getreadbuffer;
                getwritebufferproc bf_getwritebuffer;
                getsegcountproc bf_getsegcount;
                getcharbufferproc bf_getcharbuffer;
                /* safe buffer interface functions */
                getsafereadbufferproc bf_getsafereadbufferproc;
                getsafewritebufferproc bf_getsafewritebufferproc;
        } PyBufferProcs;


    The new fields are present if the Py_TPFLAGS_HAVE_GETSAFEBUFFER
    flag is set in the object's type.

    The Py_TPFLAGS_HAVE_GETSAFEBUFFER flag implies the
    Py_TPFLAGS_HAVE_GETCHARBUFFER flag.

    The getsafereadbufferproc and getsafewritebufferproc functions
    return the size in bytes of the memory block on success, and fill
    in the passed void * pointer on success.  If these functions fail
    - either because an error occurs or no memory block is exposed -
    they must set the void * pointer to NULL and raise an exception.
    The return value is undefined in these cases and should not be
    used.

    Usually the getsafewritebufferproc and getsafereadbufferproc
    functions aren't called directly, they are called through
    convenience functions declared in Include/abstract.h:

        int PyObject_AsSafeReadBuffer(PyObject *obj,
                                      void **buffer,
                                      size_t *buffer_len);

        int PyObject_AsSafeWriteBuffer(PyObject *obj,
                                       void **buffer,
                                       size_t *buffer_len);

    These functions return 0 on success, set buffer to the memory
    location and buffer_len to the length of the memory block in
    bytes. On failure, or if the safe buffer interface is not
    implemented by obj, they return -1 and set an exception.


Backward Compatibility

    The size of the PyBufferProcs structure changes if this proposal
    is implemented, but the type's tp_flags slot can be used to
    determine if the additional fields are present.


Reference Implementation

    Will be uploaded to the SourceForge patch manager by the author.


Additional Notes/Comments

    Python strings, Unicode strings, mmap objects, and maybe other
    types would expose the safe buffer interface, but the array type
    would *not*, because its memory block may be reallocated during
    its lifetime.


Community Feedback

    Greg Ewing doubts the safe buffer interface is needed at all, he
    thinks the normal buffer interface could be used if the pointer is
    (re)fetched each time it's used.

    Neil Hodgson wants to expose pointers to memory blocks with
    limited lifetime: do some kind of lock operation on the object,
    retrieve the pointer, use it, and unlock the object again.  On the
    other hand, locking may lead to deadlocks.


References

    [1] The buffer interface
        http://mail.python.org/pipermail/python-dev/2000-October/009974.html

    [2] The Buffer Problem
        http://www.python.org/peps/pep-0296.html


Copyright

    This document has been placed in the public domain.



Local Variables:
mode: indented-text
indent-tabs-mode: nil
sentence-end-double-space: t
fill-column: 70
End:
````

</details>

<details><summary><b>Step 2 — revision_2</b> (647 words)</summary>

````text
Abstract

    This PEP proposes an extension to the buffer interface called the
    'fixed buffer interface'.

    The fixed buffer interface fixes the flaws of the 'old' buffer
    interface as defined in Python versions up to and including 2.2,
    see [1]:

        The lifetime of the retrieved pointer is clearly defined.

        The buffer size is returned as a 'size_t' data type, which
        allows access to large buffers on platforms where sizeof(int)
        != sizeof(void *).


Specification

    The fixed buffer interface exposes new functions which return the
    size and the pointer to the internal memory block of any python
    object which chooses to implement this interface.

    The size and pointer returned must be valid as long as the object
    is alive (has a positive reference count).  So, only objects which
    never reallocate or resize the memory block are allowed to
    implement this interface.

    The fixed buffer interface omits the memory segment model which is
    present in the old buffer interface - only a single memory block
    can be exposed.


Implementation

    Define a new flag in Include/object.h:

        /* PyBufferProcs contains bf_getfixedreadbuffer
           and bf_getfixedwritebuffer */
        #define Py_TPFLAGS_HAVE_GETFIXEDBUFFER (1L<<15)


    This flag would be included in Py_TPFLAGS_DEFAULT:

        #define Py_TPFLAGS_DEFAULT  ( \
                             ....
                             Py_TPFLAGS_HAVE_GETFIXEDBUFFER | \
                             ....
                            0)


    Extend the PyBufferProcs structure by new fields in
    Include/object.h:

        typedef size_t (*getfixedreadbufferproc)(PyObject *, void **);
        typedef size_t (*getfixedwritebufferproc)(PyObject *, void **);

        typedef struct {
                getreadbufferproc bf_getreadbuffer;
                getwritebufferproc bf_getwritebuffer;
                getsegcountproc bf_getsegcount;
                getcharbufferproc bf_getcharbuffer;
                /* fixed buffer interface functions */
                getfixedreadbufferproc bf_getfixedreadbufferproc;
                getfixedwritebufferproc bf_getfixedwritebufferproc;
        } PyBufferProcs;


    The new fields are present if the Py_TPFLAGS_HAVE_GETFIXEDBUFFER
    flag is set in the object's type.

    The Py_TPFLAGS_HAVE_GETFIXEDBUFFER flag implies the
    Py_TPFLAGS_HAVE_GETCHARBUFFER flag.

    The getfixedreadbufferproc and getfixedwritebufferproc functions
    return the size in bytes of the memory block on success, and fill
    in the passed void * pointer on success.  If these functions fail
    - either because an error occurs or no memory block is exposed -
    they must set the void * pointer to NULL and raise an exception.
    The return value is undefined in these cases and should not be
    used.

    Usually the getfixedwritebufferproc and getfixedreadbufferproc
    functions aren't called directly, they are called through
    convenience functions declared in Include/abstract.h:

        int PyObject_AsFixedReadBuffer(PyObject *obj,
                                      void **buffer,
                                      size_t *buffer_len);

        int PyObject_AsFixedWriteBuffer(PyObject *obj,
                                       void **buffer,
                                       size_t *buffer_len);

    These functions return 0 on success, set buffer to the memory
    location and buffer_len to the length of the memory block in
    bytes. On failure, or if the fixed buffer interface is not
    implemented by obj, they return -1 and set an exception.


Backward Compatibility

    The size of the PyBufferProcs structure changes if this proposal
    is implemented, but the type's tp_flags slot can be used to
    determine if the additional fields are present.


Reference Implementation

    Will be uploaded to the SourceForge patch manager by the author.


Additional Notes/Comments

    Python strings, Unicode strings, mmap objects, and maybe other
    types would expose the fixed buffer interface, but the array type
    would *not*, because its memory block may be reallocated during
    its lifetime.


Community Feedback

    Greg Ewing doubts the fixed buffer interface is needed at all, he
    thinks the normal buffer interface could be used if the pointer is
    (re)fetched each time it's used.  This seems to be dangerous,
    because even innocent looking calls to the Python API like
    Py_DECREF() may trigger execution of arbitrary Python code.

    Neil Hodgson wants to expose pointers to memory blocks with
    limited lifetime: do some kind of lock operation on the object,
    retrieve the pointer, use it, and unlock the object again.  While
    the author sees the need for this, it cannot be addressed by this
    proposal.  Beeing required to call a function after not using the
    pointer received by the getfixedbufferprocs seems too error prone.


Credits

    Scott Gilbert came up with the name 'fixed buffer interface'.


References

    [1] The buffer interface
        http://mail.python.org/pipermail/python-dev/2000-October/009974.html

    [2] The Buffer Problem
        http://www.python.org/peps/pep-0296.html


Copyright

    This document has been placed in the public domain.



Local Variables:
mode: indented-text
indent-tabs-mode: nil
sentence-end-double-space: t
fill-column: 70
End:
````

</details>

<details><summary><b>Step 3 — revision_3</b> (751 words)</summary>

````text
Abstract

    This PEP proposes an extension to the buffer interface called the
    'fixed buffer interface'.

    The fixed buffer interface fixes the flaws of the 'old' buffer
    interface [1] as defined in Python versions up to and including
    2.2, and has the following semantics:

        The lifetime of the retrieved pointer is clearly defined and
        controlled by the client.

        The buffer size is returned as a 'size_t' data type, which
        allows access to large buffers on platforms where sizeof(int)
        != sizeof(void *).

    (Guido comments: This second sounds like a change we could also
    make to the "old" buffer interface, if we introduce another flag
    bit that's *not* part of the default flags.)


Specification

    The fixed buffer interface exposes new functions which return the
    size and the pointer to the internal memory block of any python
    object which chooses to implement this interface.

    Retrieving a buffer from an object puts this object in a locked
    state during which the buffer may not be freed, resized, or
    reallocated.

    The object must be unlocked again by releasing the buffer if it's
    no longer used by calling another function in the fixed buffer
    interface.  If the object never resizes or reallocates the buffer
    during it's lifetime, this function may be NULL. Failure to call
    this function (if it is != NULL) is a programming error and may
    have unexpected results.

    The fixed buffer interface omits the memory segment model which is
    present in the old buffer interface - only a single memory block
    can be exposed.


Implementation

    Define a new flag in Include/object.h:

        /* PyBufferProcs contains bf_acquirefixedreadbuffer,
           bf_acquirefixedwritebuffer, and bf_releasefixedbuffer */
        #define Py_TPFLAGS_HAVE_FIXEDBUFFER (1L<<15)


    This flag would be included in Py_TPFLAGS_DEFAULT:

        #define Py_TPFLAGS_DEFAULT  ( \
                             ....
                             Py_TPFLAGS_HAVE_FIXEDBUFFER | \
                             ....
                            0)


    Extend the PyBufferProcs structure by new fields in
    Include/object.h:

        typedef size_t (*acquirefixedreadbufferproc)(PyObject *,
                                                     const void **);
        typedef size_t (*acquirefixedwritebufferproc)(PyObject *,
                                                      void **);
        typedef void (*releasefixedbufferproc)(PyObject *);

        typedef struct {
                getreadbufferproc bf_getreadbuffer;
                getwritebufferproc bf_getwritebuffer;
                getsegcountproc bf_getsegcount;
                getcharbufferproc bf_getcharbuffer;
                /* fixed buffer interface functions */
                acquirefixedreadbufferproc bf_acquirefixedreadbuffer;
                acquirefixedwritebufferproc bf_acquirefixedwritebuffer;
                releasefixedbufferproc bf_releasefixedbuffer;
        } PyBufferProcs;


    The new fields are present if the Py_TPFLAGS_HAVE_FIXEDBUFFER
    flag is set in the object's type.

    The Py_TPFLAGS_HAVE_FIXEDBUFFER flag implies the
    Py_TPFLAGS_HAVE_GETCHARBUFFER flag.

    The acquirefixedreadbufferproc and acquirefixedwritebufferproc
    functions return the size in bytes of the memory block on success,
    and fill in the passed void * pointer on success.  If these
    functions fail - either because an error occurs or no memory block
    is exposed - they must set the void * pointer to NULL and raise an
    exception.  The return value is undefined in these cases and
    should not be used.

    If calls to these functions succeed, eventually the buffer must be
    released by a call to the releasefixedbufferproc, supplying the
    original object as argument.  The releasefixedbufferproc cannot
    fail.

    Usually these functions aren't called directly, they are called
    through convenience functions declared in Include/abstract.h:

        int PyObject_AquireFixedReadBuffer(PyObject *obj,
                                           const void **buffer,
                                           size_t *buffer_len);

        int PyObject_AcquireFixedWriteBuffer(PyObject *obj,
                                             void **buffer,
                                             size_t *buffer_len);

        void PyObject_ReleaseFixedBuffer(PyObject *obj);

    The former two functions return 0 on success, set buffer to the
    memory location and buffer_len to the length of the memory block
    in bytes. On failure, or if the fixed buffer interface is not
    implemented by obj, they return -1 and set an exception.

    The latter function doesn't return anything, and cannot fail.


Backward Compatibility

    The size of the PyBufferProcs structure changes if this proposal
    is implemented, but the type's tp_flags slot can be used to
    determine if the additional fields are present.


Reference Implementation

    Will be uploaded to the SourceForge patch manager by the author.


Additional Notes/Comments

    Python strings, Unicode strings, mmap objects, and array objects
    would expose the fixed buffer interface.


Community Feedback

    Greg Ewing doubts the fixed buffer interface is needed at all, he
    thinks the normal buffer interface could be used if the pointer is
    (re)fetched each time it's used.  This seems to be dangerous,
    because even innocent looking calls to the Python API like
    Py_DECREF() may trigger execution of arbitrary Python code.

    The first version of this proposal didn't have the release
    function, but it turned out that this would have been too
    restrictive: mmap and array objects wouldn't have been able to
    implement it, because mmap objects can be closed anytime if not
    locked, and array objects could resize or reallocate the buffer.


Credits

    Scott Gilbert came up with the name 'fixed buffer interface'.


References

    [1] The buffer interface
        http://mail.python.org/pipermail/python-dev/2000-October/009974.html

    [2] The Buffer Problem
        http://www.python.org/peps/pep-0296.html


Copyright

    This document has been placed in the public domain.



Local Variables:
mode: indented-text
indent-tabs-mode: nil
sentence-end-double-space: t
fill-column: 70
End:
````

</details>

<details><summary><b>Step 4 — revision_4</b> (1034 words)</summary>

````text
Abstract

    This PEP proposes an extension to the buffer interface called the
    'locked buffer interface'.

    The locked buffer interface avoids the flaws of the 'old' buffer
    interface [1] as defined in Python versions up to and including
    2.2, and has the following semantics:

        The lifetime of the retrieved pointer is clearly defined and
        controlled by the client.

        The buffer size is returned as a 'size_t' data type, which
        allows access to large buffers on platforms where sizeof(int)
        != sizeof(void *).

    (Guido comments: This second sounds like a change we could also
    make to the "old" buffer interface, if we introduce another flag
    bit that's *not* part of the default flags.)


Specification

    The locked buffer interface exposes new functions which return the
    size and the pointer to the internal memory block of any python
    object which chooses to implement this interface.

    Retrieving a buffer from an object puts this object in a locked
    state during which the buffer may not be freed, resized, or
    reallocated.

    The object must be unlocked again by releasing the buffer if it's
    no longer used by calling another function in the locked buffer
    interface.  If the object never resizes or reallocates the buffer
    during it's lifetime, this function may be NULL.  Failure to call
    this function (if it is != NULL) is a programming error and may
    have unexpected results.

    The locked buffer interface omits the memory segment model which
    is present in the old buffer interface - only a single memory
    block can be exposed.


Implementation

    Define a new flag in Include/object.h:

        /* PyBufferProcs contains bf_acquirelockedreadbuffer,
           bf_acquirelockedwritebuffer, and bf_releaselockedbuffer */
        #define Py_TPFLAGS_HAVE_LOCKEDBUFFER (1L<<15)


    This flag would be included in Py_TPFLAGS_DEFAULT:

        #define Py_TPFLAGS_DEFAULT  ( \
                             ....
                             Py_TPFLAGS_HAVE_LOCKEDBUFFER | \
                             ....
                            0)


    Extend the PyBufferProcs structure by new fields in
    Include/object.h:

        typedef size_t (*acquirelockedreadbufferproc)(PyObject *,
                                                      const void **);
        typedef size_t (*acquirelockedwritebufferproc)(PyObject *,
                                                       void **);
        typedef void (*releaselockedbufferproc)(PyObject *);

        typedef struct {
            getreadbufferproc bf_getreadbuffer;
            getwritebufferproc bf_getwritebuffer;
            getsegcountproc bf_getsegcount;
            getcharbufferproc bf_getcharbuffer;
            /* locked buffer interface functions */
            acquirelockedreadbufferproc bf_acquirelockedreadbuffer;
            acquirelockedwritebufferproc bf_acquirelockedwritebuffer;
            releaselockedbufferproc bf_releaselockedbuffer;
        } PyBufferProcs;


    The new fields are present if the Py_TPFLAGS_HAVE_LOCKEDBUFFER
    flag is set in the object's type.

    The Py_TPFLAGS_HAVE_LOCKEDBUFFER flag implies the
    Py_TPFLAGS_HAVE_GETCHARBUFFER flag.

    The acquirelockedreadbufferproc and acquirelockedwritebufferproc
    functions return the size in bytes of the memory block on success,
    and fill in the passed void * pointer on success.  If these
    functions fail - either because an error occurs or no memory block
    is exposed - they must set the void * pointer to NULL and raise an
    exception.  The return value is undefined in these cases and
    should not be used.

    If calls to these functions succeed, eventually the buffer must be
    released by a call to the releaselockedbufferproc, supplying the
    original object as argument.  The releaselockedbufferproc cannot
    fail.  For objects that actually maintain an internal lock count
    it would be a fatal error if the releaselockedbufferproc function
    would be called too often, leading to a negative lock count.

    Similar to the 'old' buffer interface, any of these functions may
    be set to NULL, but it is strongly recommended to implement the
    releaselockedbufferproc function (even if it does nothing) if any
    of the acquireread/writelockedbufferproc functions are
    implemented, to discourage extension writers from checking for a
    NULL value and not calling it.

    These functions aren't supposed to be called directly, they are
    called through convenience functions declared in
    Include/abstract.h:

        int PyObject_AquireLockedReadBuffer(PyObject *obj,
                                            const void **buffer,
                                            size_t *buffer_len);

        int PyObject_AcquireLockedWriteBuffer(PyObject *obj,
                                              void **buffer,
                                              size_t *buffer_len);

        void PyObject_ReleaseLockedBuffer(PyObject *obj);

    The former two functions return 0 on success, set buffer to the
    memory location and buffer_len to the length of the memory block
    in bytes. On failure, or if the locked buffer interface is not
    implemented by obj, they return -1 and set an exception.

    The latter function doesn't return anything, and cannot fail.


Backward Compatibility

    The size of the PyBufferProcs structure changes if this proposal
    is implemented, but the type's tp_flags slot can be used to
    determine if the additional fields are present.


Reference Implementation

    Will be uploaded to the SourceForge patch manager by the author.


Additional Notes/Comments

    Python strings, unicode strings, mmap objects, and array objects
    would expose the locked buffer interface.

    mmap and array objects would actually enter a locked state while
    the buffer is active, this is not needed for strings and unicode
    objects.  Resizing locked array objects is not allowed and will
    raise an exception. Whether closing a locked mmap object is an
    error or will only be deferred until the lock count reaches zero
    is an implementation detail.

    Guido recommends:

        But I'm still very concerned that if most built-in types
        (e.g. strings, bytes) don't implement the release
        functionality, it's too easy for an extension to seem to work
        while forgetting to release the buffer.

        I recommend that at least some built-in types implement the
        acquire/release functionality with a counter, and assert that
        the counter is zero when the object is deleted -- if the
        assert fails, someone DECREF'ed their reference to the object
        without releasing it.  (The rule should be that you must own a
        reference to the object while you've aquired the object.)

        For strings that might be impractical because the string
        object would have to grow 4 bytes to hold the counter; but the
        new bytes object (PEP 296) could easily implement the counter,
        and the array object too -- that way there will be plenty of
        opportunity to test proper use of the protocol.


Community Feedback

    Greg Ewing doubts the locked buffer interface is needed at all, he
    thinks the normal buffer interface could be used if the pointer is
    (re)fetched each time it's used.  This seems to be dangerous,
    because even innocent looking calls to the Python API like
    Py_DECREF() may trigger execution of arbitrary Python code.

    The first version of this proposal didn't have the release
    function, but it turned out that this would have been too
    restrictive: mmap and array objects wouldn't have been able to
    implement it, because mmap objects can be closed anytime if not
    locked, and array objects could resize or reallocate the buffer.


Credits


References

    [1] The buffer interface
        http://mail.python.org/pipermail/python-dev/2000-October/009974.html

    [2] The Buffer Problem
        http://www.python.org/peps/pep-0296.html


Copyright

    This document has been placed in the public domain.



Local Variables:
mode: indented-text
indent-tabs-mode: nil
sentence-end-double-space: t
fill-column: 70
End:
````

</details>

<details><summary><b>Step 5 — revision_5</b> (1059 words)</summary>

````text
Abstract

    This PEP proposes an extension to the buffer interface called the
    'locked buffer interface'.

    The locked buffer interface avoids the flaws of the 'old' buffer
    interface [1] as defined in Python versions up to and including
    2.2, and has the following semantics:

        The lifetime of the retrieved pointer is clearly defined and
        controlled by the client.

        The buffer size is returned as a 'size_t' data type, which
        allows access to large buffers on platforms where sizeof(int)
        != sizeof(void *).

    (Guido comments: This second sounds like a change we could also
    make to the "old" buffer interface, if we introduce another flag
    bit that's *not* part of the default flags.)


Specification

    The locked buffer interface exposes new functions which return the
    size and the pointer to the internal memory block of any python
    object which chooses to implement this interface.

    Retrieving a buffer from an object puts this object in a locked
    state during which the buffer may not be freed, resized, or
    reallocated.

    The object must be unlocked again by releasing the buffer if it's
    no longer used by calling another function in the locked buffer
    interface.  If the object never resizes or reallocates the buffer
    during its lifetime, this function may be NULL.  Failure to call
    this function (if it is != NULL) is a programming error and may
    have unexpected results.

    The locked buffer interface omits the memory segment model which
    is present in the old buffer interface - only a single memory
    block can be exposed.

    The memory blocks can be accessed without holding the global
    interpreter lock.


Implementation

    Define a new flag in Include/object.h:

        /* PyBufferProcs contains bf_acquirelockedreadbuffer,
           bf_acquirelockedwritebuffer, and bf_releaselockedbuffer */
        #define Py_TPFLAGS_HAVE_LOCKEDBUFFER (1L<<15)


    This flag would be included in Py_TPFLAGS_DEFAULT:

        #define Py_TPFLAGS_DEFAULT  ( \
                             ....
                             Py_TPFLAGS_HAVE_LOCKEDBUFFER | \
                             ....
                            0)


    Extend the PyBufferProcs structure by new fields in
    Include/object.h:

        typedef size_t (*acquirelockedreadbufferproc)(PyObject *,
                                                      const void **);
        typedef size_t (*acquirelockedwritebufferproc)(PyObject *,
                                                       void **);
        typedef void (*releaselockedbufferproc)(PyObject *);

        typedef struct {
            getreadbufferproc bf_getreadbuffer;
            getwritebufferproc bf_getwritebuffer;
            getsegcountproc bf_getsegcount;
            getcharbufferproc bf_getcharbuffer;
            /* locked buffer interface functions */
            acquirelockedreadbufferproc bf_acquirelockedreadbuffer;
            acquirelockedwritebufferproc bf_acquirelockedwritebuffer;
            releaselockedbufferproc bf_releaselockedbuffer;
        } PyBufferProcs;


    The new fields are present if the Py_TPFLAGS_HAVE_LOCKEDBUFFER
    flag is set in the object's type.

    The Py_TPFLAGS_HAVE_LOCKEDBUFFER flag implies the
    Py_TPFLAGS_HAVE_GETCHARBUFFER flag.

    The acquirelockedreadbufferproc and acquirelockedwritebufferproc
    functions return the size in bytes of the memory block on success,
    and fill in the passed void * pointer on success.  If these
    functions fail - either because an error occurs or no memory block
    is exposed - they must set the void * pointer to NULL and raise an
    exception.  The return value is undefined in these cases and
    should not be used.

    If calls to these functions succeed, eventually the buffer must be
    released by a call to the releaselockedbufferproc, supplying the
    original object as argument.  The releaselockedbufferproc cannot
    fail.  For objects that actually maintain an internal lock count
    it would be a fatal error if the releaselockedbufferproc function
    would be called too often, leading to a negative lock count.

    Similar to the 'old' buffer interface, any of these functions may
    be set to NULL, but it is strongly recommended to implement the
    releaselockedbufferproc function (even if it does nothing) if any
    of the acquireread/writelockedbufferproc functions are
    implemented, to discourage extension writers from checking for a
    NULL value and not calling it.

    These functions aren't supposed to be called directly, they are
    called through convenience functions declared in
    Include/abstract.h:

        int PyObject_AquireLockedReadBuffer(PyObject *obj,
                                            const void **buffer,
                                            size_t *buffer_len);

        int PyObject_AcquireLockedWriteBuffer(PyObject *obj,
                                              void **buffer,
                                              size_t *buffer_len);

        void PyObject_ReleaseLockedBuffer(PyObject *obj);

    The former two functions return 0 on success, set buffer to the
    memory location and buffer_len to the length of the memory block
    in bytes. On failure, or if the locked buffer interface is not
    implemented by obj, they return -1 and set an exception.

    The latter function doesn't return anything, and cannot fail.


Backward Compatibility

    The size of the PyBufferProcs structure changes if this proposal
    is implemented, but the type's tp_flags slot can be used to
    determine if the additional fields are present.


Reference Implementation

    An implementation has been uploaded to the SourceForge patch
    manager as http://www.python.org/sf/652857.


Additional Notes/Comments

    Python strings, unicode strings, mmap objects, and array objects
    would expose the locked buffer interface.

    mmap and array objects would actually enter a locked state while
    the buffer is active, this is not needed for strings and unicode
    objects.  Resizing locked array objects is not allowed and will
    raise an exception. Whether closing a locked mmap object is an
    error or will only be deferred until the lock count reaches zero
    is an implementation detail.

    Guido recommends:

        But I'm still very concerned that if most built-in types
        (e.g. strings, bytes) don't implement the release
        functionality, it's too easy for an extension to seem to work
        while forgetting to release the buffer.

        I recommend that at least some built-in types implement the
        acquire/release functionality with a counter, and assert that
        the counter is zero when the object is deleted -- if the
        assert fails, someone DECREF'ed their reference to the object
        without releasing it.  (The rule should be that you must own a
        reference to the object while you've acquired the object.)

        For strings that might be impractical because the string
        object would have to grow 4 bytes to hold the counter; but the
        new bytes object (PEP 296) could easily implement the counter,
        and the array object too -- that way there will be plenty of
        opportunity to test proper use of the protocol.


Community Feedback

    Greg Ewing doubts the locked buffer interface is needed at all, he
    thinks the normal buffer interface could be used if the pointer is
    (re)fetched each time it's used.  This seems to be dangerous,
    because even innocent looking calls to the Python API like
    Py_DECREF() may trigger execution of arbitrary Python code.

    The first version of this proposal didn't have the release
    function, but it turned out that this would have been too
    restrictive: mmap and array objects wouldn't have been able to
    implement it, because mmap objects can be closed anytime if not
    locked, and array objects could resize or reallocate the buffer.

    This PEP will probably be rejected because nobody except the
    author needs it.



References

    [1] The buffer interface
        http://mail.python.org/pipermail/python-dev/2000-October/009974.html

    [2] The Buffer Problem
        http://www.python.org/dev/peps/pep-0296/


Copyright

    This document has been placed in the public domain.



Local Variables:
mode: indented-text
indent-tabs-mode: nil
sentence-end-double-space: t
fill-column: 70
End:
````

</details>

<details><summary><b>Step 6 — revision_6</b> (1073 words)</summary>

````text
Abstract
========

This PEP proposes an extension to the buffer interface called the
'locked buffer interface'.

The locked buffer interface avoids the flaws of the 'old' buffer
interface [1]_ as defined in Python versions up to and including
2.2, and has the following semantics:

- The lifetime of the retrieved pointer is clearly defined and
  controlled by the client.

- The buffer size is returned as a 'size_t' data type, which
  allows access to large buffers on platforms where ``sizeof(int)
  != sizeof(void *)``.

(Guido comments: This second sounds like a change we could also
make to the "old" buffer interface, if we introduce another flag
bit that's *not* part of the default flags.)


Specification
=============

The locked buffer interface exposes new functions which return the
size and the pointer to the internal memory block of any python
object which chooses to implement this interface.

Retrieving a buffer from an object puts this object in a locked
state during which the buffer may not be freed, resized, or
reallocated.

The object must be unlocked again by releasing the buffer if it's
no longer used by calling another function in the locked buffer
interface.  If the object never resizes or reallocates the buffer
during its lifetime, this function may be NULL.  Failure to call
this function (if it is != NULL) is a programming error and may
have unexpected results.

The locked buffer interface omits the memory segment model which
is present in the old buffer interface - only a single memory
block can be exposed.

The memory blocks can be accessed without holding the global
interpreter lock.


Implementation
==============

Define a new flag in Include/object.h::

    /* PyBufferProcs contains bf_acquirelockedreadbuffer,
       bf_acquirelockedwritebuffer, and bf_releaselockedbuffer */
    #define Py_TPFLAGS_HAVE_LOCKEDBUFFER (1L<<15)


This flag would be included in ``Py_TPFLAGS_DEFAULT``::

    #define Py_TPFLAGS_DEFAULT  ( \
                        ....
                        Py_TPFLAGS_HAVE_LOCKEDBUFFER | \
                        ....
                        0)


Extend the ``PyBufferProcs`` structure by new fields in
Include/object.h::

    typedef size_t (*acquirelockedreadbufferproc)(PyObject *,
                                                  const void **);
    typedef size_t (*acquirelockedwritebufferproc)(PyObject *,
                                                   void **);
    typedef void (*releaselockedbufferproc)(PyObject *);

    typedef struct {
        getreadbufferproc bf_getreadbuffer;
        getwritebufferproc bf_getwritebuffer;
        getsegcountproc bf_getsegcount;
        getcharbufferproc bf_getcharbuffer;
        /* locked buffer interface functions */
        acquirelockedreadbufferproc bf_acquirelockedreadbuffer;
        acquirelockedwritebufferproc bf_acquirelockedwritebuffer;
        releaselockedbufferproc bf_releaselockedbuffer;
    } PyBufferProcs;


The new fields are present if the ``Py_TPFLAGS_HAVE_LOCKEDBUFFER``
flag is set in the object's type.

The ``Py_TPFLAGS_HAVE_LOCKEDBUFFER`` flag implies the
``Py_TPFLAGS_HAVE_GETCHARBUFFER`` flag.

The ``acquirelockedreadbufferproc`` and ``acquirelockedwritebufferproc``
functions return the size in bytes of the memory block on success,
and fill in the passed void \* pointer on success.  If these
functions fail - either because an error occurs or no memory block
is exposed - they must set the void \* pointer to NULL and raise an
exception.  The return value is undefined in these cases and
should not be used.

If calls to these functions succeed, eventually the buffer must be
released by a call to the ``releaselockedbufferproc``, supplying the
original object as argument.  The ``releaselockedbufferproc`` cannot
fail.  For objects that actually maintain an internal lock count
it would be a fatal error if the ``releaselockedbufferproc`` function
would be called too often, leading to a negative lock count.

Similar to the 'old' buffer interface, any of these functions may
be set to NULL, but it is strongly recommended to implement the
``releaselockedbufferproc`` function (even if it does nothing) if any
of the ``acquireread``/``writelockedbufferproc`` functions are
implemented, to discourage extension writers from checking for a
NULL value and not calling it.

These functions aren't supposed to be called directly, they are
called through convenience functions declared in
Include/abstract.h::

    int PyObject_AquireLockedReadBuffer(PyObject *obj,
                                        const void **buffer,
                                        size_t *buffer_len);

    int PyObject_AcquireLockedWriteBuffer(PyObject *obj,
                                          void **buffer,
                                          size_t *buffer_len);

    void PyObject_ReleaseLockedBuffer(PyObject *obj);

The former two functions return 0 on success, set buffer to the
memory location and buffer_len to the length of the memory block
in bytes. On failure, or if the locked buffer interface is not
implemented by obj, they return -1 and set an exception.

The latter function doesn't return anything, and cannot fail.


Backward Compatibility
======================

The size of the ``PyBufferProcs`` structure changes if this proposal
is implemented, but the type's ``tp_flags`` slot can be used to
determine if the additional fields are present.


Reference Implementation
========================

An implementation has been uploaded to the SourceForge patch
manager as http://www.python.org/sf/652857.


Additional Notes/Comments
=========================

Python strings, unicode strings, mmap objects, and array objects
would expose the locked buffer interface.

mmap and array objects would actually enter a locked state while
the buffer is active, this is not needed for strings and unicode
objects.  Resizing locked array objects is not allowed and will
raise an exception. Whether closing a locked mmap object is an
error or will only be deferred until the lock count reaches zero
is an implementation detail.

Guido recommends

    But I'm still very concerned that if most built-in types
    (e.g. strings, bytes) don't implement the release
    functionality, it's too easy for an extension to seem to work
    while forgetting to release the buffer.

    I recommend that at least some built-in types implement the
    acquire/release functionality with a counter, and assert that
    the counter is zero when the object is deleted -- if the
    assert fails, someone DECREF'ed their reference to the object
    without releasing it.  (The rule should be that you must own a
    reference to the object while you've acquired the object.)

    For strings that might be impractical because the string
    object would have to grow 4 bytes to hold the counter; but the
    new bytes object (PEP 296) could easily implement the counter,
    and the array object too -- that way there will be plenty of
    opportunity to test proper use of the protocol.


Community Feedback
==================

Greg Ewing doubts the locked buffer interface is needed at all, he
thinks the normal buffer interface could be used if the pointer is
(re)fetched each time it's used.  This seems to be dangerous,
because even innocent looking calls to the Python API like
``Py_DECREF()`` may trigger execution of arbitrary Python code.

The first version of this proposal didn't have the release
function, but it turned out that this would have been too
restrictive: mmap and array objects wouldn't have been able to
implement it, because mmap objects can be closed anytime if not
locked, and array objects could resize or reallocate the buffer.

This PEP will probably be rejected because nobody except the
author needs it.



References
==========

.. [1] The buffer interface
       http://mail.python.org/pipermail/python-dev/2000-October/009974.html

.. [2] The Buffer Problem
       http://www.python.org/dev/peps/pep-0296/


Copyright
=========

This document has been placed in the public domain.



..
  Local Variables:
  mode: indented-text
  indent-tabs-mode: nil
  sentence-end-double-space: t
  fill-column: 70
  End:
````

</details>

<details><summary><b>Step 7 — revision_7</b> (1066 words)</summary>

````text
Abstract
========

This PEP proposes an extension to the buffer interface called the
'locked buffer interface'.

The locked buffer interface avoids the flaws of the 'old' buffer
interface [1]_ as defined in Python versions up to and including
2.2, and has the following semantics:

- The lifetime of the retrieved pointer is clearly defined and
  controlled by the client.

- The buffer size is returned as a 'size_t' data type, which
  allows access to large buffers on platforms where ``sizeof(int)
  != sizeof(void *)``.

(Guido comments: This second sounds like a change we could also
make to the "old" buffer interface, if we introduce another flag
bit that's *not* part of the default flags.)


Specification
=============

The locked buffer interface exposes new functions which return the
size and the pointer to the internal memory block of any python
object which chooses to implement this interface.

Retrieving a buffer from an object puts this object in a locked
state during which the buffer may not be freed, resized, or
reallocated.

The object must be unlocked again by releasing the buffer if it's
no longer used by calling another function in the locked buffer
interface.  If the object never resizes or reallocates the buffer
during its lifetime, this function may be NULL.  Failure to call
this function (if it is != NULL) is a programming error and may
have unexpected results.

The locked buffer interface omits the memory segment model which
is present in the old buffer interface - only a single memory
block can be exposed.

The memory blocks can be accessed without holding the global
interpreter lock.


Implementation
==============

Define a new flag in Include/object.h::

    /* PyBufferProcs contains bf_acquirelockedreadbuffer,
       bf_acquirelockedwritebuffer, and bf_releaselockedbuffer */
    #define Py_TPFLAGS_HAVE_LOCKEDBUFFER (1L<<15)


This flag would be included in ``Py_TPFLAGS_DEFAULT``::

    #define Py_TPFLAGS_DEFAULT  ( \
                        ....
                        Py_TPFLAGS_HAVE_LOCKEDBUFFER | \
                        ....
                        0)


Extend the ``PyBufferProcs`` structure by new fields in
Include/object.h::

    typedef size_t (*acquirelockedreadbufferproc)(PyObject *,
                                                  const void **);
    typedef size_t (*acquirelockedwritebufferproc)(PyObject *,
                                                   void **);
    typedef void (*releaselockedbufferproc)(PyObject *);

    typedef struct {
        getreadbufferproc bf_getreadbuffer;
        getwritebufferproc bf_getwritebuffer;
        getsegcountproc bf_getsegcount;
        getcharbufferproc bf_getcharbuffer;
        /* locked buffer interface functions */
        acquirelockedreadbufferproc bf_acquirelockedreadbuffer;
        acquirelockedwritebufferproc bf_acquirelockedwritebuffer;
        releaselockedbufferproc bf_releaselockedbuffer;
    } PyBufferProcs;


The new fields are present if the ``Py_TPFLAGS_HAVE_LOCKEDBUFFER``
flag is set in the object's type.

The ``Py_TPFLAGS_HAVE_LOCKEDBUFFER`` flag implies the
``Py_TPFLAGS_HAVE_GETCHARBUFFER`` flag.

The ``acquirelockedreadbufferproc`` and ``acquirelockedwritebufferproc``
functions return the size in bytes of the memory block on success,
and fill in the passed void \* pointer on success.  If these
functions fail - either because an error occurs or no memory block
is exposed - they must set the void \* pointer to NULL and raise an
exception.  The return value is undefined in these cases and
should not be used.

If calls to these functions succeed, eventually the buffer must be
released by a call to the ``releaselockedbufferproc``, supplying the
original object as argument.  The ``releaselockedbufferproc`` cannot
fail.  For objects that actually maintain an internal lock count
it would be a fatal error if the ``releaselockedbufferproc`` function
would be called too often, leading to a negative lock count.

Similar to the 'old' buffer interface, any of these functions may
be set to NULL, but it is strongly recommended to implement the
``releaselockedbufferproc`` function (even if it does nothing) if any
of the ``acquireread``/``writelockedbufferproc`` functions are
implemented, to discourage extension writers from checking for a
NULL value and not calling it.

These functions aren't supposed to be called directly, they are
called through convenience functions declared in
Include/abstract.h::

    int PyObject_AcquireLockedReadBuffer(PyObject *obj,
                                        const void **buffer,
                                        size_t *buffer_len);

    int PyObject_AcquireLockedWriteBuffer(PyObject *obj,
                                          void **buffer,
                                          size_t *buffer_len);

    void PyObject_ReleaseLockedBuffer(PyObject *obj);

The former two functions return 0 on success, set buffer to the
memory location and buffer_len to the length of the memory block
in bytes. On failure, or if the locked buffer interface is not
implemented by obj, they return -1 and set an exception.

The latter function doesn't return anything, and cannot fail.


Backward Compatibility
======================

The size of the ``PyBufferProcs`` structure changes if this proposal
is implemented, but the type's ``tp_flags`` slot can be used to
determine if the additional fields are present.


Reference Implementation
========================

An implementation has been uploaded to the SourceForge patch
manager as https://bugs.python.org/issue652857.


Additional Notes/Comments
=========================

Python strings, unicode strings, mmap objects, and array objects
would expose the locked buffer interface.

mmap and array objects would actually enter a locked state while
the buffer is active, this is not needed for strings and unicode
objects.  Resizing locked array objects is not allowed and will
raise an exception. Whether closing a locked mmap object is an
error or will only be deferred until the lock count reaches zero
is an implementation detail.

Guido recommends

    But I'm still very concerned that if most built-in types
    (e.g. strings, bytes) don't implement the release
    functionality, it's too easy for an extension to seem to work
    while forgetting to release the buffer.

    I recommend that at least some built-in types implement the
    acquire/release functionality with a counter, and assert that
    the counter is zero when the object is deleted -- if the
    assert fails, someone DECREF'ed their reference to the object
    without releasing it.  (The rule should be that you must own a
    reference to the object while you've acquired the object.)

    For strings that might be impractical because the string
    object would have to grow 4 bytes to hold the counter; but the
    new bytes object (:pep:`296`) could easily implement the counter,
    and the array object too -- that way there will be plenty of
    opportunity to test proper use of the protocol.


Community Feedback
==================

Greg Ewing doubts the locked buffer interface is needed at all, he
thinks the normal buffer interface could be used if the pointer is
(re)fetched each time it's used.  This seems to be dangerous,
because even innocent looking calls to the Python API like
``Py_DECREF()`` may trigger execution of arbitrary Python code.

The first version of this proposal didn't have the release
function, but it turned out that this would have been too
restrictive: mmap and array objects wouldn't have been able to
implement it, because mmap objects can be closed anytime if not
locked, and array objects could resize or reallocate the buffer.

This PEP will probably be rejected because nobody except the
author needs it.



References
==========

.. [1] The buffer interface
       https://mail.python.org/pipermail/python-dev/2000-October/009974.html


Copyright
=========

This document has been placed in the public domain.



..
  Local Variables:
  mode: indented-text
  indent-tabs-mode: nil
  sentence-end-double-space: t
  fill-column: 70
  End:
````

</details>

<details><summary><b>Step 8 — final</b> (1054 words)</summary>

````text
Abstract
========

This PEP proposes an extension to the buffer interface called the
'locked buffer interface'.

The locked buffer interface avoids the flaws of the 'old' buffer
interface [1]_ as defined in Python versions up to and including
2.2, and has the following semantics:

- The lifetime of the retrieved pointer is clearly defined and
  controlled by the client.

- The buffer size is returned as a 'size_t' data type, which
  allows access to large buffers on platforms where ``sizeof(int)
  != sizeof(void *)``.

(Guido comments: This second sounds like a change we could also
make to the "old" buffer interface, if we introduce another flag
bit that's *not* part of the default flags.)


Specification
=============

The locked buffer interface exposes new functions which return the
size and the pointer to the internal memory block of any python
object which chooses to implement this interface.

Retrieving a buffer from an object puts this object in a locked
state during which the buffer may not be freed, resized, or
reallocated.

The object must be unlocked again by releasing the buffer if it's
no longer used by calling another function in the locked buffer
interface.  If the object never resizes or reallocates the buffer
during its lifetime, this function may be NULL.  Failure to call
this function (if it is != NULL) is a programming error and may
have unexpected results.

The locked buffer interface omits the memory segment model which
is present in the old buffer interface - only a single memory
block can be exposed.

The memory blocks can be accessed without holding the global
interpreter lock.


Implementation
==============

Define a new flag in Include/object.h::

    /* PyBufferProcs contains bf_acquirelockedreadbuffer,
       bf_acquirelockedwritebuffer, and bf_releaselockedbuffer */
    #define Py_TPFLAGS_HAVE_LOCKEDBUFFER (1L<<15)


This flag would be included in ``Py_TPFLAGS_DEFAULT``::

    #define Py_TPFLAGS_DEFAULT  ( \
                        ....
                        Py_TPFLAGS_HAVE_LOCKEDBUFFER | \
                        ....
                        0)


Extend the ``PyBufferProcs`` structure by new fields in
Include/object.h::

    typedef size_t (*acquirelockedreadbufferproc)(PyObject *,
                                                  const void **);
    typedef size_t (*acquirelockedwritebufferproc)(PyObject *,
                                                   void **);
    typedef void (*releaselockedbufferproc)(PyObject *);

    typedef struct {
        getreadbufferproc bf_getreadbuffer;
        getwritebufferproc bf_getwritebuffer;
        getsegcountproc bf_getsegcount;
        getcharbufferproc bf_getcharbuffer;
        /* locked buffer interface functions */
        acquirelockedreadbufferproc bf_acquirelockedreadbuffer;
        acquirelockedwritebufferproc bf_acquirelockedwritebuffer;
        releaselockedbufferproc bf_releaselockedbuffer;
    } PyBufferProcs;


The new fields are present if the ``Py_TPFLAGS_HAVE_LOCKEDBUFFER``
flag is set in the object's type.

The ``Py_TPFLAGS_HAVE_LOCKEDBUFFER`` flag implies the
``Py_TPFLAGS_HAVE_GETCHARBUFFER`` flag.

The ``acquirelockedreadbufferproc`` and ``acquirelockedwritebufferproc``
functions return the size in bytes of the memory block on success,
and fill in the passed void \* pointer on success.  If these
functions fail - either because an error occurs or no memory block
is exposed - they must set the void \* pointer to NULL and raise an
exception.  The return value is undefined in these cases and
should not be used.

If calls to these functions succeed, eventually the buffer must be
released by a call to the ``releaselockedbufferproc``, supplying the
original object as argument.  The ``releaselockedbufferproc`` cannot
fail.  For objects that actually maintain an internal lock count
it would be a fatal error if the ``releaselockedbufferproc`` function
would be called too often, leading to a negative lock count.

Similar to the 'old' buffer interface, any of these functions may
be set to NULL, but it is strongly recommended to implement the
``releaselockedbufferproc`` function (even if it does nothing) if any
of the ``acquireread``/``writelockedbufferproc`` functions are
implemented, to discourage extension writers from checking for a
NULL value and not calling it.

These functions aren't supposed to be called directly, they are
called through convenience functions declared in
Include/abstract.h::

    int PyObject_AcquireLockedReadBuffer(PyObject *obj,
                                        const void **buffer,
                                        size_t *buffer_len);

    int PyObject_AcquireLockedWriteBuffer(PyObject *obj,
                                          void **buffer,
                                          size_t *buffer_len);

    void PyObject_ReleaseLockedBuffer(PyObject *obj);

The former two functions return 0 on success, set buffer to the
memory location and buffer_len to the length of the memory block
in bytes. On failure, or if the locked buffer interface is not
implemented by obj, they return -1 and set an exception.

The latter function doesn't return anything, and cannot fail.


Backward Compatibility
======================

The size of the ``PyBufferProcs`` structure changes if this proposal
is implemented, but the type's ``tp_flags`` slot can be used to
determine if the additional fields are present.


Reference Implementation
========================

An implementation has been uploaded to the SourceForge patch
manager as https://bugs.python.org/issue652857.


Additional Notes/Comments
=========================

Python strings, unicode strings, mmap objects, and array objects
would expose the locked buffer interface.

mmap and array objects would actually enter a locked state while
the buffer is active, this is not needed for strings and unicode
objects.  Resizing locked array objects is not allowed and will
raise an exception. Whether closing a locked mmap object is an
error or will only be deferred until the lock count reaches zero
is an implementation detail.

Guido recommends

    But I'm still very concerned that if most built-in types
    (e.g. strings, bytes) don't implement the release
    functionality, it's too easy for an extension to seem to work
    while forgetting to release the buffer.

    I recommend that at least some built-in types implement the
    acquire/release functionality with a counter, and assert that
    the counter is zero when the object is deleted -- if the
    assert fails, someone DECREF'ed their reference to the object
    without releasing it.  (The rule should be that you must own a
    reference to the object while you've acquired the object.)

    For strings that might be impractical because the string
    object would have to grow 4 bytes to hold the counter; but the
    new bytes object (:pep:`296`) could easily implement the counter,
    and the array object too -- that way there will be plenty of
    opportunity to test proper use of the protocol.


Community Feedback
==================

Greg Ewing doubts the locked buffer interface is needed at all, he
thinks the normal buffer interface could be used if the pointer is
(re)fetched each time it's used.  This seems to be dangerous,
because even innocent looking calls to the Python API like
``Py_DECREF()`` may trigger execution of arbitrary Python code.

The first version of this proposal didn't have the release
function, but it turned out that this would have been too
restrictive: mmap and array objects wouldn't have been able to
implement it, because mmap objects can be closed anytime if not
locked, and array objects could resize or reallocate the buffer.

This PEP will probably be rejected because nobody except the
author needs it.



References
==========

.. [1] The buffer interface
       https://mail.python.org/pipermail/python-dev/2000-October/009974.html


Copyright
=========

This document has been placed in the public domain.
````

</details>
