.. post:: 2022-05-11
   :tags: pycon, post, legacy-blogger
   :author: Python Software Foundation
   :category: Legacy
   :location: World
   :language: en

The 2022 Python Language Summit: Python in the browser
======================================================

*This was originally posted on blogger* `here <https://pyfound.blogspot.com/2022/05/the-2022-python-language-summit-python.html>`_.

Python can be run on many platforms: Linux, Windows, Apple Macs,
microcomputers, and even Android devices. But it’s a widely known fact that,
if you want code to run in a browser, Python is simply no good – you’ll just
have to turn to JavaScript.

Now, however, that may be about to change. Over the course of the last two
years, and following over 60 CPython pull requests (many attached to GitHub
issue `#84461 <https://github.com/python/cpython/issues/84461>`_), Core
Developer Christian Heimes and contributor Ethan Smith have achieved a state
where the CPython `main` branch can now be compiled to
`WebAssembly <https://webassembly.org>`_. This opens up the possibility of being
able to run arbitrary Python programs clientside inside your web browser of
choice.

At `the 2022 Python Language
Summit <https://pyfound.blogspot.com/2022/05/the-2022-python-language-
summit_01678898482.html>`_, Heimes gave a talk updating the attendees of the
progress he’s made so far, and where the project hopes to go next.

  

* * *

WebAssembly basics
------------------

WebAssembly (or “WASM”, for short), Heimes explained, is a low-level
`assembly <https://en.wikipedia.org/wiki/Assembly_language>`_-like language that
can be as fast as native `machine
code <https://en.wikipedia.org/wiki/Machine_code>`_. Unlike your usual machine
code, however, WebAssembly is independent from the machine it is running on.
Instead, the core principle of WebAssembly is that it can be run _anywhere_ ,
and can be run in a completely isolated environment. This leads to it being a
language that is extremely fast, extremely portable, and provides minimal
security risks – perfect for running clientside in a web browser.

  

`![ <https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjXVrvjIV5Pg-7vBlGzGgVYFJAygQ2a8qe9LXiaDwLzouLJMBbHUvl6E-XR9dLV-
RbeflF7YA4C61vlgWKUpHHwfe-TiAixTknVfw2TdrUGN6RpGo6bO9aM19Rc42si-
dQtuaCQF_QSZVfvOqSxOvjnwjUhe6P3jx-
hWFNKt9W8NXGrHTY/w400-h228/Compiling%20to%20WASM.png>`_](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjXVrvjIV5Pg-7vBlGzGgVYFJAygQ2a8qe9LXiaDwLzouLJMBbHUvl6E-XR9dLV-
RbeflF7YA4C61vlgWKUpHHwfe-TiAixTknVfw2TdrUGN6RpGo6bO9aM19Rc42si-
dQtuaCQF_QSZVfvOqSxOvjnwjUhe6P3jx-
hWFNKt9W8NXGrHTY/s1105/Compiling%20to%20WASM.png)

  

  

  

`![ <https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhe_WC6ibKEMkQQTAkyJS-0N47L2GyZblm64gZnymQCFOagjRHYRStW4041pWZgXp2tR1djK4VOAFfOTUueHVyIsBrolUdprqRwMkRiMBFawhPYNdPdEQrOmnviIs06twY4QwQAygSr5Jz5OhovG1Bm3_pyqp_QOBJDloDS-
luIQDrARwc/w400-h228/What%20is%20WASM.png>`_](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhe_WC6ibKEMkQQTAkyJS-0N47L2GyZblm64gZnymQCFOagjRHYRStW4041pWZgXp2tR1djK4VOAFfOTUueHVyIsBrolUdprqRwMkRiMBFawhPYNdPdEQrOmnviIs06twY4QwQAygSr5Jz5OhovG1Bm3_pyqp_QOBJDloDS-
luIQDrARwc/s1102/What%20is%20WASM.png)

  
  

After much work, CPython now cross-compiles to WebAssembly using
`emscripten <https://emscripten.org/>`_ through the `--with-emscripten-
target=browser` flag. The CPython test suite now also passes on emscripten
builds, and work is going towards adding a buildbot to CPython’s fleet of
automatic robot testers, to ensure this work does not regress in the future.

Users who want to try out Python in the browser can try it out at
`https://repl.ethanhs.me/ <https://repl.ethanhs.me/>`_. The work opens up
exciting possibilities of being able to run PyGame clientside and adding
Jupyter bindings.

  

`![ <https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhOQOZPEsaISXhU9KzTBRipRUEbfLFnqjscGY5k7zDIVBJEh95lEXAc0mMRVgur-
Ddy0YSPKR704GIxMvQFG_Z9dJG-qIgJ2PuDT7_B8g26p3GUYlb-M-
ATRy6SbD8O0j9qgI2C-mvGwpMCqtKZzVUI3dsbngkw-Teo-
WKfoFvBLTAcJYk/w400-h228/Small%20demo.png>`_](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhOQOZPEsaISXhU9KzTBRipRUEbfLFnqjscGY5k7zDIVBJEh95lEXAc0mMRVgur-
Ddy0YSPKR704GIxMvQFG_Z9dJG-qIgJ2PuDT7_B8g26p3GUYlb-M-
ATRy6SbD8O0j9qgI2C-mvGwpMCqtKZzVUI3dsbngkw-Teo-
WKfoFvBLTAcJYk/s1098/Small%20demo.png)

  

  

`![ <https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg8iEqr-
gFtnHybO7OJ01jeRmjvKy1kQqGt-j6-JVSvmaKvnUu4ZA07rKe5h36lBQ9Tg2eSYUWFuF4t679ZqVvkyECAcp6swAw1R6R-8IfHObWIQZ9tMfo0-z2BmyvQRmiEMJpBqI3xY4etjZhSGI5Na0d7CrErhtKpL_2dE-8X49fOGQ8/w400-h228/PyGame%20demo.png>`_](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg8iEqr-
gFtnHybO7OJ01jeRmjvKy1kQqGt-j6-JVSvmaKvnUu4ZA07rKe5h36lBQ9Tg2eSYUWFuF4t679ZqVvkyECAcp6swAw1R6R-8IfHObWIQZ9tMfo0-z2BmyvQRmiEMJpBqI3xY4etjZhSGI5Na0d7CrErhtKpL_2dE-8X49fOGQ8/s1121/PyGame%20demo.png)

  

  

* * *

Support status
--------------

It should be noted that cross-compiling to WebAssembly is still highly
experimental, and not yet officially supported by CPython. Several important
modules in the Python standard library are not currently included in the
bundled package produced when `--with-emscripten-target=browser` is specified,
leading to a number of tests needing to be skipped in order for the test suite
to pass.

  

`![ <https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg6FiL8GyoOOZjbf5Riz36cJPg_E_MwFlAd5Ey7i8pp0xmfwI6bBSfB1WqMleeGPB-
Xm2NROCUk5umsw0dAEHnWEwEZ56E39RzPtAgE7Z9VoTYMTQaCcCsEBisx0yAur_oW17UeO6PNUV_ahNZ-
HzR-1whlZ0JC_nmiaZj4i8SkVK1RJMU/w400-h226/Support%20status.png>`_](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg6FiL8GyoOOZjbf5Riz36cJPg_E_MwFlAd5Ey7i8pp0xmfwI6bBSfB1WqMleeGPB-
Xm2NROCUk5umsw0dAEHnWEwEZ56E39RzPtAgE7Z9VoTYMTQaCcCsEBisx0yAur_oW17UeO6PNUV_ahNZ-
HzR-1whlZ0JC_nmiaZj4i8SkVK1RJMU/s1102/Support%20status.png)

  

  

Nonetheless, the future’s bright. Only a few days after Heimes’s talk, Peter
Wang, CEO at Anaconda, announced the launch of
`_PyScript_ <https://anaconda.cloud/pyscript-python-in-the-browser>`_ in a
`PyCon keynote address <https://anaconda.cloud/pyscript-pycon2022-peter-wang-
keynote>`_. PyScript is a tool that allows Python to be called from within HTML,
and to call JavaScript libraries from inside Python code – potentially
enabling a website to be written entirely in Python.

PyScript is currently built on top of
`_Pyodide_ <https://pyodide.org/en/stable/>`_ , a third-party project bringing
Python to the browser, on which work began before Heimes started his work on
the CPython `main` branch. With Heimes’s modifications to Python 3.11, this
effort will only become easier.

