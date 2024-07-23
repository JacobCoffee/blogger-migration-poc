.. post:: 2020-03-23
   :tags: open source, post, pip, grants, volunteer, grant, legacy-blogger
   :author: Python Software Foundation
   :category: Legacy
   :location: World
   :language: en

New pip resolver to roll out this year
======================================

*This was originally posted on blogger* `here <https://pyfound.blogspot.com/2020/03/new-pip-resolver-to-roll-out-this-year.html>`_.

The developers of pip are in the process of developing a new resolver for pip
(as `we announced on the PSF blog <https://pyfound.blogspot.com/2019/12/moss-
czi-support-pip.html>`_ last year). We aim to roll it out later this year.
(_Updated 29 September_ to add: `see our migration
guide <https://pip.pypa.io/en/latest/user_guide/#resolver-changes-2020>`_.) As
part of that work, there will be some major changes to how pip determines what
to install, based on package requirements. In this post we share:

*What will change*  
*What you can do to help*  
*When this will be happening*

To understand what pip does and why we’re working on it, please read `our
earlier overview post <https://pyfound.blogspot.com/2019/12/moss-czi-support-
pip.html>`_.

What will change
----------------

The most significant changes to the resolver will be:

  * It will *reduce inconsistency* : it will _no longer install a combination of packages that is mutually inconsistent_. At the moment, it is possible for pip to install a package which does not satisfy the declared requirements of another installed package. For example, right now, `pip install "six<1.12" "virtualenv==20.0.2"` does the wrong thing, “successfully” installing `six==1.11`, even though `virtualenv==20.0.2` requires `six>=1.12.0,<2` (`defined here <https://github.com/pypa/virtualenv/blob/20.0.2/setup.cfg#L42-L50>`_). The new resolver would, instead, outright reject installing anything if it got that input.
  * It will be *stricter* \- if you ask pip to install two packages with incompatible requirements, it will refuse (rather than installing a broken combination, like it does now).

Also, this is *a major change to a key part of pip* \- it’s quite possible
there will initially be bugs. We would like to make sure that those get caught
_before_ people start using the new version in production.

(For deep technical details, see `this in-progress GitHub
milestone <https://github.com/pypa/pip/projects/5>`_.)

What you can do to help
-----------------------

We recognize that everyone’s work is being disrupted by the COVID-19 pandemic,
and that many data scientists and medical researchers use Python and pip in
their work. We want to make the upgrade process as smooth and bug-free as
possible for our users; if you can help us, you’ll be helping each other.

  1. First and most fundamentally, `please help us understand how you use pip by *talking with our user experience researchers* <https://bit.ly/pip-ux-studies>`_. You can do this right now! You can take a survey, or have a researcher interview you over a video call. `Please sign up and spread the word <https://bit.ly/pip-ux-studies>`_ to anyone who uses pip (even a little bit).

  2. Right now, even before we release the new resolver as a beta, you can help by *running`pip check` on your current environment*. This will report if you have any inconsistencies in your set of installed packages. Having a clean installation will make it much less likely that you will hit issues when the new resolver is released (and may address hidden problems in your current environment!). If you run `pip check` and run into stuff you can’t figure out, please `ask for help in our issuetracker or chat <https://pip.pypa.io/>`_.

  3. Please make time to *_test_ the new version of pip, probably in May* (see below). While we have tried to make sure that pip’s test suite covers as many cases as we can, we are very aware that there are people using pip with many different workflows and build processes, and we will not be able to cover all of those without your help.

     * If you use pip to install your software, try out the new resolver and let us know if it works for you.
     * If you have a build pipeline that depends on pip installing your dependencies for you, check that the new resolver does what you need.
     * Run your project’s CI (test suite, build process, etc.) using the new resolver, and let us know of any issues.
     * If you have encountered resolver issues with pip in the past, check whether the new resolver fixes them. Also, let us know if the new resolver has issues with any workarounds you put in to address the current resolver’s limitations. We’ll need to ensure that people can transition off such workarounds smoothly.

As you and your colleagues plan for the next few months, please set aside
time, ideally in May, to test the new resolver and `tell us whether it breaks
anything for your setup by filling out this
survey <https://tools.simplysecure.org/survey/index.php?r=survey/index&sid=989272&lang=en>`_.
If you maintain an open source project or use pip at your job, you can make a
ticket now and put it in your backlog.

  4. *Spread the word!* If you know of other people who rely on pip, who might not have seen this message, let them know. You can do this right now.

  5. And if you develop or support a tool that wraps pip or uses it to deliver part of your functionality, please make time to *test your integration with our beta in May* , and sure that the new resolver doesn’t cause you any issues. (It shouldn’t, as the resolver is an internal component of pip and shouldn’t be visible to people embedding pip, but we’d like to be sure of that.)

When this will be happening
---------------------------

We intend to release the new resolver early in the second half of 2020. We
will provide *alpha and beta releases* before that point as the work
progresses (probably starting in *May*), and we’ll provide a GitHub issue
tracker and an email address where you can report bugs. We would appreciate as
much feedback as we can get on the betas when they become available.

(We were already working as a distributed team. The COVID-19 pandemic and
related disruptions are affecting us – for instance, we were aiming to meet,
work together, and test and discuss our work at PyCon US. But we still
anticipate releasing the new resolver in the second half of 2020.)

To find out when the new beta is available for testing, and how to report
problems, *`subscribe to the pypi-announce mailing
list <https://mail.python.org/mailman3/lists/pypi-announce.python.org/>`_*.
It’s very low-traffic.

(Why now? The Python Software Foundation’s Packaging Working Group `obtained
funding for this work <https://pyfound.blogspot.com/2019/12/moss-czi-support-
pip.html>`_ because it’s sorely needed; `many other features and tools are
blocked waiting for this
fix <https://wiki.python.org/psf/Fundable%20Packaging%20Improvements#Finish_dependency_resolver_for_pip>`_.
We’ve spent years addressing technical debt in pip so we can properly untie
this knot and refurbish the resolver. We started this chunk of donor-funded
work on pip a few months ago and it’s now gotten far enough that we can make
this pre-announcement.)

Thank you to the pip and PyPA maintainers, to the PSF and the Packaging WG,
and to all the contributors and volunteers who work on or use Python packaging
tools. And thank you to `Mozilla (through its Mozilla Open Source Support
Awards) <https://www.mozilla.org/en-US/moss/>`_ and to `the Chan Zuckerberg
Initiative <https://chanzuckerberg.com/eoss/>`_ DAF, an advised fund of Silicon
Valley Community Foundation, for funding enabling this work!

