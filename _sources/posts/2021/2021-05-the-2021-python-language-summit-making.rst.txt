.. post:: 2021-05-20
   :tags: post, legacy-blogger
   :author: Python Software Foundation
   :category: Legacy
   :location: World
   :language: en

The 2021 Python Language Summit: Making CPython Faster
======================================================

*This was originally posted on blogger* `here <https://pyfound.blogspot.com/2021/05/the-2021-python-language-summit-making.html>`_.

At the `2021 Python Language
Summit <https://pyfound.blogspot.com/2021/05/the-2021-python-language-
summit.html>`_, `Guido van Rossum <https://twitter.com/gvanrossum>`_ gave a
presentation about plans for making CPython faster. This presentation came
right after `Dino Viehland's talk about Instagram's performance improvements
to CPython <https://pyfound.blogspot.com/2021/05/the-2021-python-language-
summit-cpython.html>`_ and made multiple references to it.

`![Guido van
Rossum <https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjXUICqNBposvfIqu63rjCOvn1nm8zmAS98pvVK0phoV2cEdms1YEjSVFOkd-
ZdkPR2jTXSgfa8HX2aJcSrueSc7Fu9rYCsahz6rMK8aAFtHzj_RmywwhkTpyKok7LQlPOJ7vg/s16000/guido.png>`_
](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjXUICqNBposvfIqu63rjCOvn1nm8zmAS98pvVK0phoV2cEdms1YEjSVFOkd-
ZdkPR2jTXSgfa8HX2aJcSrueSc7Fu9rYCsahz6rMK8aAFtHzj_RmywwhkTpyKok7LQlPOJ7vg/s500/guido.png)



Can We Make CPython Faster?
---------------------------

We can, but it's not yet clear by how much. Last October, `Mark
Shannon <https://github.com/markshannon>`_ shared a plan on
`GitHub <http://github.com/markshannon/faster-cpython>`_ and python-dev. He
asked for feedback and said that he could make CPython five times faster in
four years, or fifty percent faster per year for four years in a row. He was
looking for funding and wouldn't reveal the details of his plan without it.

How Will We Make CPython Faster?  
----------------------------------

Seven months ago, Guido van Rossum left a brief retirement to work at
Microsoft. He was given the freedom to pick a project and decided to work on
making CPython faster. Microsoft will be funding a small team consisting of
Guido van Rossum, Mark Shannon, Eric Snow, and possibly others.

The team will:

  * Collaborate fully and openly with CPython's core developers
  * Make incremental changes to CPython
  * Take care of maintenance and support
  * Keep all project-specific repos open  

  * Have all discussions in trackers on open GitHub repos



The team will need to work within some constraints. They'll need to keep code
maintainable, not break stable ABI compatibility, not break limited API
compatibility, and not break or slow down extreme cases, such as pushing a
million cases on the eval stack. Although they won't be able to change the
data model, they will be able to change:

  * The byte code
  * The compiler
  * The internals of a lot of objects



The team is optimistic about doubling CPython's speed for 3.11. They plan to
try an adaptive, specializing byte code interpreter, which is a bit like the
existing inline cache and a bit like the shadow byte code covered in `Dino
Viehland's talk <https://pyfound.blogspot.com/2021/05/the-2021-python-
language-summit-cpython.html>`_. Mark Shannon shared a sketch of an
implementation of an adaptive specializing interpreter in `PEP
659 <https://www.python.org/dev/peps/pep-0659/>`_.



If the team grows, then they'll have more room to try other optimizations.
They could improve startup time, change the pyc file format, change the
internals of integers, put __dict__ at a fixed offset, use hidden classes, and
possibly use tagged integers.

  

The team plans to keep working on speeding up CPython after Python 3.11, but
they'll need to be creative in order to achieve a 5x improvement. It will
involve machine-generated code. They may also need to evolve the stable ABI.



Who Will Benefit?
-----------------

You'll benefit from the speed increase if you:

  * Run CPU-intensive pure Python code
  * Use tools or websites built in CPython



You might not benefit from the speed increase if you:

  * Rewrote your code in C, Cython, C++, or similar to increase speed already (e.g. NumPy, TensorFlow)
  * Have code that is mostly waiting for I/O
  * Use multithreading
  * Need to make your code more algorithmically efficient first

  

Where Can You Learn More?  
---------------------------

To learn more, you can check out the following repos:

  * `Fork of CPython for staging branches <http://github.com/faster-cpython/cpython>`_
  * `Tracker for discussions <http://github.com/faster-cpython/ideas>`_
  * `Tools for analysis, benchmarking, and more <http://github.com/faster-cpython/tools>`_

You can also read through `PEP 659 — Specializing Adaptive
Interpreter <https://www.python.org/dev/peps/pep-0659/>`_.

