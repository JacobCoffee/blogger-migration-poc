.. post:: 2010-07-22
   :tags: pycon, post, europython, development, language, legacy-blogger
   :author: Python Software Foundation
   :category: Legacy
   :location: World
   :language: en

Python Language Summit EuroPython 2010
======================================

*This was originally posted on blogger* `here <https://pyfound.blogspot.com/2010/07/python-language-summit-europython-2010.html>`_.

_This summary was written by Tim Golden._

Before the main events of EuroPython 2010 a Python Language Summit took place
at the Conference venue in Birmingham. Present were (in the order they sat
around the table):

  * Brett Cannon
  * Guido van Rossum
  * Holger Krekel
  * Amaury Forgeot D'Arc
  * Georg Brandl
  * Péter Szabó
  * Ezio Melotti
  * Michael Foord
  * Mark Dickinson
  * Martin von Loewis
  * Ronald Oussoren
  * Tim Golden
  * Marc-André Lemburg
  * Richard Jones

Implementation Status Reports
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Michael initiated a round-up of current and prospective Python versions for
various implementations. CPython and `IronPython <http://ironpython.net/>`_ have
both just released v2.7 with IronPython offering some Python 3 compatibility
via a command-line switch. The recent/current migration of
`Numpy <http://numpy.scipy.org/>`_ and `SciPy <http://www.scipy.org/>`_ to Python
3 should give a boost to uptake.

Amaury confirmed that `PyPy <http://codespeak.net/pypy/>`_ currently supports
2.5.2 but is looking to target 2.7. The PyPy guys also announced a C API
bridging layer which should enable a range of Python extension modules to work
directly with PyPy. This is only a stepping stone by way of broadening
support.

Brett suggested that the `Unladen Swallow <http://code.google.com/p/unladen-
swallow/>`_ merge to trunk was waiting for some work to complete on the JIT
compiler and Georg, as release manager for 3.2, confirmed that Unladen Swallow
would not be merged before 3.3.

email Module
^^^^^^^^^^^^

The email module needs some work in Python 3. David Murray has been given some
money by the PSF but needs more from other sources to complete the work. This
is hampered by the legalities around commercial organisations making donations
to not-for-profits when those donations are earmarked. Various suggestions
were put forward with no-one sure of the legal issues. Guido suggested that we
should move forward rather than stall for want of legal advice.

WSGI Update
^^^^^^^^^^^

A broad discussion arose concerning the issues debated on `web-
sig <http://www.python.org/community/sigs/current/web-sig/>`_ concerning the
`WSGI <http://wsgi.org/>`_ protocol and the bytes vs string issues. Marc-André
brought up the *cgi* module which has similar issues under Python 3 and
other examples were given, including *ftplib* , *urllib* , and some *os*
functions.

Various solutions were put forward including a hybrid bytes-with-encoding
object. This proposal was widely unpopular, but two proposals met with broad
approval: that certain stdlib functions might be polymorphic, returning the
type of their input as output; and that the encoding string should include its
error-handling. An example of the first would be that `os.getenv("HOME")`
would return `"/home/tjg"` while `os.getenv(b"HOME")` would return
`b"/home/tjg"`. An example of the latter would be `"utf8:strict"`. Something
of the sort already works for PYTHONIOENCODING.

The issue of a `__format__` equivalent for bytes was also raised as was the
idea of object methods to render an object as string or bytes, which could be
used in the polymorphic functions above.

Stable Application Binary Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Martin spoke about the state of the stable ABI PEP
(`PEP-384 <http://www.python.org/dev/peps/pep-0384/>`_), indicating that he was
targeting 3.2. This work would reduce the need to recompile extension modules
separately on Windows for every version of Python -- something especially
pertinent when code has been orphaned but is still useful.

The versioned .so files PEP (`PEP-3149 <http://python.org/dev/peps/pep-3149/>`_)
being worked out by Barry Warsaw overlaps with PEP 384, and would only be
useful for extensions which don't target the stable ABI.

Garbage Collection
^^^^^^^^^^^^^^^^^^

A messy discussion turned on the question of garbage collection of module
objects, and the order in which finalisers are called if at all, especially
when reference cycles exist. Marc-André was proposing a `__cleanup__` magic
function for Python modules, which would enable the implementer to define the
order in which resources are released / closed down. This is quite a subtle
area and raised the issue of unfinalised objects in a reference cycle whose
memory has been freed out from under them but which still exist. Martin
described the Java approach where finalisers are called once and then flagged
so they are not called again, even if their object is resurrected. This
sounded like a useful approach for Python, but would break code which expected
to be able to resurrect an object during its `__del__` method, which is not
expected to account for much code.

Guido pointed out that no-one can be expected to hold enough of the
complexities of this area of Python's implementation in their head, and that
an implementation of some sort would need to be written so that the corner-
cases could emerge.

Mac OS X
^^^^^^^^

Ronald described the issues around the version and architecture differences on
Mac OS X and especially around Tkinter (and therefore IDLE). It was agreed
that two installers could be provided: one targeting OS 10.3 on 32-bit
Intel/PPC; the other targeting 10.6 on 32 and 64-bit Intel. This latter would
then be able to use the system's Tk 8.5. The 10.6 binary would also work for
10.5, which would be indicated in the install docs.

Mercurial Migration
^^^^^^^^^^^^^^^^^^^

The Mercurial migration should move forward once Dirkjan has finished work on
his thesis. Martin insisted that a for-real repository would have to be set up
so that people can really see how it would work. An outstanding issue in hg-
svn prevents the Python history from being imported, but it should be fixable.
Martin & Tim brought up the issue of externals, which the buildbots use on
Windows to bring in and build slightly patched versions of external libraries
such as OpenSSL and sqlite3.

Brett confirmed that he would like to see the stdlib broken out into its own
repository which could then be shared between the different Python
implementations.

Python Package Index
^^^^^^^^^^^^^^^^^^^^

A discussion on the `Cheeseshop / Package Index <http://pypi.python.org/>`_
highlighted the fact that the packaging infrastructure has become increasingly
important, especially since
`setuptools <http://pypi.python.org/pypi/setuptools>`_,
`buildout <http://pypi.python.org/pypi/zc.buildout>`_, and
`pip <http://pypi.python.org/pypi/pip>`_ all download from it. Richard produced
graphs showing the increase in package downloads over time, and attributed the
recent slight tail-off to the fact that the tool-chains are now becoming more
canny with respect to caching and mirroring.

Martin & Richard confirmed that mirrors are now in place, and Marc-André
confirmed that he would be putting together a proposal to have
`PyPI <http://pypi.python.org/>`_ hosted in the cloud. Guido pointed out that if
an AppEngine implementation were desirable, he was sure that AppEngine team
would support it with resources as needed. Martin didn't feel that there was a
problem with loading on the box in question; it's the uptime that's behind
people's concern as it's now so essential to installing and deploying Python
applications.

Several people outlined the recent heated discussion over the addition of a
checkbox to the PyPI user-registration pages. Tarek has already undertaken to
patch PyPI to move the checkbox back one step, allowing existing distutils
users to register from the command line. At the same time, Brett advised
removing that functionality from distutils2 as signing up on a web page is no
great hardship.

