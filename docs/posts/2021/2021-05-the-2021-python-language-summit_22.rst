.. post:: 2021-05-22
   :tags: post, legacy-blogger
   :author: Python Software Foundation
   :category: Legacy
   :location: World
   :language: en

The 2021 Python Language Summit: Lightning Talks, Round 1
=========================================================

*This was originally posted on blogger* `here <https://pyfound.blogspot.com/2021/05/the-2021-python-language-summit_22.html>`_.

The first day of the `2021 Python Language
Summit <https://pyfound.blogspot.com/2021/05/the-2021-python-language-
summit.html>`_ finished with a series of lightning talks from `Petr
Viktorin <https://twitter.com/EnCuKou>`_, `Lorena
Mesa <https://twitter.com/loooorenanicole>`_, `Scott
Shawcroft <https://twitter.com/tannewt>`_, and `Jeff
Allen <https://github.com/jeff5>`_.

`![Petr Viktorin, Lorena Mesa, and Scott
Shawcroft <https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgz6bG0qGtvuAFKP6Gvm4DBlYoC8K0L9SCndFs_iM7jwcBYsjnMUkp9RNq97wbNWqIdWDPuwg_zmCrt1QaN2MNO4L0EJA8UZNgm-
Xb7e6A2OKlP5Nz4j-DKGjlhQNVFO7eDDbA/s16000/lightning-1.png>`_](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgz6bG0qGtvuAFKP6Gvm4DBlYoC8K0L9SCndFs_iM7jwcBYsjnMUkp9RNq97wbNWqIdWDPuwg_zmCrt1QaN2MNO4L0EJA8UZNgm-
Xb7e6A2OKlP5Nz4j-DKGjlhQNVFO7eDDbA/s500/lightning-1.png)



The Stable ABI and Limited C API
--------------------------------

Petr Viktorin spoke about the stable ABI and limited C API. The stable ABI is
a way to compile a C extension on Python 3.x and run it on Python 3.x+. It was
introduced in 2009 with `PEP 384 <https://www.python.org/dev/peps/pep-0384/>`_.
You can use it to simplify extension maintenance, and it will allow you to
support more versions. But it does have lower performance, and you can't do
everything with it that you could with the full API.

Petr Viktorin would like to see it used for bindings and embeddings. If Python
is just a small part of your application and you don't want to invest a lot of
maintainer time into supporting Python, then that would be a good use case.
You could also use it to support unreleased Python versions.

If you limit yourself to the subset of the limited C API, then you will get an
extension that conforms to the stable ABI. The limited C API aims to avoid
implementation details and play well with:

  * Alternate Python implementations
  * Extension languages other than C
  * New features, such as isolated subinterpreters

However, the limited C API is not stable.

The limited C API and the stable ABI are now defined in Misc/stable_abi.txt.
There are already tests, and soon there will be documentation as well. To
learn more, check out:

  * `The dev guide <https://devguide.python.org/c-api/>`_
  * `The user guide <https://docs.python.org/3.11/c-api/stable.html>`_

  

Promoting PyLadies in CPython Development
-----------------------------------------

Lorena Mesa spoke about `PyLadies <https://pyladies.com/>`_, which is an
international mentorship group with a focus on helping more women become
active participants and leaders in the Python open-source community.

Most of the growth in the PyLadies community has been coming from outside the
USA and Europe. South America has the most active chapters, with Brazil in the
lead. In order to help chapters better support their members, PyLadies is
working on a centralized mandate and a global governance model.

While PyLadies has been working on education and outreach, it has been
challenging to quantify how the group is helping women become active
participants and leaders in the OSS community. In order to address this issue,
they are preparing a survey about the challenges their members face in open
source. Members may be having difficulty with:

  * Language barriers
  * Technical expertise
  * Support

PyLadies will be launching a video series on how to be a contributor and would
like to hear from core developers who could:

  * Submit a recording of their workflow to publish on YouTube
  * Offer feedback

If you'd like to participate, you can `get in
touch <https://forms.gle/6eCucMpQXNnLo9ke9>`_.



CircuitPython: A Subset of CPython  
------------------------------------



CircuitPython is a much smaller version of Python that runs on
microcontrollers. Scott Shawcroft compared what's included in CircuitPython
and CPython to give a sense of what is central to users' experience of Python.  



Although CircuitPython is 650 kilobytes compared to CPython's 29 megabytes, it
still feels like Python. It is intended to be a strict subset of CPython that
allows people to learn Python on microcontrollers and then graduate to CPython
on a Linux computer without having to rework too much of their code.  

  

Scott Shawcroft compared lists of modules and built-ins in CircuitPython and
CPython to show that CircuitPython doesn't need to have much to still feel
like Python. You need to have the built-ins and the syntax, but not
necessarily all of the standard library. This is great news because, with a
smaller core, you can bring Python to smaller devices.



However, CPython users who have come to CircuitPython have asked for NumPy,
f-strings, pandas, Jupyter, pdb, and asyncio to be added. Interestingly, even
though some of their requests go beyond core Python, users still associate
them with their experience of Python. If that's the case, then maybe we don't
need to be afraid to take elements of core Python and move them into packages
because, at the end of the day, people still consider them to be Python.

  

Jython 3: Something Completely Different?
-----------------------------------------



Jeff Allen shared the approach he's advancing for the Jython 3 core, which is
quite different from Jython 2. He's been slowly working on his ideas outside
of the official repo and wanted feedback to help identify potential problem
areas before he starts working in the official repo.

  

He has already solved some more daunting problems, such as:

  * Inheritance
  * Descriptors
  * Built-in methods, but not yet their call sites
  * An interpreter for a subset of CPython bytecode



There is still a lot to do, but he hasn't had to go back to square one
recently. However, there may still be bigger problems with Java integration,
exceptions, and async. He asked for feedback about any other potential
pitfalls he may not have seen yet.  

