.. post:: 2011-09-27
   :tags: post, legacy-blogger
   :author: Python Software Foundation
   :category: Legacy
   :location: World
   :language: en

PSF Provides Grant to Port WebOb
================================

*This was originally posted on blogger* `here <https://pyfound.blogspot.com/2011/09/psf-provides-grant-to-port-webob.html>`_.

The Python Software Foundation has provided Chris McDonough with US$3000 to
port the `WebOb <http://docs.webob.org/en/latest/index.html>`_ project to Python
3. The port is scheduled to run between Oct. 1-31, with the results to be
received on or before Nov. 30.

Chris has actually begun work a little early and completed porting a
significant amount of the code already. There is still testing and
documentation work to do, however. You can follow his progress through the
project's `Github <https://github.com/Pylons/webob>`_ repository.

About WebOb
^^^^^^^^^^^

WebOb provides wrappers around the WSGI request environment, and an object to
help create WSGI responses. The objects map much of the specified behavior of
HTTP, including header parsing and accessors for other standard parts of the
environment. The current version runs on Python 2.6 and up.

Current Schedule
^^^^^^^^^^^^^^^^

Over the next few weeks, Chris will be updating the documentation and testing
WebOb against the "in the wild" things that depend on it. He encourages those
who use WebOb to check out his source from Github and try it with Python 3 and
submit bugs if they find any. You can also use the #pyramid channel on IRC to
report success stories or ask questions of Chris (AKA: `mcdonc`).

About Chris McDonough
^^^^^^^^^^^^^^^^^^^^^

Chris is a developer from Fredericksburg, VA, USA who has been using Python
since 1999, mostly to create web applications. Chris is the mastermind behind
the Pyramid web framework, the Supervisor process manager, and the Repoze set
of middleware and applications. `Chris' ohloh
profile <https://www.ohloh.net/accounts/chrism>`_ provides a good overview of
his open source contributions.

