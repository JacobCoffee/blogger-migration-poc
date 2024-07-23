.. post:: 2016-01-27
   :tags: post, pypi, legacy-blogger
   :author: Python Software Foundation
   :category: Legacy
   :location: World
   :language: en

Postscript to Warehouse Post!
=============================

*This was originally posted on blogger* `here <https://pyfound.blogspot.com/2016/01/postscript-to-warehouse-post.html>`_.

Yesterday’s post described an important development project currently being
undertaken by the PSF called Warehouse. This will redevelop and improve the
Python Package Index, `PyPI <https://pypi.python.org/pypi>`_. I wanted to let
you know about a particular issue that the developers are currently trying to
solve–that of translation into languages other than English.

Yesterday, Donald Stufft wrote to the PSF community `mailing
list <https://mail.python.org/mailman/listinfo/psf-community>`_, soliciting help
from Pythonistas with experience and knowledge in non-English coding,
translating, teaching, or other relevant expertise.

The desire is to support translations of the PyPI UI (user interface). Most,
but not all, PyPI content is in English, which typically isn’t and shouldn’t
be a problem. But the UI aspires to be "more welcoming to folks who either are
not native English speakers, or may not speak English at all."

The current translation engine for PyPI is L20n.js, but the drawback is that
this client-side engine only supports more modern "evergreen" browsers–those
which continually and automatically update. There may be users who have older
browsers, especially in non-English speaking parts of the world.

One possible solution is to write a server-side implementation of L20n, i.e.,
to port it to Python. But this solution would involve taking development time
away from Warehouse itself, as well as losing some beneficial features of
client-side translation. Another possibility is to switch to Gettext, which
PyPI had been using previously, but this solution is also considered less than
ideal.

If you can help with this issue, or would like to be better informed, please
visit:

<https://mail.python.org/pipermail/distutils-sig/2016-January/028134.html>

<https://github.com/pypa/warehouse/issues/881>.

_I would love to hear from readers. Please send feedback, comments, or blog
ideas to me at  `msushi@gnosis.cx <mailto:msushi@gnosis.cx>`_._

