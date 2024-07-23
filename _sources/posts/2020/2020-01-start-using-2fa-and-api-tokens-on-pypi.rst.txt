.. post:: 2020-01-17
   :tags: post, pypi, legacy-blogger
   :author: Python Software Foundation
   :category: Legacy
   :location: World
   :language: en

Start using 2FA and API tokens on PyPI
======================================

*This was originally posted on blogger* `here <https://pyfound.blogspot.com/2020/01/start-using-2fa-and-api-tokens-on-pypi.html>`_.

To increase the security of `PyPI <https://pypi.org/>`_ downloads, we have added
two-factor authentication (2FA) as a login security option, and API tokens for
uploading packages. This is thanks to a `grant from the Open Technology
Fund <https://pyfound.blogspot.com/2019/03/commencing-security-accessibility-
and.html>`_, coordinated by the `Packaging Working
Group <https://wiki.python.org/psf/PackagingWG>`_ of the `Python Software
Foundation <https://www.python.org/psf-landing/>`_.  
  
If you maintain or own a project on `the Python Package
Index <https://pypi.org/>`_, you should start using these features. `Click
"help" on PyPI <https://pypi.org/help/>`_ for instructions. (These features are
also available `on Test PyPI <https://packaging.python.org/guides/using-
testpypi/>`_.)  
  
Details and plans for the future:  
  
*2FA:*  
  
` Two-factor authentication (2FA) <https://pypi.org/help/#twofa>`_ makes your
account more secure by requiring two things in order to log in: _something you
know_ and _something you own_.  
  
In PyPI's case, "something you know" is your username and password, while
"something you own" can be `an application to generate a temporary
code <https://pypi.org/help/#totp>`_, or a `security
device <https://pypi.org/help/#utfkey>`_ (most commonly a USB key).  
  
_Why?_ This will help improve the security of your PyPI user accounts, and
thus reduce the risk of vandals, spammers, and thieves gaining account access.
Protecting login via the website safeguards against malicious changes to
project ownership, deletion of old releases, and account takeovers.  
  
PyPI's implementation of the `WebAuthn
standard <https://www.w3.org/TR/webauthn/ "External link">`_ and the `TOTP
standard <https://en.wikipedia.org/wiki/Time-based_One-time_Password_algorithm
"External link">`_ mean you can use `any TOTP authentication
application <https://pypi.org/help/#totp>`_ and/or any 2FA device `that meets
the FIDO standard <https://fidoalliance.org/certification/fido-certified-
products/ "External link">`_. (`We launched WebAuthn support last
year <https://blog.python.org/2019/06/pypi-now-supports-two-factor-login-
via.html>`_; this week it comes out of beta.)  
  
Go to your account settings to add a second factor.  
`![ <https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi3GfHeSEb501PCUZPCgQ2e7hJNd0Hrm301iapUtmEuZUAmU-9WdMmLxs4SYHFNSLSTMufcfOV6ERgvjMAxRxgLD586EjeawJo8OHwvEuBC6TC_BUYCzQFVUGepndDth-1-q5s/s320/2fa-
not-
enabled-17-june-2019.png>`_](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi3GfHeSEb501PCUZPCgQ2e7hJNd0Hrm301iapUtmEuZUAmU-9WdMmLxs4SYHFNSLSTMufcfOV6ERgvjMAxRxgLD586EjeawJo8OHwvEuBC6TC_BUYCzQFVUGepndDth-1-q5s/s1600/2fa-
not-enabled-17-june-2019.png)  
---  
Add a second factor in your account settings.  
  
`![ <https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhNgHqMyFZ_mcmNtFyBjqFfJ-T8N7cm6_qZJR1VxS6tIGfwUp0RTwM3AjpBLQnFnRP1zv-
AhQWj4pWKKWxt4CehIw53Ao7oXgXbHGbN3U-2eqDpU3IbV-
YKaFMaWYtptprqMy0/s320/2fa-u2f-screenshot-
june-17-2019.png>`_](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhNgHqMyFZ_mcmNtFyBjqFfJ-T8N7cm6_qZJR1VxS6tIGfwUp0RTwM3AjpBLQnFnRP1zv-
AhQWj4pWKKWxt4CehIw53Ao7oXgXbHGbN3U-2eqDpU3IbV-
YKaFMaWYtptprqMy0/s1600/2fa-u2f-screenshot-june-17-2019.png)  
---  
Create a key name in the PyPI interface.  
2FA only affects logging in via a web browser, and not (yet) package uploads.  
  
*API tokens:*  
  
`![ <https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiOaFaQtilTZVu3TW3P9I0WYrCyh04rzG_p3kIaE_EamQ0eWpena_8EfCUCr74DyeVc2EkCthqoVDHFn-
QEN3R6LGwjFMoQ68FhanrHlGpE8bRrbx4x85nLgg8PM6tDak-laQ/s320/pypi-2fa-api-tokens-
in-
settings.png>`_](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiOaFaQtilTZVu3TW3P9I0WYrCyh04rzG_p3kIaE_EamQ0eWpena_8EfCUCr74DyeVc2EkCthqoVDHFn-
QEN3R6LGwjFMoQ68FhanrHlGpE8bRrbx4x85nLgg8PM6tDak-laQ/s1600/pypi-2fa-api-
tokens-in-settings.png)  
---  
In your Account Settings,  
select "Add API token".  
`API tokens <https://pypi.org/help/#apitoken>`_ provide an alternative way
(instead of username and password) to authenticate when *uploading packages*
to PyPI. (`We launched API token support last
year <https://blog.python.org/2019/07/pypi-now-supports-uploading-via-
api.html>`_; this week it comes out of beta.)  
  
`![ <https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjLsALmRLrg2KqlfIsOyaVfnV63oojYz3Qz6Qij6jM3Q5whuB3fRnCibnL4aaxSvy83Y2YFIomWtNFzs_n3Okgmy11IgK6E9_-4TWXVbs-r8Tg84UmZo2RoTaJ0No0NTI_kOg/s320/creating-
api-token-
pypi.png>`_](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjLsALmRLrg2KqlfIsOyaVfnV63oojYz3Qz6Qij6jM3Q5whuB3fRnCibnL4aaxSvy83Y2YFIomWtNFzs_n3Okgmy11IgK6E9_-4TWXVbs-r8Tg84UmZo2RoTaJ0No0NTI_kOg/s1600/creating-
api-token-pypi.png)  
---  
PyPI interface for adding an  
API token for package upload.  
  
  
`![ <https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhTfHYFcBIrx5iiIvmdQD4PEurEdmM5il3Ez8ti1DZmdObMPJ2gHt2G5O_Y8Y1Kiy8sL6pbTfHgsF78Ts_3J1BwA9kYIMYJGgSXnDOAlTC1g3bVw1a-BHHhXMYpnOXYgcXntg/s320/pypi-
api-token-just-
created.png>`_](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhTfHYFcBIrx5iiIvmdQD4PEurEdmM5il3Ez8ti1DZmdObMPJ2gHt2G5O_Y8Y1Kiy8sL6pbTfHgsF78Ts_3J1BwA9kYIMYJGgSXnDOAlTC1g3bVw1a-BHHhXMYpnOXYgcXntg/s1600/pypi-
api-token-just-created.png)  
---  
Immediately after creating the API token,  
PyPI gives the user one chance to copy it.  
_Why?_** These API tokens can *only*  be used to upload packages to PyPI,
and not to log in more generally. This makes it safer to automate package
upload and store the credential in the cloud, since a thief who copies the
token won't also gain the ability to delete the project, delete old releases,
or add or remove collaborators. And, since the token is a long character
string (with 32 bytes of entropy and a service identifier) that PyPI has
securely generated on the server side, we vastly reduce the potential for
credential reuse on other sites and for a bad actor to guess the token.  
  
You can create a token for an entire PyPI user account, in which case, the
token will work for all projects associated with that account. Alternatively,
you can limit a token's scope to a specific project. That way, if a token is
compromised, you can just revoke and recreate that token, instead of having to
change your password in lots of automated processes.  
`![ <https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj5vY5SBPdrsGckuuhb_Lrdgo1p3Mmv9ZLwZGuu7-VaWL1TlwJj4zj93BGN6yGmvgv-f3VuzY6g_DLnneqqkM7AlO-
PUQ96mJAS-6VI7lK_jtqnxQMiZtnMCI0ksixU7RRPoQ/s320/pypi-api-token-
management.png>`_](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj5vY5SBPdrsGckuuhb_Lrdgo1p3Mmv9ZLwZGuu7-VaWL1TlwJj4zj93BGN6yGmvgv-f3VuzY6g_DLnneqqkM7AlO-
PUQ96mJAS-6VI7lK_jtqnxQMiZtnMCI0ksixU7RRPoQ/s1600/pypi-api-token-
management.png)  
---  
PyPI token management interface  
  
Go to your account settings to add an API token. * *  
  
*Future:*  
  
In the future, PyPI will set and enforce a policy requiring users with two-
factor authentication enabled to use API tokens to upload (rather than just
their password, without a second factor). We do not yet know when we will make
this policy change. When we do, `we'll announce
it <https://pypi.org/help/#upcoming-changes>`_.  
  
*Thanks:*  
  
Thanks to the Open Technology Fund for `funding this
work <https://www.opentech.fund/results/supported-projects/pypi-
improvements/>`_.  
  
More donor-funded work is in progress on pip and PyPI, via `the PSF's
Packaging Working Group <https://wiki.python.org/psf/PackagingWG>`_. Please sign
up for the `PyPI Announcement Mailing
List <https://mail.python.org/mailman3/lists/pypi-announce.python.org/>`_ for
future updates.  

  *[WebAuthn]: web authentication
  *[TOTP]: time-based one-time password

