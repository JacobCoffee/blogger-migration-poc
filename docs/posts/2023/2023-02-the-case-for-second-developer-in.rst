.. post:: 2023-02-15
   :tags: post, legacy-blogger
   :author: Python Software Foundation
   :category: Legacy
   :location: World
   :language: en

The Case for a Second Developer-in-Residence for Python
=======================================================

*This was originally posted on blogger* `here <https://pyfound.blogspot.com/2023/02/the-case-for-second-developer-in.html>`_.

As the currently serving sole developer in residence, I’m often asked if there
will be more people holding the same position in the future. I strongly
believe there should be and that it’s crucial to the long term success of this
role. The only open matter is finding sustainable sponsorship for the
position.  

The current developer in residence
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

My day-to-day work revolves around an array of maintenance tasks for the
Python Software Foundation with focus on CPython. Since I started in July
2021, I’ve done among others:  

  * PR review and merging: 627 merges to CPython that lead to closing of 276 issues on the bug tracker, and many more code reviews on Github;
  * release management for the 3.8 and 3.9 branches as well as release notes and announcements for other releases;
  * following the Python security response team reports that lead to several security releases of Python;
  * following the buildbot fleet status and reacting to failures, including maintenance of the only buildbot that runs big memory tests;
  * project management of the transition from our previous custom issue tracker to Github Issues;
  * migration from a previous custom CLA management bot to EdgeDB CLA bot;
  * co-administering `discuss.python.org <http://discuss.python.org>`_ including responding to moderation requests;
  * co-administering core Python Discord;
  * co-chairing the Python Language Summit at PyCon US;
  * reviewing talk submissions on the Program Committee for PyCon US;
  * facilitating cooperation with other significant Python projects: HPy, PyPy, nogil;
  * public speaking (5 events in 2021, 4 events in 2022).

The missing big picture
~~~~~~~~~~~~~~~~~~~~~~~

While I find this work fulfilling and there’s always more things for me to do
that other contributors suggest, one facet of the work can overshadow another.
I cannot be in all places at once. Most importantly, while removing obstacles
for other core developers (often volunteers) is indeed where we should put
paid effort, I sometimes get asked: what’s your big project?  
  
At this point I cannot say I had any large personal contribution over the past
18 months of work on CPython, which is ironic, given that I spent more time on
it than in the preceding 11 years of core development combined. I had a few
attempts at larger changes but inevitably the small busywork eats up my
attention.  

Adding another developer in residence more than doubles the position’s
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
positive impact

It’s worth noting that the codebase of CPython is over a million lines of code
now and even working on it full time does not mean a single person groks it
all. That means that what you’re getting from Łukasz, the Developer in
Residence, is something else than what you’d get from Magdalena, the Developer
in Residence.  
  
That alone means it would be worth having another person with a complementing
skill set. But I believe there’s more.  
  
Compared to working solo, having a team of two people paid full time to
improve the developer experience for the rest of the core contributors, would
allow us to take on larger sweeping projects. What we would end up doing would
be definitely consulted with the Steering Council and we would take
suggestions from the role’s sponsor. But there’s many possibilities!  
  
We could add official build support for a new platform like iOS. We could
improve test coverage of CPython tests, including coverage of trickier bits
like the platform-specific code paths, C code, or code involved in CPython’s
interpreter startup. We could revamp the buildbot master server to be more
performant. We could be taking on implementation of accepted PEPs. We could
upgrade `speed.python.org <http://speed.python.org>`_ to be more informative and
easy to use. We could move the rest of the custom CPython bots to Github
Actions, decreasing needed maintenance, improving performance and reliability.
Those are just some ideas.  
  
There is one more reason why I’m rooting for another person to join this
position. Having another developer in residence would buffer any turbulence
the other person has. Whenever I’m sick, or travel, or I’m stuck with a
particularly stubborn problem, there would reliably be somebody else the other
core developers could count on. This is important not only for them but also
for me personally as it would decrease anxiety that builds up any time I’m
unable to help somebody who needs me.  
  
The ability to split work between two people is something I think about often.
In theory there’s a whole team of core developers out there but since they’re
mostly volunteers, I’m in no position to tell them what to do. Having a peer
paid by the PSF would be different. It would be fair game to share the burden
of a gnarly boring task, and that sounds like a wonderful improvement to me.  

What if there isn’t another developer in residence?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

I’m not saying the other person is required for me to stay productive. If we
don’t find the budget for it, the situation is still better than having no
developer in residence at all, I’d like to believe. So far I haven’t received
much feedback on my work but I’m always open to hearing suggestions.

