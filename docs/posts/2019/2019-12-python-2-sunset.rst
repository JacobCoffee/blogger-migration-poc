.. post:: 2019-12-20
   :tags: post, python3, legacy-blogger
   :author: Python Software Foundation
   :category: Legacy
   :location: World
   :language: en

Python 2 series to be retired by April 2020
===========================================

*This was originally posted on blogger* `here <https://pyfound.blogspot.com/2019/12/python-2-sunset.html>`_.

The CPython core development community is urging users to migrate to Python 3
as it will be the only version that will be updated for bugs and security
vulnerabilities.  
  
After nearly 20 years of development on the Python 2 series, the last major
version 2.7 will be released in April 2020, and then all development will
cease for Python 2. Users are urged to migrate to Python 3 to benefit from its
many improvements, as well as to avoid potential security vulnerabilities in
Python 2.x after April 2020. This move will free limited resources for the
CPthyon core developer community for other important work.  
  
The final Python 2.7 maintenance release was originally planned for 2015\.
However, it was delayed 5 years to give people adequate time to migrate and to
work closely with vendors and redistributors to ensure that supported Python 3
migration options were available. Part of the reason for this delay was
because the stricter text model in Python 3 was forcing the resolution of non-
trivial Unicode handling issues in the reference interpreter and standard
library, and in migrated libraries and applications  
  
Python 3 is a noticeable improvement to Python. There is ground-up support for
Unicode and internationalization. It better expresses common idioms and
patterns, which in code makes it easier to read and reason about. Improvements
in concurrency, fault handling, testing, and debugging provide developers with
the opportunity to create more robust and secure applications.  
  
Going forward, Python 3 will be the only major version of CPython that is
actively maintained for bugs and security issues.  
  
More information:  

  * Press release: <https://www.python.org/psf/press-release/pr20191220/>
  * Simple FAQ: <https://www.python.org/doc/sunset-python-2/>
  * Comprehensive FAQ: <http://python-notes.curiousefficiency.org/en/latest/python3/questions_and_answers.html>
  * Developer porting guide: `https://portingguide.readthedocs.io <https://portingguide.readthedocs.io/>`_

  

Clarification Update January 8, 2020
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Effective January 1, 2020, no new bug reports, fixes, or changes will be made
to Python 2.  
  
After Python 2.7.17 (October 19, 2019) was released, some additional changes
accumulated before the end of 2019 when the core development team froze the
2.7 branch. As a final service to the community, python-dev will bundle those
fixes -- and only those fixes -- into a final 2.7.18 release. The release date
for 2.7.18 will be in April 2020 because that allows time for the release
managers to complete a release candidate and final release.  

