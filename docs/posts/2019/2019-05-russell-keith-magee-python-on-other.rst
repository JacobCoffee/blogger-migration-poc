.. post:: 2019-05-15
   :tags: post, legacy-blogger
   :author: Python Software Foundation
   :category: Legacy
   :location: World
   :language: en

Russell Keith-Magee: Python On Other Platforms
==============================================

*This was originally posted on blogger* `here <https://pyfound.blogspot.com/2019/05/russell-keith-magee-python-on-other.html>`_.

Russell Keith-Magee spoke in his capacity as the founder and “Benevolent
Dictator For Now” of the BeeWare Project. The project’s slogan is “Write once.
Deploy everywhere.” The goal of the BeeWare Project is to run Python
applications on Android, iOS, in the browser, even on smart watches, and to
distribute Python applications using platform-specific channels like app
stores. Keith-Magee described a number of obstacles to this goal, and
expressed his hope that the core team would consider these problems when they
plan Python’s future.

  

`Read more 2019 Python Language Summit
coverage <https://pyfound.blogspot.com/2019/05/the-2019-python-language-
summit.html>`_.  
  

`![ <https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhfABvHQyiSdS_y22gMs5qtBmDtas_Tntz734BD8yjOlkzkgTVKSgTgFMZZfwH3iYYk2LYgZL5NSOBDYk_tZvM-1YHQ2SRjBzyhrTTApzLSkhb6AXfaK2dk24bHK7f-upESyg/s1600/russell-
keith-
magee.jpg>`_](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhfABvHQyiSdS_y22gMs5qtBmDtas_Tntz734BD8yjOlkzkgTVKSgTgFMZZfwH3iYYk2LYgZL5NSOBDYk_tZvM-1YHQ2SRjBzyhrTTApzLSkhb6AXfaK2dk24bHK7f-upESyg/s1600/russell-
keith-magee.jpg)

  

  

Cross-Compilation Is Supported And Tested Poorly
================================================

On the server side, x86-64 dominates, but mobile architectures are varied and
rapidly changing. iOS alone has encompassed six architectures in recent
memory: i386, x86-64, arm6, arm7, arm7s and arm64.  
  
To make matters worse, anyone deploying Python to these architectures must
cross-compile, using a desktop or server machine to compile Python and its C
extensions, but designating a mobile architecture as the target. “The good
news,” said Keith-Magee, is that CPython uses Autoconf, and “Autoconf has
really good support for cross compilation baked in. The bad news is that
CPython doesn't so much.” Cross compilation is not tested continuously, and so
it is broken occasionally in CPython’s build configuration. There is a
vendored copy of libffi in the Python source tree, apparently only for
supporting the ctypes module on PowerPC, which makes compilation for iOS even
more difficult.  
  
Distutils and pip present a tougher challenge. They do not support cross-
compilation at all, and assume that the machine on which they run is the
target architecture of the C extensions they compile. Neither do they support
the “fat binary” format required to support multiple iOS architectures in a
single extension module.  
  

OS Differences Break The Test Suite
===================================

Python’s assumptions about system calls are violated, in a variety of ways, on
mobile and web. The most dangerous pitfalls are fork and spawn — they are
provided on iOS but any program that calls them will hang. Large amounts of
code in the Python standard library assume the existence of fork and spawn,
and even more in the test suite.  
  
Some years ago Keith-Magee provided a patch to fix or disable tests as needed
for iOS, but as he recalled, core developer Ned Deily found them “too
invasive.” Instead of changing the test suite so pervasively, a new approach
might be to skip large chunks of the test suite based on platform limitations.  
  

Python Applications Must Include a Python Installation
======================================================

Each Python application on a phone or table OS must ship an entire Python
installation with it, since Python is not available as a system library, and
applications cannot install it in a shared location. “If you've got ten Python
apps on your phone,” says Keith-Magee, “you are going to have ten installs of
Python.” Python for iOS is a fat binary that supports multiple architectures,
weighing around 100 MB in total. Python’s size handicaps browser applications,
too, which cannot begin running until the Python runtime has been loaded.  
  
The Javascript community uses “tree shaking”: Javascript applications are
distributed with the minimum subset of all their dependencies that are
actually required. Keith-Magee proposes a tool that would automatically apply
this technique to the Python standard library. Python builtins or portions of
the interpreter itself could be jettisoned, too. For example, if an
application is distributed as bytecode, then the parser and compiler could be
removed. Keith-Magee said, “While I'm sure that someone has written code that
uses Python's complex number data type, I am not that person, and in all my
apps, the code for complex number handling is dead code.” To write a tool that
would remove such components, however, would require some public API for
editing the runtime and standard library.  
  

asyncio Does Not Integrate With Mobile GUI Events
=================================================

Mobile applications are GUIs, and GUI programming is event-based. Python’s
asyncio is a natural framework for GUI programming, but it must be adapted to
run atop the GUI environment’s own event loop. According to Keith-Magee this
is relatively easy on Unix platforms like Linux, macOS, and iOS, with poll-
based APIs. He estimates it requires a few hundred lines of code. On Android,
Windows, and the web, however, the event model is entirely different, and
asyncio integration has been an open bug for years. Keith-Magee said he does
not know asyncio internals well enough to propose a solution but welcomes any
suggestions.  
  

Only CPython Can Use C Standard Library Modules
===============================================

Keith-Magee has been experimenting with alternatives to CPython for mobile and
web. Replacing the core language implementation is “relatively achievable,” he
said, “but the standard library’s another thing.” The C modules in the
standard library are only compatible with CPython. Some, like the decimal
module, have recently been ported from Python to C, which accelerates them but
presents more hindrances for non-CPython interpreters.  
  
Keith-Magee asked the core developers to maintain pure-Python implementations
of all standard library modules, for the sake of alternative interpreters. But
recognizing how burdensome that would be, he requested as a fallback that the
C interface for each extension module be clearly defined.  
  

Setup.py Cannot Build App Store Bundles
=======================================

An application packaged for a mobile app store requires various metadata, such
as a bundle identifier, that is not currently expressible in setup.py. Keith-
Magee described his confusion about how to proceed, given his confusion about
the direction of Python packaging in general. Should the metadata be in the
pyproject.toml file specified by PEP 518? Should he adapt pip or use a custom
build tool? He felt that if the core team has any clear vision for the future
of Python packaging, “I can tell you from down in the trenches that message
isn't getting through.” He requested more information and more opinions about
packaging from the core team.  
  

Wish List
=========

The talk concluded with a wish list for adapting Python to mobile and web:  
  
1\. Host/target separation testing in CI  
  
2\. Host/target separation in distutils/pip  
  
3\. Feature gating (especially in the test suite)  
  
4\. Unvendoring libffi for macOS  
  
5\. Tree (and/or root) shaking  
  
6\. AsyncIO support for other eventing styles  
  
7\. Reference implementation of modules (or a clear native interface)  
  
8\. Clearer communications on packaging  
  
Keith-Magee claims that Python faces an “existential risk” if mobile and web
support does not improve. His son, who uses only an iPad for school, asked
him, “When can I learn to program like you?” Unless students like him can
program Python on their devices, Python risks being left behind by the next
generation of programmers.

