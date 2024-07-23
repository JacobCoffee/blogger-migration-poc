.. post:: 2017-11-27
   :tags: post, pypi, legacy-blogger
   :author: Python Software Foundation
   :category: Legacy
   :location: World
   :language: en

The PSF awarded $170,000 grant from Mozilla Open Source Program to improve sustainability of PyPI
=================================================================================================

*This was originally posted on blogger* `here <https://pyfound.blogspot.com/2017/11/the-psf-awarded-moss-grant-pypi.html>`_.

When are we finally going to see
`Warehouse <https://github.com/pypa/warehouse>`_ deployed? What's the holdup?
Has this project stalled?  
  
For the last year, we at the Python Packaging Authority have heard these
questions continuously from the Python community.  
  
Today we are excited to announce that we have applied for, and been awarded, a
grant to help improve the sustainability of the `Python Package
Index <http://pypi.python.org/>`_ in the amount of $170,000.  This has been
awarded by `Mozilla <https://www.mozilla.org/>`_, through the `Foundational
Technology <https://www.mozilla.org/en-US/moss/foundational-technology/>`_ track
of their `Open Source Support Program <https://www.mozilla.org/en-US/moss/>`_.
We would like to thank Mozilla for their support.  
  
This post will explain both the context for this request, and the work that
will be funded.  
Specifically, this grant funds several contributors' efforts to finish the
development and deployment of Warehouse (`pypi.org <https://pypi.org/>`_), the
`replacement <http://pyfound.blogspot.com/2016/01/welcome-to-warehouse.html>`_
for our legacy codebase that runs `pypi.python.org <http://pypi.python.org/>`_
\-- which will allow more people to contribute.  
  

Background
----------

  

The Python Packaging Index (PyPI) is the principal repository of software
packages for the Python programming language. Currently, over 100 million
Python packages are downloaded from PyPI every week. The Python community (and
indeed the wider technical community) depends on PyPI for the ongoing
functioning of the entire Python ecosystem.  
  
There are no paid staff at the PSF who work on PyPI, and there are only a
handful of people who contribute regularly.  *This leads to a situation where
we have to depend on volunteers to be on-call for outages and respond to
critical security vulnerabilities in core Python Infrastructure.* For deeper
context, read `PyPI maintainer Donald Stufft's May 2016 post "Powering the
Python Package Index" <https://caremad.io/posts/2016/05/powering-pypi/>`_, (but
note that `since his job change in the last
year <https://caremad.io/posts/2017/01/a-new-home/>`_ his paid time to work on
PyPI has decreased significantly).  
  
This isn't a tenable situation for the long term, and we hope that this grant
will help us start to change this.  
  

Developer Sustainability
------------------------

  
Unfortunately, the codebase that runs PyPI is old, almost entirely lacking in
automated test coverage and other common best practices. (PyPI contributor
Ernest W. Durbin III goes into this further in his PyGotham 2017 talk
`"Running Vintage Software: PyPI's Aging
Codebase." <http://pyvideo.org/pygotham-2017/running-vintage-software-pypis-
aging-codebase.html>`_) The new Warehouse code base is built with Pyramid, and
is much easier to maintain. This technical debt has a number of undesirable
outcomes, but the one I'd like to focus on is *repelling new contributors*.  
  
Eric Holscher, like many would-be contributors to the legacy PyPI codebase,
once tried to contribute a small feature to PyPI years ago, thinking it would
be quite simple. However, as he opened the code base and started looking
around, he discovered that the code wasn't written in a modern framework,
didn't follow standard conventions or best practices, and he could barely even
understand where to start adding something new.  
  
Migrating PyPI to a new codebase will stop this from happening. We hope to
gain a number of new contributors who are willing and able to help maintain
the code base, and decrease the chance of burnout for the staff.  
  

Operations Sustainability
-------------------------

  
Operations are the other large sustainability issue that we're hoping to
tackle with this grant. There are only two people currently who wear a pager
and are on-call for PyPI. They are not currently supported by modern
automation tools or served by a continuing project manager. Once all package
index activity is going through pypi.org (Warehouse) and we deprecate the old
pypi.python.org codebase and site, with a stabilized infrastructure resource
load, we can assess our new level of staffing and hosting needs. Based on that
assessment, we'll be able to fundraise for staffing and ask our sponsors for
financial and in-kind donations to keep PyPI robust.  
  

Next Steps
----------

  
With the help of many people (especially the Packaging Working Group, our MOSS
liaison Gervase Markham, our Mozilla champion Dan Callahan, and Ewa Jodlowska
and Mark Mangoba at the PSF), we've been figuring out the timeline for this
work.  
  
`The first milestone for
Warehouse <https://github.com/pypa/warehouse/milestone/1>`_ is redirecting
portions of the production pypi.python.org to Warehouse including traffic for
the simple index and package downloads. At that milestone Warehouse will be
the main entryway to Python packages for all but a small fraction of the
interactions PyPI sees.  
  
The bulk of the work will be bringing Warehouse to feature parity with the
administrative capabilities users need from the Package Index.  We'll keep you
posted as we figure out when you can expect that to be true.  
  
Please feel free to ask questions about the Warehouse project `in the #pypa-
dev channel on Freenode <https://webchat.freenode.net/?channel=#pypa-dev>`_, or
`in the GitHub issues for Warehouse <https://github.com/pypa/warehouse/>`_! If
you have questions for the PSF about the grant, you can ask `via
email <https://www.python.org/psf/about/#how-do-i-reach-the-psf>`_.  
  
Thanks to Donald Stufft, Ewa Jodlowska, Nathaniel J. Smith, Nick Coghlan,
Nicole Harris, Sumana Harihareswara, Ernest W. Durbin III, Dustin Ingram, Mark
Mangoba, Kenneth Reitz, Eric Holscher for contributing to this post.

