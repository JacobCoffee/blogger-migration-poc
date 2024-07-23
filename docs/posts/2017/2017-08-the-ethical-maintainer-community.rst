.. post:: 2017-08-10
   :tags: post, CSA, community service awards, legacy-blogger
   :author: Python Software Foundation
   :category: Legacy
   :location: World
   :language: en

The Ethical Maintainer: Community Service Award Recipient Glyph Lefkowitz
=========================================================================

*This was originally posted on blogger* `here <https://pyfound.blogspot.com/2017/08/the-ethical-maintainer-community.html>`_.

`![ <https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgVDcOfQLGOEeVrMqeP3vOzUg4ApF0L_qBGU_ueqvrdvg8-QUM92ZOljY3dlWyHXI3O1fqV3oU_gXwmXQdHL2F_1JNApChF7MiWJ8dCgj4obOpoHHXdUzywYsjXf8LKW77jCA/s320/glyph.jpg>`_](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgVDcOfQLGOEeVrMqeP3vOzUg4ApF0L_qBGU_ueqvrdvg8-QUM92ZOljY3dlWyHXI3O1fqV3oU_gXwmXQdHL2F_1JNApChF7MiWJ8dCgj4obOpoHHXdUzywYsjXf8LKW77jCA/s1600/glyph.jpg)

  
Glyph Lefkowitz was barely 20 years old when he promised himself, "I am never
going to use a proprietary programming language again!" He had been writing a
Java application for his first professional programming job, which he had
started directly after high school. The firm was a mom and pop shop that sold
inventory software. Glyph was hired to rewrite their application for a
contemporary platform: Java's `Abstract Window
Toolkit <https://en.wikipedia.org/wiki/Abstract_Window_Toolkit>`_. With the
hubris of the young, he promised, "Sure, I can rewrite your whole application
in a new language." He could do it working only four days a week, too, and
make time to work on his multiplayer online game.  
  
"I had a pretty terrible experience with Java," he says. In those early days
of the Java AWT, on classic Mac OS it leaked a tiny bit of memory every time
it opened and closed a window, and in his application, nearly every task a
user desired required opening and closing a window. On the constrained Macs of
the time, the application would crash after about 100 tasks, often taking the
whole OS down with it. The AWT was proprietary, so there was no way to fix the
bug himself. "I was fired," says Glyph, "because I was having a nervous
breakdown over this."  
  

The Birth of Twisted
--------------------

Meanwhile, Glyph was also building his multi-user text adventure in Java. He
wanted to rapidly experiment with varied gameplay logic, and to avoid
constantly restarting the server as he tried new code, he built a system in
Java that could load new modules at runtime. When, burned by his Java defeat,
he switched to Python, he found that practically all of the Java code required
to load modules and execute them simply disappeared.  
  
The switch from Java to Python had another effect, which profoundly determined
the direction of Glyph's career. He discovered async.  
  
Glyph's friend James Knight, who would become an original contributor to
Twisted, helped with the Python port. The initial code for the Python server
ran a thread per player, but Knight used a
`select <https://docs.python.org/2/library/select.html#select.select>`_ call to
determine, within each thread, whether it was time to read a message from the
player or send one. When young Glyph saw that code he was astonished. "It's
doing two things at once! But it's also kind of one thing." After all `the
bugs he'd battled in his multithreaded
Java <https://glyph.twistedmatrix.com/2014/02/unyielding.html>`_, he thought,
"Couldn't we just do one thing all the time?" He and Knight rewrote the entire
game server as a single-threaded event loop. He liked how it simplified the
code. Only one thread accessed a shared data structure at a time. His original
motivation to use an event loop was not efficiency: rather, it was how much
easier it was to make his code correct.  
  
Glyph says that his strength, in his 20s, was knowing what he didn't know. His
father is a programmer, and he taught Glyph that most programming techniques
are already well-known. Therefore when Glyph and James Knight got their event
loop working, Glyph thought, "Someone must have done this before." He searched
on Alta Vista and found `the ACE
project <http://www.cs.wustl.edu/~schmidt/ACE.html>`_, which included a C++
event loop. Glyph refined his Python event loop based on the best practices he
found in ACE, and this became the basis for Twisted, which is now one of the
oldest and most influential of all Python libraries.  
  
Based on this early experience discovering that event loops were a well-known
technique, Twisted's motto is "no new ideas allowed." Twenty years later,
however, Glyph has begun to innovate on the margins. For example, `his Tubes
library <https://tubes.readthedocs.io/en/latest/tube.html#what-are-tubes>`_
implements asynchronous I/O as "flows" of data with flow control and
backpressure. But when it comes to event loops, he says, "There's so much
prior art that coming up with new inventions is not worthwhile."  
  

Twisted's Influence On Python
-----------------------------

In the second quarter of 2017, the Python Software Foundation recognized Glyph
Lefkowitz with a Community Service Award for his work on Twisted and his
contributions to the Python community. Nick Coghlan nominated him, saying that
Twisted "predates almost all other Python event handling systems by years, and
still has by far the most comprehensive set of network protocol handlers." The
decade-long journey from `PEP 342's generators-as-
coroutines <https://www.python.org/dev/peps/pep-0342/>`_, which enabled
`Twisted's inlineCallbacks
feature <http://twistedmatrix.com/documents/current/core/howto/defer-
intro.html#inline-callbacks-using-yield>`_ and Tornado's Futures, to native
coroutine support with "async" and "await", began with Twisted. Coghlan says
that evolution could be reasonably described as taking the concepts first
embodied in Twisted and drawing them ever closer to the center of the
language.  
  
In 2012, Guido van Rossum began writing asyncio, an async framework for the
Python standard library. He collaborated closely with Glyph, as well as
Tornado's maintainer Ben Darnell, to incorporate their best ideas in asyncio.
He was interested in Twisted's notion of a Deferred, but he couldn't seem to
understand it. Glyph says that trying to explain Deferred to Guido "was the
worst time I've ever had on a mailing list." `Guido
wrote <https://www.google.com/url?q=https://groups.google.com/d/msg/python-
tulip/EgpBV5-sIQ4/xf89to1eExcJ&sa=D&ust=1502293861319000&usg=AFQjCNHYXF9nS2rJd9ZZ7t7_s2bnxhFYfg>`_,
"I really don't get Deferreds. Don't bother pointing me to docs or tutorials;
I tried and failed." He said that Glyph's "snarky tone is seriously affecting
my ability to process your response." Then he went silent for a week.  
  
Glyph was devastated. He felt like he'd been flamed and ghosted by the founder
of the language itself. `Then Guido suddenly returned to the mailing
list <https://groups.google.com/forum/#!searchin/python-
tulip/guido$20deferred%7Csort:relevance/python-
tulip/ut4vTG-08k8/txVI_TXL634J>`_, with what Glyph calls "the most trenchant and
keenly observed critique of the Deferred module. It was possibly the best code
review I've ever received." It was suddenly clear that Twisted's Deferred
would interoperate just fine with the new asyncio event loop. "We were all on
board."  
  

Responsibilities of Open Source Programmers
-------------------------------------------

Glyph is distinct among Python programmers for his outspoken views on ethics.
In `his 2015 PyCon talk <http://pyvideo.org/pycon-us-2015/the-ethical-
consequences-of-our-collective-activi.html>`_ he proposed that programmers write
a code of ethics, similar to other professions such as medicine and
journalism. If we don't, he says, "someone else is going to do it for us, and
they are not going to understand our field well enough to do it correctly."
Since `software is eating the world <https://a16z.com/2016/08/20/why-software-
is-eating-the-world/>`_ and it influences nearly all economic activity, we have
`a grave obligation to write code
ethically <https://glyph.twistedmatrix.com/2005/11/ethics-for-programmers-
primum-non.html>`_.  
  
Open source programmers often think we owe our users nothing, because we give
away code for free. But this attitude ignores the benefits that we've gained.
"Being an open source maintainer has opened all sorts of doors for me," says
Glyph. "Whenever anyone does anything with Twisted the credit accrues to me.
That's not really accurate, because `there are lots of other
maintainers <https://github.com/twisted/twisted/graphs/contributors>`_ like
Amber Brown, David Reid, Ashwini Oruganti, Jean-Paul Calderone, Moshe Zadka,
and Christopher Armstrong." Regardless, anyone who releases open source code
engages in a subtle exchange with users, which obliges the coder to uphold
some responsibilities. In my conversation with him, Glyph identified three
responsibilities for open source programmers: to make clear promises, to
secure our code, and to release code of appropriate quality.  
  
Open source maintainers are uniquely obliged to make clear promises. If a
maintainer abandons a project, her main obligation is to announce her
departure and to transfer control. "Being an open-source maintainer is not a
life sentence," says Glyph. But it is irresponsible to make a worthy piece of
software, gain users, then disappear without a word.  
  
We also have a responsibility to protect our personal information security;
for example, a Python project maintainer must protect her PyPI account so her
users know they won't be hacked when they install her package. That
responsibility is shared with the community's infrastructure maintainers, and
Glyph cites PyPI as one of the best modern examples. "It doesn't get enough
credit because of Python's checkered history with packaging," he says, "but
the way Donald Stufft thinks about practical information security, and the
other folks who work on PyPI as well, and the resources the PSF has invested
there," have laid a foundation for securely distributing open source Python.  
  
And finally, many of us set a low bar for the quality of code that we release:
if the project scratched our own itch, we might as well open-source it. In
Glyph's opinion, we must more carefully consider the impact of the code we
give away, because we can't predict how it will be used. Glyph knows that many
of the largest sites run Twisted somewhere in their stack, and he feels the
responsibility keenly.  
  
"A lot of our software completely escapes its originating context," says
Glyph. The author might intend to release a mere prototype, but downstream
packagers come to depend on her code, and other programmers even farther
downstream might not know they depend on it at all. Of course, software users
share some responsibility for auditing what code they use. "This
responsibility is not black or white," says Glyph. "There's small tradeoffs
and fractional proportions. It's not 100% yours or not, but you've got to
think about it."

