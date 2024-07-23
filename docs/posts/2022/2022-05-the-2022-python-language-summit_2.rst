.. post:: 2022-05-11
   :tags: pycon, post, legacy-blogger
   :author: Python Software Foundation
   :category: Legacy
   :location: World
   :language: en

The 2022 Python Language Summit: Performance Improvements by the Faster CPython team
====================================================================================

*This was originally posted on blogger* `here <https://pyfound.blogspot.com/2022/05/the-2022-python-language-summit_2.html>`_.

Python 3.11, if you haven’t heard, is fast. Over the past year, Microsoft has
`funded a
team <https://developers.slashdot.org/story/21/05/17/0225252/microsoft-funds-
a-team-with-guido-van-rossum-to-double-the-speed-of-python>`_ – led by core
developers Mark Shannon and Guido van Rossum – to work full-time on making
CPython faster. With additional funding from Bloomberg, and help from a wide
range of other contributors from the community, `the results have borne
fruit <https://docs.python.org/3.11/whatsnew/3.11.html#faster-cpython>`_. On the
pyperformance benchmarks `at the time of the beta
release <https://github.com/faster-cpython/ideas/blob/main/main-vs-310.rst>`_,
Python 3.11 was around 1.25x faster than Python 3.10, a phenomenal
achievement.

But there is more still to be done. At `the 2022 Python Language
Summit <https://pyfound.blogspot.com/2022/05/the-2022-python-language-
summit_01678898482.html>`_, Mark Shannon presented on where the Faster CPython
project aims to go next. The future’s fast.

  

* * *

The first problem Shannon raised was a problem of measurements. In order to
know how to make Python faster, we need to know how slow Python is currently.
But how slow at doing _what_ , exactly?

Good benchmarks are vital for a project that aims to optimise Python for
general usage. For that, the Faster CPython team needs the help of the
community at large. The project “needs more benchmarks,” Shannon said – it
needs to understand more precisely what the user base at large is using Python
for, how they’re doing it, and what makes it slow at the moment (if it is
slow!).

A benchmark, Shannon explained, is “just a program that we can time”. Anybody
with a benchmark – or even just a suggestion for a benchmark! – that they
believe is representative of a larger project they’re working on is invited to
submit them to the issue tracker at the `python/pyperformance
repository <https://github.com/python/pyperformance/issues>`_ on GitHub.

  

* * *

Nonetheless, the Faster CPython team has plenty to be getting on with in the
meantime.

Much of the optimisation work in 3.11 has been achieved through the
implementation of `PEP 659 <https://peps.python.org/pep-0659/>`_, a
“specializing adaptive interpreter”. The adaptive interpreter that Shannon and
his team have introduced tracks individual bytecodes at various points in a
program’s execution. When it spots an opportunity, a bytecode may be
“quickened”: this means that a slow bytecode, that can do many things, is
replaced by the interpreter with a more specialised bytecode that is very good
at doing one specific thing. The work on PEP 659 has now largely been done,
but major parts, such as dynamic specialisations of for-loops and binary
operations, are still to be completed.

Shannon noted that Python also has essentially the same memory consumption in
3.11 as it did in 3.10. This is something he’d like to work on: a smaller
memory overhead generally means fewer `reference-
counting <https://docs.python.org/3.6/c-api/intro.html#objects-types-and-
reference-counts>`_ operations in the virtual machine, a lower `garbage-
collection <https://devguide.python.org/garbage_collector/>`_ overhead, and
smoother performance as a result of it all.

Another big remaining avenue for optimisations is the question of C
extensions. CPython’s easy interface with C is its major advantage over other
Python implementations such as `PyPy <https://www.pypy.org/>`_, where
incompatibilities with C extensions are one of the biggest hurdles for
adoption by users. The optimisation work that has been done in CPython 3.11
has largely ignored the question of extension modules, but Shannon now wants
to open up the possibility of exposing low-level function APIs to the virtual
machine, reducing the overhead time of communicating between Python code and C
code.




* * *

Is that a JIT I see on the horizon?
-----------------------------------

Lastly, but certainly not least, Shannon said, “everybody wants a JIT
compiler… even if it doesn’t make sense yet”.

A JIT (“just-in-time”) compiler is the name given for a compiler that
dynamically detects where performance bottlenecks exist in a program as the
program is running. Once these bottlenecks have been identified, the JIT
compiles these parts of the program on-the-fly into native `machine
code <https://en.wikipedia.org/wiki/Machine_code>`_ in order to speed things up.
It’s a similar idea to Shannon’s PEP 659, but goes much further, since the
specialising adaptive interpreter never goes beyond the bytecode level.

The idea of using a JIT compiler for Python is hardly new.
`PyPy <https://www.pypy.org>`_’s JIT compiler is the major source of the large
performance gains the project has over CPython in some areas. Third-party
projects, such as `pyjion <https://github.com/tonybaloney/Pyjion>`_ and
`numba <https://github.com/numba/numba>`_, bring just-in-time compilation to
CPython that’s just a `pip install` away. Integrating a JIT into the core of
CPython, however, would be materially different.

Shannon has historically voiced scepticism about the wisdom of introducing a
JIT compiler into CPython itself, and said that work on introducing one is
still some way off. A JIT, according to Shannon, will probably not arrive
until 3.13 at the earliest, given the amount of lower-hanging fruit that is
still to be worked on. The first step towards a JIT, he explained, would be to
implement a _trace interpreter_ , which would allow for better testing of
concepts and lay the groundwork for future changes.

  

* * *

Playing nicely with the other Python projects
---------------------------------------------

The gains Shannon’s team has achieved are hugely impressive, and likely to
benefit the community as a whole in a profound way. But various problems lie
on the horizon. Sam Gross’s `proposal for a version of CPython without the
Global Interpreter Lock <https://pyfound.blogspot.com/2022/05/the-2022-python-
language-summit-python_11.html>`_ (the `nogil` fork) has potential for speeding
up multithreaded Python code in very different ways to the Faster CPython
team’s work – but it could also be problematic for some of the optimisations
that have already been implemented, many of which assume that the GIL exists.
Eric Snow’s `dream of achieving multiple subinterpreters within a single
process <https://pyfound.blogspot.com/2022/05/the-2022-python-language-summit-
per.html>`_, meanwhile, will have a smaller performance impact on single-
threaded code compared to `nogil`, but could still create some minor
complications for Shannon’s team.

