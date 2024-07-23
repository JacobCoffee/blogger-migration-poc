.. post:: 2019-06-03
   :tags: post, legacy-blogger
   :author: Python Software Foundation
   :category: Legacy
   :location: World
   :language: en

Pablo Galindo Salgado: The Night's Watch is Fixing the CIs in the Darkness for You
==================================================================================

*This was originally posted on blogger* `here <https://pyfound.blogspot.com/2019/06/pablo-galindo-salgado-nights-watch-is.html>`_.

`![ <https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgykyJ2Ky5ABOKlQu3Xsk8i4weEGsvq8FKTB92Xy7kNoGDndrDh8aT5RKdJ6xgGiaKzvzx3vC92NrsjP8TD9gcroY6PSostwqSmVtsHijuv-51f09t21iNrNFTnnr3SYkHlKA/s400/PyconUS_-
Language-summit-lightning-
talk-1.png>`_](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgykyJ2Ky5ABOKlQu3Xsk8i4weEGsvq8FKTB92Xy7kNoGDndrDh8aT5RKdJ6xgGiaKzvzx3vC92NrsjP8TD9gcroY6PSostwqSmVtsHijuv-51f09t21iNrNFTnnr3SYkHlKA/s1600/PyconUS_-
Language-summit-lightning-talk-1.png)

  
Python is tested on a menagerie of “buildbot” machines with different OSes and
architectures, to ensure all Python users have the same experience on all
platforms. As Pablo Galindo Salgado told the Language Summit, the bugs
revealed by multi-platform tests are “Lovecraftian horrors”: race conditions,
bugs specific to particular architectures or compiler versions, and so on. The
core team had to confront these horrors with few good weapons, until now.  
  
*`Read more 2019 Python Language Summit
coverage <https://pyfound.blogspot.com/2019/05/the-2019-python-language-
summit.html>`_.*  
  

The Solemn Duty of Bug Triage
=============================

  
When a test fails, the core developer who triages the failure follows an
arduous process. “It's not glamorous by any means,” said Galindo, “but someone
needs to do it.” Galindo, Victor Stinner, and Zachary Ware are the main bug
triagers, and they all follow a similar sequence: read the failure email,
search for duplicate failures, read the voluminous logs to characterize the
problem, and file a bug with a detailed description. Then, optionally, they
try to reproduce the problem. Since failures are often specific to one
buildbot, the triagers must contact the buildbot’s owner and get permission to
ssh into it and debug.  
  
According to Galindo, typical test failures are “really, really complicated,”
so the triage team takes a firm stance about reverting changes. If they
suspect that a change has broken a test, its author has one day to follow up
with a fix or the change will be reverted. “Nobody likes their commits to be
reverted,” he told the Language Summit. But test failures can cause cascading
failures later on, so the team must be ruthless.  
  

New Tools for Squashing Bugs
============================

  
A pull request is not tested by the buildbots until after it is merged, so the
author does not immediately know if they have broken any tests. Galindo and
his colleagues have written a bot which reacts to a test failure by commenting
on the merged pull request that caused it, with reassuring instructions to
help the panicked author respond. “We have some arcane magic,” he said, to
distinguish compiler errors from tracebacks and neatly format them into the
message, so the author get begin diagnosing immediately.  
  

`![ <https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgNK9Kix0IukNxCgnarP8KMQxghpMNpvytGKnksy3hM3kbX_k05faE-
ZSU1cRcAexXjHVsZ3NczrL-Kx8ZuVFhXCqjogArWdMjhWIWyN4bHiWYmYj6HgXs-
UiPNniLLxX4pfA/s640/buildbot-
failure.png>`_](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgNK9Kix0IukNxCgnarP8KMQxghpMNpvytGKnksy3hM3kbX_k05faE-
ZSU1cRcAexXjHVsZ3NczrL-Kx8ZuVFhXCqjogArWdMjhWIWyN4bHiWYmYj6HgXs-
UiPNniLLxX4pfA/s1600/buildbot-failure.png)

  
Since the bot was deployed in September, the mean time to fix a test failure
has fallen dramatically. When Galindo showed this chart, the core developers
broke into applause.  
  

`![ <https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjoml_QeZEni9Z_pP_WUR02MMXMjGYhoKZi6CSbxlS8PzflWXagw-x7TGojeKM1H898ZHiP6JXx1XL2tbqEwTibxfNOu8Tra3hhW37XT2_SbeNtWphBWmFz_fQ4CM1jXHCHaw/s640/bot-
activated.png>`_](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjoml_QeZEni9Z_pP_WUR02MMXMjGYhoKZi6CSbxlS8PzflWXagw-x7TGojeKM1H898ZHiP6JXx1XL2tbqEwTibxfNOu8Tra3hhW37XT2_SbeNtWphBWmFz_fQ4CM1jXHCHaw/s1600/bot-
activated.png)

  
Nevertheless, there are still severe problems with Python’s tests. Flaky tests
break about 40% of the builds; the system is programmed to retry a failure and
consider it successful if the second run passes, but this is clearly just a
stopgap. Galindo urged the core team to reduce flaky tests by eliminating race
conditions and sleeps. He also asked for help writing a tool that would
analyze which flaky tests fail most often, and a tool to detect and merge
duplicate test failures.  
  
Finally, Galindo proposed allowing contributors to test their pull requests on
the buildbots before merging. This feature should be implemented cautiously.
“The buildbots are very delicate,” he said. They cannot safely run arbitrary
code like on Travis or other commercial test infrastructures. Still, it would
be worth the effort, if contributors could catch mistakes before they are
merged.  
  

`![ <https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhTvi5eYQ-
FZJf5JZ2YQlR3p1xwfLVxwzL-
guWK0Q9jSdJ8mCOLOahs6ahyphenhyphenYkhaIE5ftyIhFpJFTNSazFoOS1PupHYQoRCWzZRGtwMHtpOK8c7NTV7kanQK8qvMkNny9rF3vw/s640/galindo.jpg>`_](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhTvi5eYQ-
FZJf5JZ2YQlR3p1xwfLVxwzL-
guWK0Q9jSdJ8mCOLOahs6ahyphenhyphenYkhaIE5ftyIhFpJFTNSazFoOS1PupHYQoRCWzZRGtwMHtpOK8c7NTV7kanQK8qvMkNny9rF3vw/s1600/galindo.jpg)

