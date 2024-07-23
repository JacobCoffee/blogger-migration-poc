.. post:: 2011-10-17
   :tags: post, service, award, community service awards, legacy-blogger
   :author: Python Software Foundation
   :category: Legacy
   :location: World
   :language: en

2011 Frank Willison Memorial Award
==================================

*This was originally posted on blogger* `here <https://pyfound.blogspot.com/2011/10/2011-frank-willison-memorial-award.html>`_.

The 2011 Frank Willison Memorial Award for Services to the Python Community
has been awarded to Georg Brandl.

Georg has been a core contributor to CPython `since
2005 <http://hg.python.org/cpython/rev/65c95ad672ae/>`_, contributing bug fixes
for compiler internals and modules such as
`pdb <http://docs.python.org/library/pdb.html>`_. His most widely known
contributions are to Python's documentation, through writing as well as by
creating and maintaining the `Sphinx <http://sphinx.pocoo.org/>`_ tool chain for
converting
`reStructuredText <http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html>`_
input files to more easily consumed formats such as HTML and PDF.

The `video announcing Georg's
award <http://www.youtube.com/watch?v=I708QrOlM74>`_ at OSCON 2011 is available
on YouTube.

Making Documentation Easier
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Earlier versions of Python used LaTeX and a Perl-based tool-chain to convert
documentation into HTML and PDF. The reliance on Perl, and the relative
difficulty of contributing to LaTeX-formatted source files, came up from time
to time, but Georg was the one to finally take on the problem of building the
necessary tools to manage the content in another format, and then converting
all of the existing files.

Georg studied the `docutils <http://docutils.sourceforge.net/>`_ project and
decided that it met most of the requirements, but needed a few custom markup
features and a tool to convert individual input files to a unified output
document. He wrote a tool called "doctools" for Python's documentation, which
was eventually re-christened to Sphinx "because of the build tool for
python.org, which was called Pyramid -- and unhappily without regard to the
two existing projects called Sphinx."

Over time, the user base for Sphinx grew beyond CPython's documentation team,
and Georg continues to work with other contributors to make it more generally
useful for other projects. For example, some of the Python-centric features
have been reorganized with the recent addition of the "domains" system,
allowing Sphinx to be used for projects written in C, Java, and other
languages just as easily as Python.

When I asked him about Sphinx, Georg said,

> Today I'm very happy and very proud of what the community has done for
> documentation, also thanks to Sphinx: while Python itself always had
> excellent docs, now extensive and usable docs are basically a trademark of
> the whole Python community (just look at
> `ReadTheDocs <http://readthedocs.org/>`_ or
> `packages.python.org <http://packages.python.org/>`_).

About Georg
^^^^^^^^^^^

Georg is a PhD student of Physics. He works at the Munich research reactor
slash neutron source on magnetism, researching novel materials for the
computing of tomorrow. He uses Python to control experiments consisting of
dozens of individual devices, and for teaching other scientists how to do so
efficiently. When he is not working on Python-related projects, Georg likes to
cycle and to cook.

About the Award
^^^^^^^^^^^^^^^

Since 2002, O'Reilly Media has presented the `Frank Willison Award for
Contributions to the Python
Community <http://www.python.org/community/awards/frank-willison/>`_ to someone
who has done outstanding work for the Python community. The award was
established in memory of Frank Willison, a Python enthusiast and O'Reilly
editor-in-chief, who died in July 2001. Previous recipients include `Christian
Tismer (2010) <http://pyfound.blogspot.com/2010/07/frank-willison-memorial-
award-recipient.html>`_, Martin von Löwis (2008), and Steve Holden (2007).

