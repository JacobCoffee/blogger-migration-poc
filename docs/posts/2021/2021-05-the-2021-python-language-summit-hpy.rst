.. post:: 2021-05-22
   :tags: post, legacy-blogger
   :author: Python Software Foundation
   :category: Legacy
   :location: World
   :language: en

The 2021 Python Language Summit: HPy — Present and Future
=========================================================

*This was originally posted on blogger* `here <https://pyfound.blogspot.com/2021/05/the-2021-python-language-summit-hpy.html>`_.

At the `2021 Python Language
Summit <https://pyfound.blogspot.com/2021/05/the-2021-python-language-
summit.html>`_, `Antonio Cuni <https://twitter.com/antocuni>`_ gave a presentation
about `HPy <https://hpyproject.org/>`_. He also gave a `presentation about
HPy <https://pyfound.blogspot.com/2020/04/hpy-future-proof-way-of-
extending.html>`_ at the `2020 Python Language
Summit <https://pyfound.blogspot.com/2020/04/the-2020-python-language-
summit.html>`_, so this year he shared updates on how the project has evolved
since then.  

`![Antonio
Cuni <https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh0Vl5V51ib3_WGTnoZDpyzf7WaLfWQDxPZMXNPxD2CIMUcm6hhHrGf6n2hsmIFLjd6GoIlYtWgo1ZZKqG_RypgOjVxV6nzaJ6W3y1WAENlnfkXhZ37af37XMP5g6B31-IT3_Q/w320-h320/antonio-
cuni.png>`_
](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh0Vl5V51ib3_WGTnoZDpyzf7WaLfWQDxPZMXNPxD2CIMUcm6hhHrGf6n2hsmIFLjd6GoIlYtWgo1ZZKqG_RypgOjVxV6nzaJ6W3y1WAENlnfkXhZ37af37XMP5g6B31-IT3_Q/s460/antonio-
cuni.png)



What Is HPy?
------------

HPy is an alternative API for writing C extensions. Although the current
Python C API shows CPython implementation details, HPy hides all the
implementation details that would otherwise be exposed. Antonio Cuni said
that, if everyone used HPy, then it would help Python evolve in the long term.

Using HPy extensions will make it easier to support alternative
implementations. HPy is designed to be GC friendly and isn't build on top of
ref counting. It is also designed to have zero overhead on CPython, so you can
port an existing module from the Python C API to HPy without any performance
loss. In addition, it allows incremental migration, allowing you to port your
existing extension one function at a time, or even one method at a time. HPy
is also faster than the existing Python C API on alternative implementation
such as `PyPy <https://www.pypy.org/>`_ and
`GraalPython <https://www.graalvm.org/python/>`_.

What's New With HPy?  
----------------------

In the past year since Antonio Cuni last shared an update at a Python Language
Summit, HPy has continued to make progress. It now has:

  * Support for Windows
  * Support for creating custom types in C
  * A debug mode to help you find mistakes in your C code
  * Setup tools integration to make it easier to compile HPy extensions    

There has also been work on a very early port of some parts of NumPy to HPy.
The feedback from the NumPy team has been positive so far. Soon, the HPy team
will start writing a Cython backend so that all Cython extensions will be able
to automatically use HPy as well.

The HPy team has made a lot of progress with building community and getting
funding. There is now a `site for HPy <https://hpyproject.org/>`_ as well as a
`blog <https://hpyproject.org/blog/>`_, and there has been a lot of interest and
involvement from the Python community. For example, someone independently
started `porting Pillow <https://github.com/cklein/Pillow-hpy>`_. Oracle, IBM,
and Quansight Labs have provided some funding, but there has still been plenty
of non-funded open source development, as usual.

How Do the CPython ABI and the Universal ABI Compare?  
-------------------------------------------------------

There are some differences between the CPython ABI and the Universal ABI:

`![CPython ABI vs Universal
ABI <https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgrZ9gWAzFZXxeciJBc4TXu0eY6jnsngxo1cEejQ17MewvmwjGEalnwbb1VqggNjdzpyB-
BslOFCnxKYoMVPj-twkomD9MFDwl1Lg-El_WGpEnafnrrRltGxxbagsuO-SLg0GQ/s16000/HPy-
comparison.png>`_](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgrZ9gWAzFZXxeciJBc4TXu0eY6jnsngxo1cEejQ17MewvmwjGEalnwbb1VqggNjdzpyB-
BslOFCnxKYoMVPj-twkomD9MFDwl1Lg-El_WGpEnafnrrRltGxxbagsuO-SLg0GQ/s500/HPy-
comparison.png)

On the Universal ABI side, there is no way to support wheels.

How Does Debug Mode Work?
-------------------------

HPy's debug mode may be useful to you even if you aren't concerned about the
problems that HPy is intended to solve because it can help you find common
problems in your C code, such as memory leaks. Here's an example of an HPy
function that takes an object and increments it by one:

`![ <https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjFGXRXFMSpSt5kF7TiYgTPd75Oi_FTRozH3bMMUCRfW4eH9tEhzxUqQ84T8w5eIdt2Vry0MIrkKgrivBs67VVSXBp313_6ZBn_RGunMC0NftF5yMPc5aunYuhLpoq1o2mgBt0/s16000/debug-1.png>`_](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjFGXRXFMSpSt5kF7TiYgTPd75Oi_FTRozH3bMMUCRfW4eH9tEhzxUqQ84T8w5eIdt2Vry0MIrkKgrivBs67VVSXBp313_6ZBn_RGunMC0NftF5yMPc5aunYuhLpoq1o2mgBt0/s500/debug-1.png)

HPy_Close() isn't called on the object that was created, so you have a memory
leak. If you want to compile this file into an extension, then you can use
setup.py:

`![ <https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhegRSp6zdBadudofVL1Zy5gNOB47O9SZh8yB0clFjlexk6WKkNBIWqj3DfkY-l0Li4m-oM6B62hxLpeh72cDfd-
nX4loAOSy4eM43HUm4nq26eZrdqIbP2jJkktFa1DCRjXYU/s16000/debug-2.png>`_](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhegRSp6zdBadudofVL1Zy5gNOB47O9SZh8yB0clFjlexk6WKkNBIWqj3DfkY-l0Li4m-oM6B62hxLpeh72cDfd-
nX4loAOSy4eM43HUm4nq26eZrdqIbP2jJkktFa1DCRjXYU/s500/debug-2.png)

Now, you can load the module and debug:  

`![ <https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiXElirVP1Xv0-IL3k9-5JRFTbrjVB41bc3h-_IJxn4vfdMxPaa0gB0grjF01XAVm1OhkWrCwZ-
XWnf3RSKttg54VAqasJL3jySPJvjJRxcIjWWd8F6fVEmHu-
VDBv-b7_tHi8/s16000/debug-3.png>`_](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiXElirVP1Xv0-IL3k9-5JRFTbrjVB41bc3h-_IJxn4vfdMxPaa0gB0grjF01XAVm1OhkWrCwZ-
XWnf3RSKttg54VAqasJL3jySPJvjJRxcIjWWd8F6fVEmHu-VDBv-b7_tHi8/s500/debug-3.png)



What Does the Future Hold?
--------------------------

Antonio Cuni closed his presentation by asking the CPython developers at the
summit if it would be possible to make HPy a semi-official API in the future,
with first-class support for importing modules and distributing wheels. Some
attendees suggested writing a PEP to make that happen.  

