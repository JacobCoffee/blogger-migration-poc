.. post:: 2019-05-30
   :tags: post, pypi, legacy-blogger
   :author: Python Software Foundation
   :category: Legacy
   :location: World
   :language: en

Use two-factor auth to improve your PyPI account's security
===========================================================

*This was originally posted on blogger* `here <https://pyfound.blogspot.com/2019/05/use-two-factor-auth-to-improve-your.html>`_.

To increase the security of Python package downloads, we're beginning to
introduce two-factor authentication (2FA) as a login security option on the
Python Package Index. This is thanks to a `grant from the Open Technology
Fund <https://pyfound.blogspot.com/2019/03/commencing-security-accessibility-
and.html>`_; coordinated by the `Packaging Working
Group <https://wiki.python.org/psf/PackagingWG>`_ of the `Python Software
Foundation <https://www.python.org/psf-landing/>`_.  
  
Starting today, the canonical Python Package Index at
`PyPI.org <https://pypi.org/>`_ and the test site at
`test.pypi.org <https://test.pypi.org/>`_ offer 2FA for all users. We encourage
project maintainers and owners to log in and `go to their Account Settings to
add a second factor <https://pypi.org/manage/account/#two-factor>`_. This will
help improve the security of their PyPI user accounts, and thus reduce the
risk of vandals, spammers, and thieves gaining account access.  
  
PyPI's maintainers `tested this new feature throughout
May <https://wiki.python.org/psf/WarehousePackageMaintainerTesting>`_ and fixed
several resulting bug reports; regardless, you might find a new issue. If you
find any potential security vulnerabilities, please follow our `published
security policy <https://pypi.org/security/>`_. (Please don't report security
issues in Warehouse via GitHub, IRC, or mailing lists. Instead, please
directly email one or more of our maintainers.) If you find an issue that is
not a security vulnerability, please `report it via
GitHub <https://github.com/pypa/warehouse/issues/new>`_.  
  
PyPI currently supports a single 2FA method: generating a code through a Time-
based One-time Password (TOTP) application. After you set up 2FA on your PyPI
account, then you must provide a TOTP (along with your username and password)
to log in. Therefore, to use 2FA on PyPI, you'll need to provision an
application (usually a mobile phone app) in order to generate authentication
codes; see `our FAQ <https://pypi.org/help/#totp>`_ for suggestions and
pointers.  
  
You'll need to verify your primary email address on your Test PyPI and/or PyPI
accounts before setting up 2FA. You can also do that in `your Account
Settings <https://pypi.org/manage/account/#account-emails>`_.  
  
Currently, only TOTP is supported as a 2FA method. Also, 2FA only affects
login via the website which safeguards against malicious changes to project
ownership, deletion of old releases, and account take overs. Package uploads
will continue to work without 2FA codes being provided.  
  
But we're not done! We're currently working on WebAuthn-based multi-factor
authentication, which will let you use, for instance, Yubikeys for your second
factor. Then we'll add API keys for package upload, then an advanced audit
trail of sensitive user actions. More details are in `our progress
reports <https://discuss.python.org/t/pypi-security-work-multifactor-auth-
progress-help-needed/1042>`_.  
  
Thanks to the `Open Technology Fund <https://www.opentech.fund>`_ for funding
this work. And please sign up for the `PyPI Announcement Mailing
List <https://mail.python.org/mailman3/lists/pypi-announce.python.org/>`_ for
future updates.

