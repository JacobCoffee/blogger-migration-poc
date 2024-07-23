.. post:: 2020-07-13
   :tags: open source, post, pip, grants, grant, legacy-blogger
   :author: Python Software Foundation
   :category: Legacy
   :location: World
   :language: en

Pip team midyear report
=======================

*This was originally posted on blogger* `here <https://pyfound.blogspot.com/2020/07/pip-team-midyear-report.html>`_.




The `grant-funded team working on improvements to
pip <https://pyfound.blogspot.com/2020/03/new-pip-resolver-to-roll-out-this-
year.html>`_ in 2020 has now passed the halfway mark. Here's an update on where
are so far and what's next.

Funding and Timeline Status
---------------------------

The plan that we proposed last year said that, by now, we would have finished
Foundational work (Phase I) and Resolver work (Phase II), and the team would
be doing Maintenance and Sustainability work (Phase III). Please see
[](https://wiki.python.org/psf/Pip2020DonorFundedRoadmap)`the timeline for
user experience work <https://wiki.python.org/psf/Pip2020DonorFundedRoadmap>`_
and `the timelines for development work <https://github.com/python/request-
for/blob/master/2020-pip/RFP.md#scope>`_.

  

We are behind where we had planned to be in the work roadmap. This is
partially because the COVID-19 pandemic disrupted our work, but also because
of policy and architecture decisions the project needed, and because
foundational user experience research work has taken more time than we
originally allotted. Thus, we have finished `the Phase I and Phase II sections
of the development work <https://github.com/python/request-
for/blob/master/2020-pip/RFP.md#scope>`_, and are approximately 75% of the way
through `the Phase I and Phase II user experience
work <https://wiki.python.org/psf/Pip2020DonorFundedRoadmap#Detailed_work_plan>`_.
See below for accomplishments so far.

  

Funding: we predicted that we would be approximately 80% of the way through
our one-year project budget (since the second half of the year has a slower
work pace, primarily focusing on maintaining and deepening the work we started
in the first half). We are now approximately 71% of the way through the
budget, which gives us flexibility for the second half of the project.

Accomplishments
---------------

  * *Multiple pip releases* (`changelog <https://pip.pypa.io/en/latest/news/>`_) since we started in January, including `332 pull requests merged since we kicked off <https://github.com/pypa/pip/pulls?q=is%3Apr+is%3Amerged+merged%3A%3E%3D2020-01-10>`_ (out of 2637 merged since 2011), and including improvements to the resolver library resolvelib: `22 pull requests merged since we kicked off <https://github.com/sarugaku/resolvelib/pulls?q=is%3Apr+is%3Amerged+merged%3A%3E2020-01-10>`_

  * *p**ip's new dependency resolver**is**about to go into beta.* We released pip 20.1 in April which included an alpha version of the new resolver (hidden behind an optional "\--unstable-feature=resolver" flag, but usable). `This month we will release pip 20.2 <https://github.com/pypa/pip/issues/8511>`_, which will include a robust beta of the new resolver (hidden behind an optional "\--use-feature=2020-resolver" flag) that we will encourage users to test.

  * *User experience data-gathering* included:

    * Recruited over 200 Python community members to be part of the UX research "panel" of respondents (`sign up if you are interested <http://www.ei8fdb.org/thoughts/2020/03/pip-ux-study-recruitment/>`_)

    * Administered 5 surveys to gather feedback about issues with the pip resolver and dependency management

    * Interviewed and/or did user tests with over 30 maintainers and users so far

  * *UX findings* and resulting improvements included:

    * [](https://www.notion.so/Error-message-format-and-guidelines-7b4ede077ad54c10a8f4182795fb949d)`Preliminary error message formatting guidelines <https://www.notion.so/Error-message-format-and-guidelines-7b4ede077ad54c10a8f4182795fb949d>`_ and `preliminary research findings to improve the ResolutionImpossible error message's format and content <https://editor.apps.ei8fdb.org/s/rylD-Qp3L#>`_, which have now `been implemented <https://github.com/pypa/pip/issues/8377>`_

    * Improved `documentation to help users fix conflicting dependencies <https://pip.pypa.io/en/latest/user_guide/#fixing-conflicting-dependencies>`_

  * *Documentation* improvements especially regarding `pip internals and architecture <https://pip.pypa.io/en/latest/development/architecture/>`_

Next steps
----------

*Phase III* `development work commences next
month <https://github.com/python/request-for/blob/master/2020-pip/RFP.md#june-
december-2020-maintenance-and-sustainability-phase-iii>`_. We will continue to
improve the pip dependency resolver in response to testers' feedback. This
will help us prepare to release pip 20.3, with the new resolver on by default,
in October. We'll also review and respond to code contributions and new
issues, to keep up with the pip code and issue review queue, help new
contributors develop into continuing contributors, and help existing
contributors grow into co-maintainers.

  

And `our user experience work will also
enter <https://wiki.python.org/psf/Pip2020DonorFundedRoadmap#Phase_III_.28Maintenance_and_Sustainability_work.2C_June-
December_2020.29>`_`
 <https://wiki.python.org/psf/Pip2020DonorFundedRoadmap#Phase_III_.28Maintenance_and_Sustainability_work.2C_June-
December_2020.29>`_*`Phase
III <https://wiki.python.org/psf/Pip2020DonorFundedRoadmap#Phase_III_.28Maintenance_and_Sustainability_work.2C_June-
December_2020.29>`_,* deepening and expanding foundational research in Python
packaging. `We will <http://www.ei8fdb.org/thoughts/2020/03/pip-ux-study-
recruitment/>`_ recruit more users for interviews and surveys, develop user
journey maps & workflows, work with maintainers to write documentation and
help messages, develop templates for UI bugs, commands, error messages,
output, documentation, and configuration files, and teach pip maintainers UX
practices.

For more info or to contribute:
-------------------------------

We run this project as transparently as possible, so you can:

  *  read and participate in `GitHub issues <https://github.com/pypa/pip/projects/6>`_

  * contact us in the `Discourse <https://discuss.python.org/t/an-update-on-pip-and-dependency-resolution/1898>`_` forum <https://discuss.python.org/t/an-update-on-pip-and-dependency-resolution/1898>`_ or `Zulip chat <https://python.zulipchat.com/#narrow/stream/218659-pip-development>`_

  * read `our meeting notes <https://wiki.python.org/psf/PackagingWG#Dependency_resolver_and_user_experience_improvements_for_pip>`_

Thank you
---------

Thanks to our contractors on this project: Nicole Harris, Bernard Tyers, and
Georgia Bullen of Simply Secure; Pradyun Gedam; Ilan Schnell; Paul F. Moore of
Atos; Tzu-ping Chung; Sumana Harihareswara of Changeset Consulting.

This award continues our relationship with Mozilla, which supported Python
packaging tools with `a Mozilla Open Source Support Award in 2017 for
Warehouse <https://pyfound.blogspot.com/2017/11/the-psf-awarded-moss-grant-
pypi.html>`_. Thank you, Mozilla! (MOSS has a number of types of awards, which
are open to different sorts of open source/free software projects. If your
project is looking for financial support, do check `the MOSS
website <https://www.mozilla.org/en-US/moss/>`_ to see if you qualify.)

  

This is new funding from the Chan Zuckerberg Initiative. This project is being
made possible in part by a grant from the Chan Zuckerberg Initiative DAF, an
advised fund of Silicon Valley Community Foundation. Thank you, CZI! (If your
free software/open source project is used by biology researchers, check `the
Essential Open Source Software for Science Request for
Applications <https://chanzuckerberg.com/rfa/essential-open-source-software-
for-science/>`_ and consider applying for the next round).

  

Thank you to the pip and
`PyPA <https://www.pypa.io/>`_[](https://www.blogger.com/) maintainers, to the
PSF and the Packaging WG, and to all the contributors and volunteers who work
on or use Python packaging tools.

  

