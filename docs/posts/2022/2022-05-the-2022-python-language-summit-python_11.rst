.. post:: 2022-05-11
   :tags: pycon, post, legacy-blogger
   :author: Python Software Foundation
   :category: Legacy
   :location: World
   :language: en

The 2022 Python Language Summit: Python without the GIL
=======================================================

*This was originally posted on blogger* `here <https://pyfound.blogspot.com/2022/05/the-2022-python-language-summit-python_11.html>`_.

If you peruse the archives of language-summit blogs, you’ll find that one
theme comes up `again <https://lwn.net/Articles/689548/>`_
`and <https://lwn.net/Articles/723514/>`_
`again <https://lwn.net/Articles/754577/>`_: the dream of Python without the
GIL. Continuing this venerable tradition, Sam Gross kicked off `the 2022
Language Summit  <https://pyfound.blogspot.com/2022/05/the-2022-python-
language-summit_01678898482.html>`_by giving the attendees an update on `nogil`,
a project that took the Python community by storm when it was first announced
in October 2021.

The GIL, or `“Global Interpreter Lock” <https://realpython.com/python-gil/>`_,
is the key feature of Python that prevents true concurrency between threads.
This is another way of saying that it makes it difficult to do multiple tasks
simultaneously while only running a single Python process. Previously the main
cheerleader for removing the GIL was Larry Hastings, with his famous
“Gilectomy” project. The Gilectomy project was ultimately abandoned due to the
fact that it made single-threaded Python code significantly slower. But after
seeing Gross’s proof-of-concept fork in October, Hastings wrote in `an email
to the python-dev mailing list <https://mail.python.org/archives/list/python-
dev@python.org/message/CCGH6COYQGCAFZWD32ROUOHRSE4BUL3P/>`_:

  

> Sam contacted me privately some time ago to pick my brain a little. But
> honestly, Sam didn’t need any help–he’d already taken the project further
> than I’d ever taken the Gilectomy.

  

* * *

The current status of `nogil`
-----------------------------

Since releasing his `proof-of-concept
fork <https://github.com/colesbury/nogil>`_ in October – based on an alpha
version of Python 3.9 – Gross stated that he’d been working to rebase the
`nogil` changes onto 3.9.10.

3.9 had been chosen as a target for now, as reaching a level of early adoption
was important in order to judge whether the project as a whole would be
viable. Early adopters would not be able to use the project effectively if
third-party packages didn’t work when using `nogil`. There is still much
broader support for Python 3.9 among third-party packages than for Python
3.10, and so Python 3.9 still made more sense as a base branch for now rather
than 3.10 or `main`.

Gross’s other update was that he had made a change in his approach with regard
to thread safety. In order to make Python work effectively without the GIL, a
lot of code needs to have new locks added to it in order to ensure that it is
still thread-safe. Adding new locks to existing code, however, can be very
difficult, as there is potential for large slowdowns in some areas. Gross’s
solution had been to invent a new kind of lock, one that is “more Gilly”.

  

* * *

The proposal
------------

Gross came to the Summit with a proposal: to introduce a new compiler flag in
Python 3.12 that would disable the GIL.

This is a slight change to Gross’s initial proposal from October, where he
brought up the idea of a runtime flag. A compiler flag, however, reduces the
risk inherent in the proposal: “You have more of a way to back out.”
Additionally, using a compiler flag avoids thorny issues concerning
preservation of `C ABI <https://docs.python.org/3/c-api/stable.html#stable-
application-binary-interface>`_ stability. “You can’t do it with a runtime
flag,” Gross explained, “But there’s precedent for changing the ABI behind a
compiler flag”.

  

* * *

Reception
---------

Gross’s proposal was greeted with a mix of excitement and robust questioning
from the assembled core developers.

Carol Willing queried whether it might make more sense for `nogil` to carry on
as a separate fork of CPython, rather than for Gross to aim to merge his work
into the `main` branch of CPython itself. Gross, however, responded that this
“was not a path to success”.

> "A lot of the value of Python is the ecosystem, not just the language…
> CPython really leads the way in terms of the community moving as a block.
>
> "Removing the GIL is a _really_ transformative step. Most Python programs
> just don’t use threads at the moment if they want to run on multiple cores.
> If `nogil` is to be a success, the community as a whole has to buy into it."
>
> – Sam Gross

Samuel Colvin, maintainer of `the  <https://pydantic-
docs.helpmanual.io>`_``pydantic <https://pydantic-docs.helpmanual.io>`_``
library <https://pydantic-docs.helpmanual.io>`_, expressed disappointment that
the new proposal was for a compiler flag, rather than a runtime flag. “I can’t
help thinking that the level of adoption would be massively higher” if it was
possible to change the setting from within Python, Colvin commented.

There was some degree of disagreement as to what the path forward from here
should be. Gross appeared to be seeking a high-level decision about whether
`nogil` was a viable way forward. The core developers in attendance, however,
were reluctant to give an answer without knowing the low-level costs. “We need
to lay out a plan of _how_ to proceed,” remarked Pablo Galindo Salgado. “Just
creating a PR with 20,000 lines of code changed is infeasible.”

Barry Warsaw and Itamar Ostricher both asked Gross about the impact `nogil`
could have on third-party libraries if they wanted to support the new mode.
Gross responded that the impact on many libraries would be minimal – no impact
at all to a library like ``scikit-learn <https://scikit-learn.org/stable/>`_`,
and perhaps only 15 lines of code for ``numpy <https://numpy.org>`_`. Gross had
received considerable interest from scientific libraries, he said, so was
confident that the pressure to build separate C extensions to support `nogil`
mode would not be unduly burdensome. Carol Willing encouraged Gross to attend
scientific-computing conferences, to gather more feedback from that community.

There was also a large amount of concern from the attendees about the impact
the introduction of `nogil` could have on CPython development. Some worried
that introducing `nogil` mode could mean that the number of tests run in CI
would have to double. Others worried that the maintenance burden would
significantly increase if two separate versions of CPython were supported
simultaneously: one with the GIL, and one without.

Overall, there was still a large amount of excitement and curiosity about
`nogil` mode from the attendees. However, significant questions remain
unresolved regarding the next steps for the project.

