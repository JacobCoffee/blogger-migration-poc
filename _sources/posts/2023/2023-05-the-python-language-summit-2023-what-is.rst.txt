.. post:: 2023-05-29
   :tags: pycon, post, legacy-blogger
   :author: Python Software Foundation
   :category: Legacy
   :location: World
   :language: en

The Python Language Summit 2023: What is the Standard Library for?
==================================================================

*This was originally posted on blogger* `here <https://pyfound.blogspot.com/2023/05/the-python-language-summit-2023-what-is.html>`_.

 Brett Cannon came to the `Python Language
Summit <https://pyfound.blogspot.com/2023/05/the-python-language-
summit-2023_29.html>`_ this year with a fundamental question for the assembled
core developers: What is the standard library for?

According to a quick `python -c "import sys;
print(len(sys.stdlib_module_names))"` call on my laptop, the standard library
in Python 3.11 consists of 305 importable modules. Many of these are
implementation details that, if you’re a good citizen, you really _shouldn’t_
be importing – but the point stands that the Python standard library is
perhaps now larger than it should be.

But the goal of his question, Cannon explained, wasn’t to decide which modules
to get _rid_  of. Instead, it was to create guidelines on when and why _new_
modules should be accepted into the standard library.

> "We need to audit the standard library, and not _deprecate_  it, but decide
> which bits should probably not have been added if we had perfect hindsight.

> \-- _Guido van Rossum, CPython Core Developer and former BDFL_

Carol Willing agreed that the core dev team shouldn’t be looking to remove
modules _en masse_ , but should decide what kinds of modules they wanted to
admit in the future. Łukasz Langa agreed, and pointed out that it was often
hard removing modules even when we wanted to, due to the fact that “the
standard library is a huge import cycle”.

Where do we go now?
-------------------

Cannon himself put forward two possible answers to his question, before
tossing it out to the audience:

  1. The standard library should contain everything required to bootstrap an installer.
  2. The standard library should make it easy for beginners to be able to write scripts without installing anything.

The conversation was free-flowing, but a common point of consensus among the
attendees was that the standard library should focus on tools and utilities
that allow users to write better Python code. Hynek Schlawack cited
``dataclasses` <https://docs.python.org/3/library/dataclasses.html>`_ as an
example of a module that made writing classes much less painful, and generally
led to them writing better code as a result. (Schlawack is the author of the
`attrs <https://www.attrs.org/en/stable/>`_ library, the third-party inspiration
for `dataclasses`, which itself is still going strong.) Filipe Laíns agreed,
arguing that the core dev team should focus on building business
implementations for third-party libraries to build on top of.

> “The default answer for ‘Should this be in the standard library?’ should be
> ‘No’, but we should bless smaller utilities that help people write better
> Python code”

> \-- _Antonio Cuni, HPy Core Developer_

There was a certain amount of regret in the air about modules that perhaps
should never have been added to the standard library, and had proved
themselves to be significant maintenance burdens in the years since, but could
now never be removed.
``tkinter` <https://docs.python.org/3/library/tkinter.html>`_, it was
universally agreed, was the primary example here; possibly
``multiprocessing` <https://docs.python.org/3/library/multiprocessing.html>`_
also.

Guido van Rossum pondered whether
``asyncio` <https://docs.python.org/3/library/asyncio.html>`_ should ever have
been added to the standard library, remarking that it had been difficult to
evolve `asyncio` while it was in the standard library, and had possibly been
added before it was “fully baked”. The `ssl` integration had probably been a
mistake, he said, and should have been left to third parties.

Łukasz Langa noted that modules such as `asyncio` and
``typing` <https://docs.python.org/3/library/typing.html>`_, which had continued
to evolve rapidly after being added to the standard library, had helped spur
new syntax changes to Python that had been to the language’s betterment.
Without `asyncio` in the standard library, Langa argued, we would probably
never have adopted the `async`/`await` syntax that is now the foundation of
asynchronous Python programming.

Zac Hatfield-Dods, maintainer of several prominent third-party packages, said
that different standard-library packages had different impacts on the Python
ecosystem. `Pytest <https://docs.pytest.org/en/7.3.x/>`_, one of the libraries
he maintains, had managed to flourish and find success despite the existence
of ``unittest` <https://docs.python.org/3/library/unittest.html>`_ in the
standard library. But another library he helps out with, the asynchronous
`Trio <https://trio.readthedocs.io/en/stable/>`_ framework, had struggled to
attract users while `asyncio` had been part of the standard library. “Nobody
supports alternative async implementations,” he complained, despite Trio’s
development often being years ahead of where `asyncio` is. (In the coffee
break afterwards, Hatfield-Dods was keen to emphasise that he is, in fact, a
fan of `asyncio` and the work of the `asyncio` maintainers.)

  

`![ <https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhNHMtg7BSQza8aOAebA4arhofrKFaaX0MulKsXjgTFBc
--7H5bWHuumjdw-
DMOHN_eGH1cBA4sZzumqMPp0caSMVZv2aySrlwd7R9jMgjwwsMEpluO89sKCEsbAiHli5fg_i65HkN2OJoXnCqlKQiCA9HBlICEB_NUcFOsN3WcCPKOAbU/s320/image_2023-05-27_223251699.png>`_](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhNHMtg7BSQza8aOAebA4arhofrKFaaX0MulKsXjgTFBc
--7H5bWHuumjdw-
DMOHN_eGH1cBA4sZzumqMPp0caSMVZv2aySrlwd7R9jMgjwwsMEpluO89sKCEsbAiHli5fg_i65HkN2OJoXnCqlKQiCA9HBlICEB_NUcFOsN3WcCPKOAbU/s959/image_2023-05-27_223251699.png)  
---  
Zac Hatfield-Dods (left), speaking at the Language Summit  
(Photo by Hugo van Kemenade)  
  
  

Cannon brought up the question of whether a module like
``pathlib` <https://docs.python.org/3/library/pathlib.html>`_ belonged. “It’s
just sugar,” he remarked – i.e., hardly a “core utility” or a protocol that
allowed people to write better code. But it has nonetheless been one of the
more popular additions to the standard library in recent years. Langa again
pushed back, arguing that without the addition of `pathlib` to the standard
library, we would never have added
``os.PathLike` <https://docs.python.org/3/library/os.html#os.PathLike>`_, a
protocol that had allowed a common interface for describing file-system paths
in Python. “A third-party PyPI package wouldn’t have convinced us to make that
change,” Langa argued.

Several attendees noted that adding a module to the standard library often
made it hard for users to use features added to the module in newer versions
of Python, due to CPython’s slow development cycle. One solution could be to
provide third-party versions of standard-library modules on PyPI, backporting
the latest features of a module to older versions of Python. Thomas Wouters
argued that previous attempts at providing these backport modules had often
been disastrous. However, Jelle Zijlstra noted that
`typing_extensions <https://github.com/python/typing_extensions>`_, which
backports features from the latest version of the `typing` module, had been
incredibly successful (though it was sometimes hard to maintain).

Overall, there was agreement that the original motivations for a large,
“batteries-included” standard library no longer held up to scrutiny. “In the
good old days,” Ned Deily reminisced, “We said ‘batteries-included’ because we
didn’t have a good story for third-party installation.” But in 2023,
installing third-party packages from PyPI is much easier.

Often, Thomas Wouters noted, people preferred using standard-library modules
in a corporate setting due to the fact that the installation of any third-
party package would require approval from their company’s IT department. But,
he noted, this was hardly Python’s problem.

