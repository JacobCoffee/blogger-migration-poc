.. post:: 2015-10-23
   :tags: PSF funding, post, ecosystem, porting, python3, legacy-blogger
   :author: Python Software Foundation
   :category: Legacy
   :location: World
   :language: en

Twisted Trial Ported to Python 3!
=================================

*This was originally posted on blogger* `here <https://pyfound.blogspot.com/2015/10/twisted-trial-ported-to-python-3.html>`_.

*Twisted* , as many of you know, is an asynchronous, or "event driven"
networking framework written in Python
(<https://twistedmatrix.com/trac/wiki>). *Twisted* has been around for about
a decade, offers many features, including low-level primitives and high-level
interfaces, and works with many protocols (including HTTP, XMPP, NNTP, IMAP,
SSH, IRC, FTP).

  
`![ <https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi0Z0Sa1Y-oAsPlgcexMK8tmpoGvnrvHcbTPWrSD4J3Qfl0JS0nMPC0uWGS9iooH9UmHlgJ9HDHsPSEyvqSXqJJfENYl39pQ1h6kYEh9eqg4iip2605cCjTq0dOzgQ4_G-
Lebc/s200/Twisted-
Logo.tiff>`_](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi0Z0Sa1Y-oAsPlgcexMK8tmpoGvnrvHcbTPWrSD4J3Qfl0JS0nMPC0uWGS9iooH9UmHlgJ9HDHsPSEyvqSXqJJfENYl39pQ1h6kYEh9eqg4iip2605cCjTq0dOzgQ4_G-
Lebc/s1600/Twisted-Logo.tiff)  
---  
Twisted Logo  
  
Due to its maturity and complexity, *Twisted*  requires a lot of time and
effort to be completely ported to Python 3. Fortunately, the PSF was able to
help fund some of this work; one recent result is the release of *Twisted
15.4,*  which includes *Twisted’* s standard test-runner,
*Trial*(codenamed "Trial by Fire").

The PSF Grant allowed core developer and *Twisted* release manager,  
Amber (HawkOwl) Brown, to port *Trial* to Python 3. She recently sent the
PSF this announcement:

> “Just wanting to let you all know that a *Twisted* with the PSF-funded
> *Trial Py3* port is now released. And a little example of it in action:  
>  <https://asciinema.org/a/cthr9xezlt8mxg5dp0n73fzc9>. Again, many thanks for
> accepting the grant proposal – the ability to dedicate a significant chunk
> of time to this work has meant it was completed well sooner than if the
> grant had not been accepted.”

Due to certain differences between Python 3 and Python 2 (e.g., removal of
ClassType and unbound methods), Amber tells us that the porting of *Trial*
required a rewriting and retesting of the test suite loader. The work is
mostly done and the current port duplicates most of *Trial* ’s previous
functionality with the exception of its distributed test runner
(`DistTrialRunner`).

Specifically, the PSF grant allowed Amber to perform the following steps:

> "\- Complete and test the *Trial* unittest loader"

> "\- Fix the remaining failing *Trial* tests "

> "\- Create a tool which runs only the portions of *Twisted* that have been
> ported to Python 3 for use in *Twisted* development "

> "\- Break up the port into smaller pieces, put them up for review, and
> address the review comments "

> "\- Merge the reviewed portions"

*Trial* ’s features–a front-end, the ability to handle Deferreds and
asynchronous tests, and the capacity to build testcase-duration reactors, make
testing much easier. The *Twisted* team will now be able to use *Trial*
for continued Python 3 porting, while users of *Twisted* will be able to
test their codebases more easily as they port them to Python 3. Because of
*Trial* , we can look forward to *Twisted 15.5* in the near future (and
hope to see more users' code ported to Python 3, as well). As Amber tells us,

> "15.5, coming soon, will come with another handful of ported modules, and
> the `twistd` application (a daemoniser + plugin runner, the recommended way
> of spawning long-running Twisted services)."

The PSF sends its gratitude and congratulations to Amber Brown and the
*Twisted* team on this important accomplishment.  
  

To learn more about *Twisted* , the following websites, video talks, and
tutorials are available:

<http://labs.twistedmatrix.com/>

<http://krondo.com/wp-content/uploads/2009/08/twisted-intro.html>

<http://www.ibm.com/developerworks/library/l-twist1/>

<http://pyvideo.org/video/2597/twisted-mixing>

<https://www.youtube.com/watch?v=_HZR7_ZBkYY>  
  

_I would love to hear from readers. Please send feedback, comments, or blog
ideas to me at  `msushi@gnosis.cx <mailto:msushi@gnosis.cx>`_._

