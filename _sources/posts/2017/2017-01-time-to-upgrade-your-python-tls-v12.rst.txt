.. post:: 2017-01-31
   :tags: post, pypi, legacy-blogger
   :author: Python Software Foundation
   :category: Legacy
   :location: World
   :language: en

Time To Upgrade Your Python: TLS v1.2 Will Soon Be Mandatory
============================================================

*This was originally posted on blogger* `here <https://pyfound.blogspot.com/2017/01/time-to-upgrade-your-python-tls-v12.html>`_.

If you're using an older Python without the most secure TLS implementation,
this is the year to get serious about upgrading. Otherwise next June you may
not be able to "pip install" packages from PyPI.  
  
PyPI's maintainer Donald Stufft `recently
announced <https://mail.python.org/pipermail/distutils-
sig/2017-January/029970.html>`_ that python.org and related sites will begin
disabling the old TLS versions 1.0 and 1.1. This change was imposed on us by
our content delivery network, Fastly, in response to `a change imposed on them
by the Payment Card Industry Security Standards
Council <https://www.pcisecuritystandards.org/pdfs/15_12_18_SSL_Webinar_Press_Release_FINAL.pdf>`_.
In order to continue serving websites that take credit card payments, Fastly
is required to disable the old, insecure versions of TLS. Since the PSF's
servers, including PyPI, use Fastly, the old versions of TLS will be disabled
as well.  
  
`Fastly wrote in October 2015 <https://www.fastly.com/blog/securing-online-
transactions-announcing-our-plan-tls-10-and-11-deprecation>`_,  

> There have been serious and systemic security issues with earlier versions
> of TLS and its predecessor, SSL, including POODLE, Heartbleed, and LOGJAM.
> These threatened to break trust in fundamental methods of secure
> communication, exposing both you and your customers to breaches in security.
> The actions of the PCI DSS Council to maintain a high minimum bar are a step
> towards ensuring the security of all online business transactions.

There are two deadlines to upgrade your Python to a version with the latest
TLS. The first comes soon, on April 30, 2017, when python.org sites without
`Extended Validation
Certificates <https://en.wikipedia.org/wiki/Extended_Validation_Certificate>`_
will stop supporting TLS 1.0 and 1.1. These sites include:  
  

  * testpypi.python.org
  * test.pypi.org
  * files.pythonhosted.org

  
`Warehouse <https://pypi.org/>`_, the future successor to PyPI, will also be
affected by April's deadline, since Warehouse serves files from
files.pythonhosted.org.  
  
The more crucial deadline comes June 30, 2018. On that date all remaining
python.org sites, including PyPI, will no longer support TSL 1.0 and 1.1.
Older Python versions that do not implement TLSv1.2 will be prohibited from
accessing PyPI.  
  
See below for instructions to check your interpreter's TLS version.
`1 <https://www.blogger.com/blogger.g?blogID=8520#1>`_  
  
Stufft writes, "I am going to see about possibly organizing some scheduled
'brown outs' of TLSv1.0 and TLSv1.1 prior to the cut off dates to try and help
folks find places that will need updates. Any scheduled brownouts will be
posted to status.python.org prior to happening."  
  
Mac users should pay special attention. So far, the system Python shipped with
MacOS does not yet support TLSv1.2 in any MacOS version; beginning next June
these system Pythons will no longer be able to "pip install" packages.
`2 <https://www.blogger.com/blogger.g?blogID=8520#2>`_ Fortunately, it's easy to
install a modern Python alongside the MacOS system Python. Either `download
Python 3.6 from python.org <https://www.python.org/downloads/>`_, or for `Python
2.7 with the latest TLS, use Homebrew <http://docs.python-
guide.org/en/latest/starting/install/osx/>`_. Both methods of installing Python
will continue working after June 2018.  
  

* * *

  
`*1.* <https://www.blogger.com/blogger.g?blogID=8520#top1>`_ To check your
Python interpreter's TLS version, install the "requests" package and run a
command. For example, for Python 2:  
  

python2 -m pip install --upgrade requests  
python2 -c "import requests;
print(requests.get('https://www.howsmyssl.com/a/check',
verify=False).json()['tls_version'])"

  
Or Python 3:  
  

python3 -m pip install --upgrade requests  
python3 -c "import requests;
print(requests.get('https://www.howsmyssl.com/a/check',
verify=False).json()['tls_version'])"

  
If you see "TLS 1.2", your interpreter's TLS is up to date. If you see "TLS
1.0" or an error like "tlsv1 alert protocol version", then you must upgrade.
`↩ <https://www.blogger.com/top1>`_  
  
`*2.* <https://www.blogger.com/blogger.g?blogID=8520#top2>`_ The reason
Python's TLS implementation is falling behind on macOS is that Python
continues to use OpenSSL, which Apple has stopped updating on macOS. In the
coming year, the Python Packaging Authority team will investigate porting pip
to Apple's own "SecureTransport" library as an alternative to OpenSSL, which
would allow old Python interpreters to use modern TLS with pip only. "This is
a non-trivial amount of effort," writes Stufft, "I'm not sure it's going to
get done."  
  
In the long run, the Python interpreter itself would easily keep up with TLS
versions, if it didn't use OpenSSL on platforms like macOS and Windows where
OpenSSL is not shipped with the OS. Cory Benfield and Christian Heimes propose
to redesign the standard library's TLS interfaces to make it easier to swap
OpenSSL with platform-native TLS implementations.
`↩ <https://www.blogger.com/blogger.g?blogID=8520#top2>`_

