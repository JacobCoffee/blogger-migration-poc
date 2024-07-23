.. post:: 2020-04-30
   :tags: post, legacy-blogger
   :author: Python Software Foundation
   :category: Legacy
   :location: World
   :language: en

Lightning Talks Part 1 - Python Language Summit 2020
====================================================

*This was originally posted on blogger* `here <https://pyfound.blogspot.com/2020/04/lightning-talks-part-1.html>`_.

`![ <https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEigrdUbEgJgVDmnOPtQJ_G_t5RHXIWNOBc9XENxkES5nQh3-TpHFZ89eW_LP3tAfAENJvt9OV3j2ib6JUB4NzF_Yz_0trMO1Y8gl6izl-3VuEIvm8zGl69KJ5G3zUlvpY4Myw/s1600/sumana-
and-eric-
snow.jpg>`_](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEigrdUbEgJgVDmnOPtQJ_G_t5RHXIWNOBc9XENxkES5nQh3-TpHFZ89eW_LP3tAfAENJvt9OV3j2ib6JUB4NzF_Yz_0trMO1Y8gl6izl-3VuEIvm8zGl69KJ5G3zUlvpY4Myw/s1600/sumana-
and-eric-snow.jpg)  

Sumana Harihareswara
--------------------

What do you need from pip, PyPI, and packaging?
===============================================

  
Python packaging has seen relatively quick development in recent years as a
result of increased funding; most famously the new
`PyPI.org <https://pypi.org/>`_ website was launched in 2018. The current work
in progress includes `malware
detection <https://pyfound.blogspot.com/2018/12/upcoming-pypi-improvements-
for-2019.html>`_ and `signed
packages <https://www.python.org/dev/peps/pep-0458/>`_ on PyPI, a new dependency
resolver for pip, and a revamp of virtualenv. Much of this work is funded by
grants from companies. (`Details on the Working Group
page <https://wiki.python.org/psf/Fundable%20Packaging%20Improvements>`_.)
Sumana Harihareswara from the `Packaging Working
Group <https://wiki.python.org/psf/PackagingWG>`_ is a prolific grant proposal
writer; she `presented ideas for further
development <https://www.harihareswara.net/need-from-pip.pdf>`_.  
  
`Read more 2020 Python Language Summit
coverage <https://pyfound.blogspot.com/2020/04/the-2020-python-language-
summit.html>`_.  

* * *

Python packaging ideas for the future include:  
  

  * Better specifications, toolchain, and services for building distributions  

  * Robust interoperability testing  

  * Revamp PyPI API  

  * Make setuptools the reference implementation of the distutils API  

  * Provide more standardized editable installations  

  * Add support for pyproject.toml as a way to configure setuptools  

  * `Create & maintain a generic wheel-builder <https://github.com/pypa/packaging-problems/issues/25>`_  

  * `PEP 480: secure the developer-to-user supply chain  <https://www.python.org/dev/peps/pep-0480/>`_  

  * `Implement perennial manylinux (PEP 600) <https://discuss.python.org/t/pep-600-future-manylinux-platform-tags-for-portable-linux-built-distributions/2414/>`_
  

Harihareswara solicited packaging ideas from the audience to inform the
`Python Packaging Authority roadmap <https://www.pypa.io/en/latest/roadmap/>`_
and the `Fundable Packaging
Improvements <https://wiki.python.org/psf/Fundable%20Packaging%20Improvements>`_
page, asked them to add their complaints to the `packaging problems
list <https://github.com/pypa/packaging-problems/issues>`_, and requested help
writing grant proposals.  
  
Since Harihareswara had listed a `revamp of
virtualenv <https://discuss.python.org/t/virtualenv-20-0-0-beta1-is-
available/3077>`_ among the works in progress, Barry Warsaw wondered what
advantages virtualenv has over venv, which is now built in to all supported
Python versions. Bernat Gabor, who maintains virtualenv, answered that
virtualenv is faster, provides a richer API for tools built on it, and serves
as a laboratory for ideas that might be merged into venv.  
  
Ernest W. Durbin III provided a status update on malware checking: the
`framework is in place <https://warehouse.readthedocs.io/development/malware-
checks/>`_ but only two checks have been implemented, "mainly for
demonstration." He has invited security researchers to implement more checks.  
  
David Mertz asked whether pip's new dependency resolver would be able to
resolve dependency conflicts. Paul Moore said he is still researching what
users want pip to do in the case of conflicts, and what solutions are provided
by resolver algorithms. The new resolver is about to be released, but it is
still alpha-level and will be turned off by default.  
  

Eric Snow
---------

A Retrospective on My "Multi-Core Python" Project
=================================================

  
Of all the schemes for freeing CPython from the Global Interpreter Lock, the
frontrunner is Eric Snow's plan to give each subinterpreter its own lock. He
`proposed the idea in 2015 <https://mail.python.org/pipermail/python-
ideas/2015-June/034177.html>`_, began discussing and prototyping the idea
intensely, and burned out the next year. "I was trying to do too much on my
own," said Snow. In 2017 he resumed development, this time with dozens of
collaborators, and `wrote PEP 554 to expose subinterpreters to pure Python
programs <https://www.python.org/dev/peps/pep-0554/>`_, which will ease testing
for the multi-core project. `He presented his progress to the Language Summit
in 2018 <https://lwn.net/Articles/754162/>`_ and in a `2019 PyCon
talk <https://www.youtube.com/watch?v=7RlqbHCCVyc>`_. His `TalkPython
interview <https://talkpython.fm/episodes/show/225/can-subinterpreters-free-
us-from-pythons-gil>`_ last year was especially effective at drawing attention
to the project.  
  
Snow's immediate blocker is PEP 554's acceptance and implementation, but much
work remains after that. He told the 2020 Language Summit, "I've just been
chugging along, little by little. Lots of _little_ pieces to get this project
done!" Hard problems include passing data safely between subinterpreters, the
"grind" of removing all the global variables, and reaching the actual goal:
creating a distinct GIL per subinterpreter. Snow predicts the split GIL won't
land in Python 3.9, but "3.10 for sure."  
  
Snow thanked a large list of contributors, many of them outside the core
developer team.  
  
Kyle Stanley asked whether daemon threads should be still be allowed in
subinterpreters or not. (Victor Stinner `tried to ban
them <https://bugs.python.org/issue37266>`_ but had to revert his change.) Snow
replied that daemon threads in subinterpreters lead to many finalization
problems, and their use should be discouraged, but removing them entirely has
proven too disruptive for the core team to accomplish any time soon.

