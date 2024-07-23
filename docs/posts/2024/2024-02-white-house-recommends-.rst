.. post:: 2024-02-29
   :tags: post, legacy-blogger
   :author: Python Software Foundation
   :category: Legacy
   :location: World
   :language: en

White House recommends use of memory-safe languages like Python
===============================================================

*This was originally posted on blogger* `here <https://pyfound.blogspot.com/2024/02/white-house-recommends-.html>`_.

Earlier this week the White House `published a
report <https://www.whitehouse.gov/oncd/briefing-room/2024/02/26/press-
release-technical-report/>`_ recommending the use of memory-safe programming
languages to eliminate an entire class of vulnerabilities affecting software.
The report quotes claims from large software producers like Google and
Microsoft which estimate that *70% of vulnerabilities affecting software are
due to memory-safety issues.*  
  
Back in December of 2023, the Cybersecurity and Infrastructure Security Agency
(CISA) `published a report <https://www.nsa.gov/Press-Room/Press-Releases-
Statements/Press-Release-View/Article/3608324/us-and-international-partners-
issue-recommendations-to-secure-software-products/>`_ that included a list of
memory-safe programming languages, *among them was the Python programming
language*.

The Python Software Foundation’s `response to the US Government's Request for
Information <https://www.regulations.gov/comment/ONCD-2023-0002-0107>`_ noted
Python's memory-safety and ability to wrap code written in C, C++, and Rust
among other systems languages. Part of Python’s popularity stems from the
large number of community-maintained packages using this feature for
performance, wrapping existing libraries, and low-level API access.

`Cryptography <https://github.com/pyca/cryptography>`_ is one of the most
depended on Python libraries for cryptographic primitives, installed nearly 10
million times per day. `Cryptography started migrating from using C to
Rust <https://mail.python.org/pipermail/cryptography-
dev/2020-December/000998.html>`_ for security reasons in 2020 and made the first
release with Rust binary extensions in 2021. You can listen to maintainers
Paul Kehrer and Alex Gaynor `discuss this non-trivial migration in their PyCon
2022 talk <https://www.youtube.com/watch?v=z_Eiy2W0APU>`_.  
  
The migration of the cryptography library included tools like
`PyO3 <https://pyo3.rs>`_ and `setuptools-
rust <https://github.com/PyO3/setuptools-rust>`_ that enable easier adoption of
Rust binary extensions. There’s already plenty of buzz for using Rust and
Python together, the adoption of Rust in Python packages is *`steadily
increasing <https://sethmlarson.dev/security-developer-in-residence-weekly-
report-18#querying-the-dataset>`_ from the single digits in 2020 to today with
hundreds of packages using Rust.*  
  
There are many opportunities to learn about writing Python binary extensions
using Rust, for example, at `PyCon US 2024 <https://us.pycon.org/2024>`_ there
will be a `tutorial about getting started with
PyO3 <https://us.pycon.org/2024/schedule/presentation/113/>`_ and a `talk on
PyO3 and maturin <https://us.pycon.org/2024/schedule/presentation/89/>`_, a `PEP
517 build backend for Rust <https://github.com/PyO3/maturin>`_ by a maintainer
of the PyO3 project.  
  
Historically Python binary extensions were built mostly using C and C++
meaning there are many projects which, for reasons like backwards
compatibility or lack of resources and time, cannot or do not want to migrate
to Rust. For these projects, the use of compiler options can harden binaries
against some memory safety issues. The OpenSSF Best Practices working group
has `published a list of compiler options <https://best.openssf.org/Compiler-
Hardening-Guides/Compiler-Options-Hardening-Guide-for-C-and-C++>`_ to consider
adopting in order to harden builds of C and C++ code.  
  
There is still much work to be done to secure the Python ecosystem and it
can’t be done without our amazing community of contributors and maintainers.
We look forward to more investment in this area as part of the industries’
adoption of memory-safe programming languages. If you are interested in being
part of conversations around improving security in Python, we invite you to
open a thread on `discuss.python.org <https://discuss.python.org/>`_.  
  

