.. post:: 2020-03-04
   :tags: post, pypi, legacy-blogger
   :author: Python Software Foundation
   :category: Legacy
   :location: World
   :language: en

An Update on PyPI Funded Work
=============================

*This was originally posted on blogger* `here <https://pyfound.blogspot.com/2020/03/an-update-pypi-funded-work.html>`_.

`Originally announced at the end of
2018 <http://pyfound.blogspot.com/2018/12/upcoming-pypi-improvements-
for-2019.html>`_, a gift from `Facebook Research <https://research.fb.com/>`_ is
funding improvements for the security `PyPI <https://pypi.org/>`_ and its users.

What's been done
----------------

After launching a `request for
information <http://pyfound.blogspot.com/2019/08/pypi-
security-q4-2019-request-for.html>`_ and subsequent `request for
proposal <http://pyfound.blogspot.com/2019/09/pypi-security-q4-2019-request-
for.html>`_ in the second half of 2019, contractors were selected and work
commenced on `Milestone 2 <https://github.com/python/request-
for/blob/master/2019-Q4-PyPI/RFP.md#milestone-2---systems-for-automated-
detection-of-malicious-uploads>`_ of the project in December 2019 and was
completed in February 2020.

The result is that PyPI now has `tooling in
place <https://warehouse.readthedocs.io/development/malware-checks/>`_ to
implement automated checks that run in response to events such as Project or
Release creation or File uploads as well as on schedules. In addition to
`documentation <https://warehouse.readthedocs.io/development/malware-checks/>`_
example checks were also implemented that demonstrate `event
based <https://github.com/pypa/warehouse/blob/4d68ab7f06336c9b94cea634d603b54e3466489f/warehouse/malware/checks/setup_patterns/check.py>`_
and
`scheduled <https://github.com/pypa/warehouse/blob/4d68ab7f06336c9b94cea634d603b54e3466489f/warehouse/malware/checks/package_turnover/check.py>`_
checks.

Results from checks are made available for PyPI moderators and administrators
to review, but will not have any automated responses put in place. As a check
suite is developed and refined we hope that these will help to identify
malicious uploads and spam that PyPI regularly contends with.

What's next
-----------

With the acceptance of `PEP 458 <https://www.python.org/dev/peps/pep-0458/>`_ on
`February 15 <https://github.com/python/peps/pull/1306>`_ we're excited to
announce that work on implementation of `The Update
Framework <https://theupdateframework.io/>`_ has started.

This work will enable clients like `pip` to ensure that they have downloaded
valid files from PyPI and equip the PyPI administrators to better respond in
event of a compromise.

The timeline for this work is currently planned over the coming months, with
an initial key signing to be held at `PyCon 2020 <https://us.pycon.org/2020/>`_
in Pittsburgh, Pennsylvania and rollout of the services needed to support
`TUF <https://theupdateframework.io/>`_ enabled clients in May or June.

Other PyPI News
---------------

For users who have enabled `two factor
authentication <https://pyfound.blogspot.com/2020/01/start-using-2fa-and-api-
tokens-on-pypi.html>`_ on PyPI, support has been
`added <https://github.com/pypa/warehouse/pull/7260>`_ for Account Recovery
codes. These codes are intended for use in the case where you've lost your
Webauthn device or TOTP application, allowing you to recover access to your
account.

You can generate and store recovery codes now by visiting your `account
settings <https://pypi.org/manage/account/#two-factor>`_ and clicking "Generate
Recovery Codes".

