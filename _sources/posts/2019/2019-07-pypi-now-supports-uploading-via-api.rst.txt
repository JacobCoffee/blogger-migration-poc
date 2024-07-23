.. post:: 2019-07-31
   :tags: post, pypi, legacy-blogger
   :author: Python Software Foundation
   :category: Legacy
   :location: World
   :language: en

PyPI now supports uploading via API token
=========================================

*This was originally posted on blogger* `here <https://pyfound.blogspot.com/2019/07/pypi-now-supports-uploading-via-api.html>`_.

We're `further <https://pyfound.blogspot.com/search/label/pypi>`_ increasing the
security of the Python Package Index with another new beta feature: scoped API
tokens for package upload. This is thanks to a `grant from the Open Technology
Fund <https://pyfound.blogspot.com/2019/03/commencing-security-accessibility-
and.html>`_, coordinated by the `Packaging Working
Group <https://wiki.python.org/psf/PackagingWG>`_ of the `Python Software
Foundation <https://www.python.org/psf-landing/>`_.  
  
Over the last few months, we've `added two-factor authentication (2FA) login
security methods <https://pyfound.blogspot.com/2019/06/pypi-now-supports-two-
factor-login-via.html>`_. We added Time-based One-Time Password (TOTP) support
in late May and physical security device support in mid-June. Now, over 1600
users have started using physical security devices or TOTP applications to
better secure their accounts. And over the past week, over 7.8% of logins to
PyPI.org have been protected by 2FA, up from 3% in the month of June.  
  
`![Add API token screen, with textarea for token name and dropdown menu to
choose token
scope <https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjLsALmRLrg2KqlfIsOyaVfnV63oojYz3Qz6Qij6jM3Q5whuB3fRnCibnL4aaxSvy83Y2YFIomWtNFzs_n3Okgmy11IgK6E9_-4TWXVbs-r8Tg84UmZo2RoTaJ0No0NTI_kOg/s400/creating-
api-token-
pypi.png>`_](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjLsALmRLrg2KqlfIsOyaVfnV63oojYz3Qz6Qij6jM3Q5whuB3fRnCibnL4aaxSvy83Y2YFIomWtNFzs_n3Okgmy11IgK6E9_-4TWXVbs-r8Tg84UmZo2RoTaJ0No0NTI_kOg/s1600/creating-
api-token-pypi.png)  
---  
PyPI interface for adding an  
API token for package upload  
Now, we have another improvement: `you can use API tokens to upload
packages <https://pypi.org/help/#apitoken>`_ to PyPI and `Test
PyPI <https://packaging.python.org/guides/using-testpypi/>`_! And we've designed
the token to be a drop-in replacement for the username and password you
already use (warning: this is a *beta feature* that `we need your help to
test <https://wiki.python.org/psf/WarehousePackageMaintainerTesting>`_).  
  
*How it works:* Go to your `PyPI account
settings <https://pypi.org/manage/account/#two-factor>`_ and select "Add API
token". When you create an API token, you choose its scope: you can create a
token that can upload to all the projects you maintain or own, or you can
limit its scope to just one project.  
  
  
`![API token management interface displays each token's name, scope, date/time
created, and date/time last used, and the user can view each token's unique ID
or revoke
it <https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj5vY5SBPdrsGckuuhb_Lrdgo1p3Mmv9ZLwZGuu7-VaWL1TlwJj4zj93BGN6yGmvgv-f3VuzY6g_DLnneqqkM7AlO-
PUQ96mJAS-6VI7lK_jtqnxQMiZtnMCI0ksixU7RRPoQ/s320/pypi-api-token-
management.png>`_](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj5vY5SBPdrsGckuuhb_Lrdgo1p3Mmv9ZLwZGuu7-VaWL1TlwJj4zj93BGN6yGmvgv-f3VuzY6g_DLnneqqkM7AlO-
PUQ96mJAS-6VI7lK_jtqnxQMiZtnMCI0ksixU7RRPoQ/s1600/pypi-api-token-
management.png)  
---  
PyPI API token management interface  
The token management screen shows you when each of your tokens were created,
and last used. And you can revoke one token without revoking others, and
without having to change your password on PyPI and in configuration files.  
  
Uploading with an API token is currently optional but encouraged; in the
future, PyPI will set and enforce a policy requiring users with two-factor
authentication enabled to use API tokens to upload (rather than just their
password sans second factor). Watch `our announcement mailing
list <https://mail.python.org/mailman3/lists/pypi-announce.python.org/>`_ for
future details.  
  
`![A successful API token creation: a long string that only appears once, for
the user to
copy <https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhTfHYFcBIrx5iiIvmdQD4PEurEdmM5il3Ez8ti1DZmdObMPJ2gHt2G5O_Y8Y1Kiy8sL6pbTfHgsF78Ts_3J1BwA9kYIMYJGgSXnDOAlTC1g3bVw1a-BHHhXMYpnOXYgcXntg/s400/pypi-
api-token-just-
created.png>`_](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhTfHYFcBIrx5iiIvmdQD4PEurEdmM5il3Ez8ti1DZmdObMPJ2gHt2G5O_Y8Y1Kiy8sL6pbTfHgsF78Ts_3J1BwA9kYIMYJGgSXnDOAlTC1g3bVw1a-BHHhXMYpnOXYgcXntg/s1600/pypi-
api-token-just-created.png)  
---  
Immediately after creating the API token,  
PyPI gives the user one chance to copy it|  
  
*Why:* These API tokens can *only* be used to upload packages to PyPI, and
not to log in more generally. This makes it safer to automate package upload
and store the credential in the cloud, since a thief who copies the token
won't also gain the ability to delete the project, delete old releases, or add
or remove collaborators. And, since the token is a long character string (with
32 bytes of entropy and a service identifier) that PyPI has securely generated
on the server side, we vastly reduce the potential for credential reuse on
other sites and for a bad actor to guess the token.  
  
  
*Help us test:* Please `try this
out <https://wiki.python.org/psf/WarehousePackageMaintainerTesting>`_! This is a
`beta feature <https://wiki.python.org/psf/WarehousePackageMaintainerTesting>`_
and we expect that users will find minor issues over the next few weeks; we
ask for your bug reports. If you find any potential security vulnerabilities,
please follow our `published security policy <https://pypi.org/security/>`_.
(Please don't report security issues in Warehouse via GitHub, IRC, or mailing
lists. Instead, please directly email security@python.org.) If you find an
issue that is not a security vulnerability, please `report it via
GitHub <https://github.com/pypa/warehouse/issues/new>`_.  
  
We'd particularly like testing from:  

  * Organizations that automate uploads using continuous integration
  * People who save PyPI credentials in a `.pypirc` file
  * Windows users
  * People on mobile devices
  * People on very slow connections
  * Organizations where users share an auth token within a group
  * Projects with 4+ maintainers or owners
  * People who usually block cookies and JavaScript
  * People who maintain 20+ projects
  * People who created their PyPI account 6+ years ago

*What's next for PyPI:* Next, we'll move on to working on an advanced audit
trail of sensitive user actions, plus improvements to accessibility and
localization for PyPI (some of which have already started). More details are
in `our progress reports on Discourse <https://discuss.python.org/t/pypi-
security-work-multifactor-auth-progress-help-needed/1042>`_.  
  
Thanks to the `Open Technology Fund <https://www.opentech.fund/>`_ for funding
this work. And please sign up for the `PyPI Announcement Mailing
List <https://mail.python.org/mailman3/lists/pypi-announce.python.org/>`_ for
future updates.

