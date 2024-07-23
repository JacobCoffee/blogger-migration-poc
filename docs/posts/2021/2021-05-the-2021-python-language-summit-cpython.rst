.. post:: 2021-05-20
   :tags: post, legacy-blogger
   :author: Python Software Foundation
   :category: Legacy
   :location: World
   :language: en

The 2021 Python Language Summit: CPython Performance Improvements at Instagram
==============================================================================

*This was originally posted on blogger* `here <https://pyfound.blogspot.com/2021/05/the-2021-python-language-summit-cpython.html>`_.

`Dino Viehland <https://twitter.com/DinoViehland>`_ gave a presentation at the
`2021 Python Language
Summit <https://pyfound.blogspot.com/2021/05/the-2021-python-language-
summit.html>`_ about improvements to CPython's performance at Instagram.

`![Dino
Viehland <https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjqqWiC5mKNc6rzGhp-
zdhu8z9l4GA7p61c-GLbkdgMzObwqtzn_eZhr8EJM5ZUOfnzdywQB4G1dfqWSs7-6WeQwlvF8fL5r-GXhn2wB7kJWUA_mOoz5pzX-
YA2MXxNY3dFKRA/s16000/talk-4-author.png>`_](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjqqWiC5mKNc6rzGhp-
zdhu8z9l4GA7p61c-GLbkdgMzObwqtzn_eZhr8EJM5ZUOfnzdywQB4G1dfqWSs7-6WeQwlvF8fL5r-GXhn2wB7kJWUA_mOoz5pzX-
YA2MXxNY3dFKRA/s320/talk-4-author.png)

`Cinder <https://github.com/facebookincubator/cinder>`_ is Instagram's internal
performance-oriented production version of CPython 3.8, so all of the
comparisons in this presentation dealt with Python 3.8. Cinder has a lot of
performance optimizations, including bytecode inline caching, eager evaluation
of coroutines, a method-at-a-time JIT, and an experimental bytecode compiler
that uses type annotations to emit type-specialized bytecode that performs
better in the JIT.

Successful Improvements
-----------------------

Instagram did a lot of work with asynchronous I/O. One big change was sending
and receiving values without raising StopIteration. Raising all of those
exceptions was a huge source of overhead. On simple benchmarks, this was 1.6
times faster, but it was also a 5% win in production. These changes have been
upstreamed to Python 3.10 (bpo-41756 & bpo-42085).

Instagram also made another change to asynchronous I/O that hasn't been
upstreamed yet: eager evaluation. Often, in their workload, if they await a
call to a function, then it can run and immediately complete. If the call
completes without blocking, then they don't have to create a coroutine object.
Instead, a wait handle is returned. (One singleton instance is used, as the
handle is immediately consumed.)

They used the new `vectorcall <https://www.python.org/dev/peps/pep-0590/>`_ API
to do this work, so they have a new flag to show that a call is being awaited
at the call site. In addition to having functions check this flag, they also
have asyncio.gather() check the flag. This avoids overhead for task creation
and scheduling. These changes led to a 3% win in production and haven't been
upstreamed yet, but there have been discussions.

Another big change is inline caching for byte code, which they call shadow
byte code. Although Python 3.10 has some inline caching as well, Instagram
took a somewhat different approach. In Instagram's implementation, hot methods
get a complete copy of the byte code and caches. As the function executes,
they replace the opcodes in that copy with a hidden copy that's more specific.
This resulted in a 5% win in production.

Dino Viehland also spoke about dictionary watchers, which haven't been
upstreamed to CPython. Dictionary watchers provide updates to globals for
builtins when they are modified. Instagram achieved this by reusing the
existing version tag in dictionaries to mark dictionaries that are being
watched. They took the low bit from that, so now whenever they need to bump
the dictionary version, they bump it by two. This led to an additional 5% win
when combined with shadow byte code.

Instagram made targeted optimizations as well. The CPython documentation
mentions that assigning to __builtins__ is a CPython implementation detail.
But it's an unusual one, because when you assign to it, it may not be
respected immediately. For example, if you're using the same globals, then you
use the existing builtins. Instagram made that always point to the fixed
builtins dictionary, which led to a 1% win in production.

They also made some small changes to PyType_Lookup that were upstreamed and
will be in Python 3.10. You can check bpo-43452 to learn more. In addition,
Instagram worked on ThreadState lookup avoidance and prefetching variables
before they're loaded, but frame creation is still expensive.

Experimental Work
-----------------

Instagram has tried some experimental changes as well. One big one was the
JIT. They have a custom method at a time JIT. There is nearly full coverage
for all of the opcodes. They do have some unsupported opcodes, but they are
rare and not used in methods, such as IMPORT_STAR. There are a couple of
intermediate representations. The front end lowers to an HIR where they do an
SSA and have a ref count insertion pass as well as other optimization passes.
After they go though the HIR level, they lower it to an LIR, which is closer
to x64.

Another experimental idea is something they call static Python. It provides
similar performance gains as MyPyC or Cython, but it works at runtime and has
no extra compile steps. It starts with a new source loader that loads files
marked with import __static__, and it supports cross module compilation across
different source files. There are also new byte codes such as INVOKE_FUNCTION
and LOAD_FIELD that can be bound tightly at runtime. It uses normal `PEP
484 <https://www.python.org/dev/peps/pep-0484/>`_ annotations.

InterOp needs to enforce types at the boundaries between untyped Python and
static Python. If you call a typed function, then you might get a TypeError.
Static Python has a whole new static compiler that uses the regular Python ast
module and is based on the Python 2.x compiler package.

In addition, Pyro is an unannounced, experimental, from-scratch implementation
that reuses the standard library. The main differences between Pyro and
CPython are:

  * Compacting garbage collection
  * Tagged pointers
  * Hidden classes

The C API is emulated for the `PEP
384 <https://www.python.org/dev/peps/pep-0384/>`_ subset for supporting C
extensions.

Performance Results
-------------------

Production improvements are difficult to measure because changes have been
incremental over time, but they are estimated at between 20% and 30% overall.
When Instagram was benchmarking, they used CPython 3.8 as the baseline and
compared** Cinder, Cinder with the JIT, and Cinder JIT noframe, which
Instagram is not yet using in production but wants to move towards so they
won't have to create Python frame objects for jitted code.  

Cinder had good results on a large set of benchmarks and a 4x return on
richards but did worse with others, particularly 2to3, python_startup, and
python_startup_no_site. This was probably because they JIT every single
function when it's invoked the first time. They haven't yet made the changes
to JIT a function when it becomes hot. They also haven't yet tested
comparisons with Pypy.  



Cinder is open source, so you can check out the
`repo <https://github.com/facebookincubator/cinder>`_ yourself.

