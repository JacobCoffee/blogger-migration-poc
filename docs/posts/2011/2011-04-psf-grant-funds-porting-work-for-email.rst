.. post:: 2011-04-04
   :tags: email, post, python 3.0, grant, legacy-blogger
   :author: Python Software Foundation
   :category: Legacy
   :location: World
   :language: en

PSF Grant Funds Porting Work for the email Package
==================================================

*This was originally posted on blogger* `here <https://pyfound.blogspot.com/2011/04/psf-grant-funds-porting-work-for-email.html>`_.

R. David Murray recently completed work funded by the PSF to update Python's
`email` package to work with Python 3.2. The result of the project is a fully
functioning version of the standard library package for parsing and
constructing email messages.

Project History
^^^^^^^^^^^^^^^

The version of the `email <http://docs.python.org/py3k/library/email.html>`_
package that was shipped with Python 3.0 and 3.1 had some bugs, not the least
of which was the inability to handle binary inputs. The parser was limited to
files and messages in ASCII. Due to this, under Python 3 the `email` module
could only create messages and never receive anything. This deficiency broke
many applications that depend on `email`. For example, the
`cgi <http://docs.python.org/py3k/library/cgi.html>`_ package uses the `email`
package to process binary uploads.

After discussions held in the `email-sig discussion
group <http://mail.python.org/pipermail/email-sig/>`_, a complete rewrite of the
API was suggested as the only option and R. David Murray submitted a
`proposal <http://www.bitdance.com/projects/email6/psfproposal/>`_ to the PSF to
fund the development of Email 6. The proposal was initially accepted, and some
seed money (including matching funds) were provided. Since then, additional
funding has been provided by `QNX <http://qnx.com/>`_.

At first, David spent some time working on the Policy framework, and with some
help from Antoine Pitrou, who fixed some issues in the
`nntp <http://docs.python.org/py3k/library/nntplib.html>`_ module, David devised
a way to integrated byte handling in the `email` package without a complete
rewrite of the original code by using extensions to the API that allow it to
accept and generate bytes. The implementation used the "surrogateescape"
mechanism, developed by Martin von Löwis, allowing minimum code modifications.

David also provided some modifications to
`smtplib <http://docs.python.org/py3k/library/smtplib.html>`_, enabling it to
transmit messages with non-ASCII characters. He also worked with Victor
Stinner to give the `cgi` module the ability to handle binary data. They then
took on the task of updating the
`mailbox <http://docs.python.org/py3k/library/mailbox.html>`_ module, and using
the new features coded initially by David, made `mailbox` fully functional for
Python 3.2.

David mentions that there are still some bugs, specially in the transition to
the string/byte separation, but, also according to him, these bugs were
greatly reduced in version 3.2.

All this work gave Python 3.2 a fully functional `email` handling package. The
nntplib, smtplib, email, cgi and mailbox modules were also made functional,
something that benefits the whole Python community. The grant provided by PSF
paved the way to reach full functionality.

