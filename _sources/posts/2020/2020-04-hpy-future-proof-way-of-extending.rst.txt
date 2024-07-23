.. post:: 2020-04-30
   :tags: post, legacy-blogger
   :author: Python Software Foundation
   :category: Legacy
   :location: World
   :language: en

HPy: a future-proof way of extending Python? - Python Language Summit 2020
==========================================================================

*This was originally posted on blogger* `here <https://pyfound.blogspot.com/2020/04/hpy-future-proof-way-of-extending.html>`_.

`![ <https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi83fOiYUKkQgeZk6-ESclX7wvTvu1GsbgkUVo2xkety6Ohv2Q6vf8KzlRL0jis93K4FFlwPmtpko-T7_YX_GWImY9ChJNOsXP4Wo7qvJip6uqrUTAnMXAIknEgZey58GPj3g/s1600/antonio-
cuni.jpeg>`_](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi83fOiYUKkQgeZk6-ESclX7wvTvu1GsbgkUVo2xkety6Ohv2Q6vf8KzlRL0jis93K4FFlwPmtpko-T7_YX_GWImY9ChJNOsXP4Wo7qvJip6uqrUTAnMXAIknEgZey58GPj3g/s1600/antonio-
cuni.jpeg)  
Antonio Cuni presented `HPy <https://github.com/pyhandle/hpy>`_ (pronounced
"aitch pi"), an attempt at a replacement C API that is compatible and
performant across several interpreter implementations. The idea was born at
EuroPython last year from a discussion among CPython, PyPy, and Cython
developers.  
  
`Read more 2020 Python Language Summit
coverage. <https://pyfound.blogspot.com/2020/04/the-2020-python-language-
summit.html>`_  

* * *

CPython's API for C extensions is tightly coupled with the interpreter's
internals. Another interpreter such as Jython, if it wants to support the same
C extensions, must emulate these internals, pretending to the C extension that
the interpreter works the same as CPython. Even CPython suffers: any of its
internals that are exposed in the C API can't be improved without breaking
compatibility. Python objects in the C API are pointers to CPython's PyObject
structs, whose internal layout is partly exposed to extensions. Extensions
expect each PyObject pointer to be constant for the object's lifetime, which
prevents a memory manager like PyPy's from `moving objects during garbage
collection <https://doc.pypy.org/en/latest/gc_info.html>`_.  
  
Most prominently, the C API requires extensions to control objects' lifetimes
by incrementing and decrementing their reference counts. Any Python
implementation that does _not_ have a reference-counting memory manager, such
as PyPy, `must emulate refcounts for the sake of the C
API <https://morepypy.blogspot.com/2018/09/inside-cpyext-why-emulating-
cpython-c.html>`_. Cuni calls this a "massive amount of precious developer hours
wasted," an impediment to performance, and the main obstacle for Larry
Hastings's `GILectomy <https://lwn.net/Articles/754577/>`_.  
  
Victor Stinner has already `outlined the design for a better C
API <https://pythoncapi.readthedocs.io/>`_ that hides some internals, but still
depends on reference-counting; Cuni confronts the same questions and gives a
more radical answer.  
  
HPy is a new C API that is interpreter-agnostic. Instead of PyObject pointers,
HPy presents _handles_ (hence the "H" in its name). Where a C API user would
incref a PyObject when copying a reference to it, an HPy user would
_duplicate_ a handle. Each handle is distinct and must be closed
independently. Cuni showed this code example:  

    
    
    /* C API */
    PyObject *a = PyLong_FromLong(42);
    PyObject *b = a;
    Py_INCREF(b);
    Py_DECREF(a);
    Py_DECREF(a); // Ok
    /* HPy */
    HPy a = HPyLong_FromLong(ctx, 42);
    HPy b = HPy_Dup(ctx, a);
    HPy_Close(a);
    HPy_Close(a); // WRONG!
    

Handles are HPy's basic departure from the C API. The independence of handles'
liftimes, said Cuni, decouples HPy from CPython's ref-counting memory manager,
and makes HPy a natural, fast C interface for other Pythons. PyPy, for
example, will maintain a map of handles to objects; when its garbage collector
moves objects in memory, it only needs to update the map. Handles permit
precise debugging: if a handle is leaked, HPy prints the line number where it
was created. (The HPy context parameter `ctx` that is passed everywhere allows
for subinterpreters, and perhaps other features in the future.)  
  
Brett Cannon asked whether HPy will be a minimalist API for extension
development, or if it will include specialized APIs for speed. For example,
the current C API has a generic `PyObject_GetItem`, and a fast
`PyDict_GetItem` specialized for dicts. Cuni said he prefers a smaller API,
but benchmarks would guide him.  
  
Cannon asked whether a tool could semi-automatically port C code from the C
API to HPy. It could not, according to Cuni, because the problem of closing
each handle exactly once must be solved carefully by a human. HPy's debug
messages will be a great help. "In theory," Cuni said, "it should be as easy
as adding an 'H' to all C API calls, renaming `Py_INCREF` to `HPy_Dup`,
putting `HPy_Close` here and there, and then see if the debug mode is happy or
complains."  
  
Victor Stinner asked whether his `draft proposal to incrementally modify the C
API to hide
internals <https://github.com/vstinner/misc/blob/master/cpython/pep-opaque-c-
api.rst>`_ would eventually solve PyPy's problems with C extensions. Cuni
replied, "It's not enough for PyPy because of reference counting and the fact
that `PyObject*` is not a good representation for objects that can move in
memory." But he acknowledged that Stinner's proposal goes in the right
direction.  
  
Cuni said the "HPy strategy to conquer the world" is to create a zero-overhead
façade that maps HPy to the C API (using compile-time macros), then port
third-party C extensions to pure HPy, one function at a time. It must be
faster on alternative implementations than their existing C API emulations;
`early benchmarks show a 3x speedup on
PyPy <https://morepypy.blogspot.com/2019/12/hpy-kick-off-sprint-report.html>`_
and 2x on `GraalPython <https://github.com/graalvm/graalpython>`_, a JVM-based
Python.  
  
`HPy is currently missing type
objects <https://hpy.readthedocs.io/en/latest/overview.html#current-status-
and-roadmap>`_, but Cuni said it "basically works." An HPy extension can be
compiled to the CPython ABI or to an "HPy universal ABI" that allows the same
compiled extension to work with multiple interpreters. In the future, a new
Cython backend will target HPy instead of the C API. Cuni and his
collaborators have ported `ujson <https://pypi.org/project/ujson/>`_ to HPy;
they plan to port `a subset of NumPy <https://github.com/paugier/piconumpy>`_
next, and eventually to write a PEP and merge HPy into the official CPython
distribution, where it will live alongside the existing C API. Cuni hopes the
core developers will endorse HPy for third-party C extension development; in a
"hypothetical sci-fi future" CPython might port its standard library C modules
to HPy.  

