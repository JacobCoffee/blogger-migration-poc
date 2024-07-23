.. post:: 2021-05-23
   :tags: post, legacy-blogger
   :author: Python Software Foundation
   :category: Legacy
   :location: World
   :language: en

The 2021 Python Language Summit: The Challenges of Packaging Python for a Linux Distro
======================================================================================

*This was originally posted on blogger* `here <https://pyfound.blogspot.com/2021/05/the-2021-python-language-summit_23.html>`_.

`Matthias Klose <https://github.com/doko42>`_ gave a talk about the challenges
of packaging Python for a Linux distribution at the `2021 Python Language
Summit <https://pyfound.blogspot.com/2021/05/the-2021-python-language-
summit.html>`_. He wanted to discuss:

  * CPython sources and how they fit with Debian and Ubuntu
  * Ownership of module installations 
  * Architecture and platform support
  * Inclusiveness and the ubiquity of Python on various platforms
  * Communication issues



What Is Python Like on Debian and Ubuntu?  
-------------------------------------------

He shared what Debian 11 and Ubuntu 21.04 have installed for Python. By
default, there is almost nothing, so it's usually pulled in by various seeds
or images. Linux distributions usually have a mature packaging system and
don't ship naked CPython, unlike macOs or Windows.

These Debian and Ubuntu versions still use Python 2 to bootstrap PyPI, but one
version of Python 3 is also shipped with them. CPython itself is split into
multiple binary packages for license issues, dependencies, development needs,
and cross-buildability needs. There is also a new python3-full package that
includes everything for the batteries-included experience. About twenty
percent of the packages shipped by Debian use Python. He said that this is
usually enough for desktop users but may not be enough for developers.
However, the line between those two groups is not always clear.  

As for the QA that Python is getting in Debian and Ubuntu, for the main part
of the archive, it must conform to the Debian Free Software Guidelines. These
guidelines include free distribution, inclusion of source code, and ability to
modify and create derived works. Packages have to build from source and pass
the upstream test suite as well as CI tests.

What Distro-Specific Decisions Were Made for Debian and Ubuntu?
---------------------------------------------------------------

Debian has a `policy for shipping Python
packages <https://www.debian.org/doc/packaging-manuals/python-policy/>`_ that is
also used by Ubuntu. Usually, applications are in application-specific
locations so they don't get in the way of anything else. They ship modules as
\--single-version-externally-managed, and they are usually shipped only if the
application needs them.

The site-packages directory has been renamed to /usr/lib/python3/dist-packages
and /usr/local/lib/python3.x/dist-packages for local installs. The path
doesn't change during Python upgrades (`PEP
3147 <https://www.python.org/dev/peps/pep-3147/>`_ and `PEP
3149 <https://www.python.org/dev/peps/pep-3149/>`_). Although there are a large
number of packages that use Python, pip is not used in the archive but just
provided for use.

You can't call Python with python, python2, python3.x, or python3. There is no
Python executable name by default to call Python because they just removed
most of the Python 2 stuff. There is a package called python-is-python3 that
reinstalls the Python symlink. That package was a compromise, and there was
some difficulty getting it into Debian.

In the past, there have been license issues with shipping the CPython upstream
sources. There are still license issues with the _dbm module, which is only
buildable with a GPL-3+ license. There were also some executables included in
the sources that were removed for 3.10. The big remaining issue is that wheels
are still included without the source and can't be shipped, so you have to
build them using the regular setuptools and pip distributions. Usually,
symlinks and dependencies are used to point to the proper setuptools and pip
packages.

The relationship between pip and Linux distributions is a difficult one, and
there is more than one way to install Python modules. Part of the motivation
behind renaming site-packages to dist-packages was that pip was breaking
desktop systems. They also wanted to resolve conflicts with locally built
Python (installed in /usr/local).

There has been some controversy about what can break your system:

  * sudo rm -rf /
  * sudo pip install pil
  * sudo apt install python3-pil

PyPA does not consider sudo pip install to be dangerous, but Debian and Ubuntu
have different opinions about how pip should behave. Mixing packages from two
different installers can lead to problems. Although `PEP
517 <https://www.python.org/dev/peps/pep-0517/>`_ appears to say that pip is
only recommended, pip does seem to be enforced more and more. Matthias Klose
joked that perhaps ensurepip should be renamed to enforcepip. He also said
that having some kind of offline mode for pip would help.

He discussed inclusiveness and said that Python being ubiquitous should be
seen as an asset rather than a burden. He was sad to see negative attitudes
towards platforms that are used less, such as AIX, and didn't see why Python
would want to exclude some communities.

What Communication Issues Are There?  
--------------------------------------

In December or November, there were tweets about problems within Debian and
Ubuntu. He considered some of the concerns that were brought up to be valid,
but he said that there were also legal threats made against the Debian project
on behalf of the PSF. He was of the opinion that all parties could improve and
that it wasn't just a Debian or Ubuntu problem.

Here are some of the communication problems he highlighted:

  * Distro issues don't reach distro people.
  * Problems with pip breaking systems don't reach pip developers.
  * There is no single place to discuss PyPA issues.
  * There have been problems with manylinux wheels built for CentOS that came up in distro channels.

He would like to see communication improve and reminded the summit attendees
that no group speaks with a single voice.

