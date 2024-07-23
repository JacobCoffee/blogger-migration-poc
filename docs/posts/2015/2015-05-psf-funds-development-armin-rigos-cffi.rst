.. post:: 2015-05-08
   :tags: open source, post, C, python, PSF, development, pypy, legacy-blogger
   :author: Python Software Foundation
   :category: Legacy
   :location: World
   :language: en

PSF funds development: Armin Rigo's CFFI 1.0
============================================

*This was originally posted on blogger* `here <https://pyfound.blogspot.com/2015/05/psf-funds-development-armin-rigos-cffi.html>`_.

In looking back over the PSF newsblog posts, it appears that most of the PSF
funded projects I’ve written about were conferences, workshops, and
education/outreach efforts. These are, of course, truly important. However,
it’s also important to get the word out about several development projects
that the PSF has sponsored in 2015. One such project is Armin Rigo’s work on
CFFI 1.0.

> _RESOLVED, that the Python Software Foundation grant Armin Rigo $2500
> towards cffi development aimed at making cffi generated extension modules
> importable without runtime dependencies on an extension module build
> toolchain._

"CFFI" or "C Foreign Function Interface for Python" provides a way to call
compiled C code, i.e., external C libraries, from Python using interface
declarations written in C. This eliminates the need to use a programming
language other than C and Python. At the same time, CFFI minimizes the amount
of C code that needs to be written, so it really is a boon for Python
developers. It works with Python 2.6 and up and with PyPy 2x and 3x. See `CFFI
Documentation <https://cffi.readthedocs.org/en/latest/>`_.

CFFI has already had approximately 7 million downloads, so it is clearly of
use, but its creator, Armin Rigo (who is also one of the creators of PyPy) saw
room for improvement. Specifically, according to Armin, there were two main
problems:

>   1. The difficulties of installation [which] can be seen from outside by
> looking at various workarounds and 3rd-party documentation that have grown
> into existence. For example, the `setup.py` of projects like cryptography,
> PyNaCl and bcrypt deploys workarounds that are explicitly documented
> in<https://caremad.io/2014/11/distributing-a-cffi-project/>.
>
>   2. The time taken at import is excessive in some cases. For example,
> importing `pygame-cffi` on a Raspberry Pi ARM board takes on the order of 10
> to 20 seconds (and this is the "fast" case where the compiler doesn’t need
> to be invoked any more)
>
>

Due to the PSF grant, Armin was able to fix both problems. The 1.0 version,
now in beta, is available at `CFFI
1.0 <http://morepypy.blogspot.ch/2015/05/cffi-10-beta-1.html>`_.

Our thanks to the amazing Armin Rigo for this very welcome tool!

Stay tuned for my next post about the PSF’s recent award of $8,000 USD for
_Read the Docs_.

_I would love to hear from readers. Please send feedback, comments, or blog
ideas to me at  `msushi@gnosis.cx <mailto:msushi@gnosis.cx>`_._

