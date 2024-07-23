.. post:: 2019-05-21
   :tags: post, legacy-blogger
   :author: Python Software Foundation
   :category: Legacy
   :location: World
   :language: en

Petr Viktorin: Extension Modules And Subinterpreters
====================================================

*This was originally posted on blogger* `here <https://pyfound.blogspot.com/2019/05/petr-viktorin-extension-modules-and.html>`_.

`![ <https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiMA-u9-iK07aAEVCQWQ3J9EBkURU0xr1kVHKo2K1I0gJXjvcEDkije1FAWE84JUunKr1-3uMsfeJIqq2C1jh_1KZmkLO7Y6yxIcGXgfDORy7Dj0br85lHzRP1-qujnzx3usA/s640/petr-
viktorin-2.jpg>`_](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiMA-u9-iK07aAEVCQWQ3J9EBkURU0xr1kVHKo2K1I0gJXjvcEDkije1FAWE84JUunKr1-3uMsfeJIqq2C1jh_1KZmkLO7Y6yxIcGXgfDORy7Dj0br85lHzRP1-qujnzx3usA/s1600/petr-
viktorin-2.jpg)When a Python subinterpreter loads an extension module written
in C, it tends to unwittingly share state with other subinterpreters that have
loaded the same module, unless that module is written very carefully. Petr
Viktorin addressed the Python Language Summit to describe the problem in
detail and propose a cleaner isolation of subinterpreters.  
  
`Read more 2019 Python Language Summit
coverage <https://pyfound.blogspot.com/2019/05/the-2019-python-language-
summit.html>`_.  
  

Python-Based Libraries Use Subinterpreters For Isolation
========================================================

  
Python can run several interpreter instances in a single process, keeping each
subinterpreter relatively isolated from the others. There are two ways this
feature could be used in the future, but both require improvements to Python.
First, Python could achieve parallelism by giving each subinterpreter its own
Global Interpreter Lock (GIL) and passing messages between them; Eric Snow has
proposed this use of subinterpreters in `PEP
554 <https://www.python.org/dev/peps/pep-0554/#concurrency>`_.  
  
Another scenario is when libraries happen to use Python as part of their
implementation. Viktorin described, for example, a simulation library that
uses Python and NumPy internally, or a chat library that uses Python and
asyncio. It should be possible for one application to load multiple libraries
such as this, each of which uses a Python interpreter, without cross-
contamination. This use case was the subject of Viktorin’s presentation. The
problem, he said, is that “CPython is not ready for this,” because it does not
properly manage global state.  
  

There Are Many Kinds Of Global State
====================================

  
Viktorin described a hierarchy, or perhaps a tree, of kinds of global state in
an interpreter.  
  
*Process state:* For example, open file descriptors.  
  
*Runtime state:* The Python memory allocator’s data structures, and the GIL
(until PEP 554).  
  
*Interpreter state:* The contents of the "builtins" module and the dict of
all imported modules.  
  
*Thread state:* Thread locals like asyncio’s current event loop; fortunately
this is per-interpreter.  
  
*Context state:* Implicit state such as
``decimal.context <https://docs.python.org/2/library/decimal.html#decimal.localcontext>`_`.  
  
*Module state:* Python variables declared at file scope or with the “global”
keyword, which in fact creates module-local state.  
  
`![ <https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjwPHkCe37FjTDRYbReAshFlCSfasU8RLxwkroNH_A9322MQ9IWkute6v3YjcXFyIMgSulr_rkqShiGFozsxHBbo1ZTjrYbA4zNM8aHD88tqoYYN-
McVcUtei0Ik1UE4sBXMg/s640/petr-
viktorin-1.jpg>`_](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjwPHkCe37FjTDRYbReAshFlCSfasU8RLxwkroNH_A9322MQ9IWkute6v3YjcXFyIMgSulr_rkqShiGFozsxHBbo1ZTjrYbA4zNM8aHD88tqoYYN-
McVcUtei0Ik1UE4sBXMg/s1600/petr-viktorin-1.jpg)  

Module State Behaves Surprisingly
=================================

  
With a series of examples, Viktorin demonstrated the subtle behavior of
module-level state.  
  
To begin with a non-surprising example, a pure-Python module’s state is
recreated by re-importing it:  
  

    
    
    import enum
    old_enum = enum
    del sys.modules['enum']
    import enum
    old_enum == enum  # False
    

  
But surprisingly, a C extension module only _appears_ to be recreated when it
is re-imported:  
  

    
    
    import _sqlite3
    old_sqlite3 = _sqlite3
    del sys.modules['_sqlite3']
    import _sqlite3
    old_sqlite3 == _sqlite3 # False
    

  
The last line seems to show that the two modules are distinct, but as Viktorin
said, “This is a lie.” The module’s initialization is not re-run, and the
_contents_ of the two modules are shared:  
  
`old_sqlite3.Error is _sqlite3.Error # True`  
  
It is far too easy to contaminate other subinterpreters with these shared
contents—in effect, a C extension’s module state is therefore a process global
state.  
  

Modules Must Be Rewritten Thoughtfully
======================================

  
C extensions written in `the new
style <https://www.python.org/dev/peps/pep-3121/>`_ avoid this problem with
subinterpreters. Not all C extensions in the standard library are updated yet;
Christian Heimes commented that the `ssl` module must be ported to the new
style of initialization. Although it is simple to find modules that must be
ported, the actual porting requires thought. Coders must meticulously
distinguish among different kinds of global state. C static variables are
process globals, `PyState_FindModule` returns an interpreter-global reference
to a module, and `PyModule_GetState` returns module-local state. Each nugget
of module data must be deliberately placed at one of the levels in the
hierarchy.  
  
As an example of how tricky this is, Viktorin pointed out a bug in the `csv`
module. If it is imported twice, exception-handling breaks:  
  

    
    
    import _csv
    old_csv = _csv
    del sys.modules['_csv']
    import _csv
    try:
        # Pass an invalid array to reader(): should be a string, not 1.
        list(old_csv.reader([1]))
    except old_csv.Error:
        # The exception clause should catch the error but doesn't.
        pass
    

  
The` old_csv.reader` function ought to raise an instance of` old_csv.Error`,
which would match the `except` clause. In fact, the `csv` module has a bug.
When it is re-imported it overwrites interpreter-level state, including the
`_csv.Error` type, instead of keeping its state at the module-local level.  
  
Audience members agreed this was a bug, but Viktorin insists that this
particular bug is merely a symptom of a larger problem: it is too hard to
write properly isolated extension modules. `Viktorin and three coauthors have
proposed PEP 573 <https://www.python.org/dev/peps/pep-0573/>`_ to ease this
problem, with special attention to exception types.  
  
Viktorin advised all module authors to keep state at the module level. He
recognized that this is not always possible: for example, the Python standard
library’s `readline` module wraps the C `readline` library, which has global
hooks. These are necessarily process-global state. He asked the audience, how
should this scenario be handled? Should `readline` error if it is imported in
more than one subinterpreter? He said, “There’s some thinking to do.” In any
case, CPython needs a good default.  
  
The correct way to code a C extension is to use module-local state, and that
should be the most obvious place to store state from C. It seems to Viktorin
that the newest style APIs do emphasize module-local state as he desires, but
they are not yet well-known.  
  
Further reading:  
  
`PEP 384 <https://www.python.org/dev/peps/pep-0384/>`_ (3.2): Defining a Stable
ABI  
  
`PEP 489 <https://www.python.org/dev/peps/pep-0489/>`_ (3.5): Multi-phase
extension module initialization  
  
`PEP 554 <https://www.python.org/dev/peps/pep-0554/#concurrency>`_ (3.9):
Multiple Interpreters in the Stdlib  
  
`PEP 573 <https://www.python.org/dev/peps/pep-0573/>`_ (3.9): Module State
Access from C Extension Methods  
  
Not a PEP yet: `CPython C API Design
Guidelines <https://mail.python.org/archives/list/capi-
sig@python.org/message/B2VDVLABM4RQ4ATEJXFZYWEGTBZPUBKW/>`_ (layers & rings)

