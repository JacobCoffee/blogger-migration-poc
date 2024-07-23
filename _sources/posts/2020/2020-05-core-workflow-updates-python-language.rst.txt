.. post:: 2020-05-07
   :tags: post, legacy-blogger
   :author: Python Software Foundation
   :category: Legacy
   :location: World
   :language: en

Core Workflow updates - Python Language Summit 2020
===================================================

*This was originally posted on blogger* `here <https://pyfound.blogspot.com/2020/05/core-workflow-updates-python-language.html>`_.

`![ <https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjcuM2j2xsM-
FWT81fCMoDu43PV9FZak01JYveD9qE912_5YKq0y6UYe7hl5AhnuYcrOi50-xKtaJ_ztXjVYEehJvbAtFF1eVWuUxp0bWjamES6kk0K8wcRrj5y5jydU0VN9Q/s320/wijaya.jpg>`_](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjcuM2j2xsM-
FWT81fCMoDu43PV9FZak01JYveD9qE912_5YKq0y6UYe7hl5AhnuYcrOi50-xKtaJ_ztXjVYEehJvbAtFF1eVWuUxp0bWjamES6kk0K8wcRrj5y5jydU0VN9Q/s1600/wijaya.jpg)  
  
The PyCon 2015 sprint was the first time this blogger contributed to Python—or
rather, I tried to. The three patches I submitted that year are awaiting a
review to this day. In recent years, however, the core team has made bold
changes to their development workflow to make their tasks easier, to spread
responsibility more widely, and to improve the experience of contributors.
When I submitted a patch in the 2018 sprints it was reviewed and merged in a
few weeks. Mariatta Wijaya has led many of these changes. She presented the
latest updates to the core workflow.  
  
`Read more 2020 Python Language Summit
coverage <http://pyfound.blogspot.com/2020/04/the-2020-python-language-
summit.html>`_.  

* * *

"This is the third Language Summit in which I've talked about GitHub issues,"
sighed Wijaya. `Last year she
urged <https://pyfound.blogspot.com/2019/05/mariatta-wijaya-lets-use-github-
issues.html>`_ the core team to make a decision about replacing the quirky old
bug tracker on bugs.python.org. Two weeks later they approved `PEP 581: Using
GitHub Issues <https://www.python.org/dev/peps/pep-0581/>`_. Its sequel, `PEP
588: GitHub Issues Migration plan <https://www.python.org/dev/peps/pep-0588/>`_,
is still in progress. "I really care about this topic," said Wijaya, but she
and her collaborators have mostly focused on other projects for the last year.  
  
There are signs of progress, however. Wijaya began a wish list where Python
developers can request `features for GitHub's issue
tracker <https://github.com/python/core-workflow/issues/359>`_ that will make it
a full replacement for bugs.python.org. `The PSF is seeking to hire a project
manager <http://pyfound.blogspot.com/2020/05/pythons-migration-to-github-
request-for.html>`_ for the migration. Wijaya, Brett Cannon, and others have met
with GitHub staff, who have offered to import old issues in bulk. The
migration will be "like throwing a big switch," said Cannon; there must be a
great deal of planning behind the scenes before it is thrown.  
  
In 2018, the Python developers created `a web
forum <https://discuss.python.org/>`_ (running on
`Discourse <https://discourse.org/>`_) as a potential replacement for their
several mailing lists. Since then, they have contended with _both_ mailing
lists and the web forum. Wijaya asked, "We've been using Discourse for a
couple of years, is it time to make some final decisions?" Guido van Rossum
said that using Discourse via email is clunky, but if he silenced its emails
he would forget to check it on the web. Brett Cannon hypothesized that people
who have tuned their personal systems for managing email prefer to use only
email, and those who have not, prefer Discourse. The Summit attendees reached
no conclusion.  
  
A new team of Python contributors formed last summer: `the Python Triage
Team <https://devguide.python.org/triaging/#python-triage-team>`_. Triagers can
close issues, edit issue labels, etc., and they can label or close pull
requests in the Python organization's GitHub repositories. Unlike core
developers, they cannot merge pull requests. Their power to manage issues
extends to all the core developers' repositories, including CPython, the
developer guide, and the source code for Python's GitHub bots. New members
join the team `when they are invited by core
developers <https://devguide.python.org/triaging/#becoming-a-member-of-the-
python-triage-team>`_; they can self-nominate by asking a core dev to vouch for
them. Wijaya said several triagers have graduated to the core team, and she
wants this pipeline to keep flowing. New core developer Kyle Stanley
recommended better promotion of the triager-to-core-dev career path. "For
myself and several recent candidates, it seems to have worked excellently as a
stepping stone."

