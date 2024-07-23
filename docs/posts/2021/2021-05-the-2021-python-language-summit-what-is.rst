.. post:: 2021-05-29
   :tags: post, legacy-blogger
   :author: Python Software Foundation
   :category: Legacy
   :location: World
   :language: en

The 2021 Python Language Summit: What Is the stdlib?
====================================================

*This was originally posted on blogger* `here <https://pyfound.blogspot.com/2021/05/the-2021-python-language-summit-what-is.html>`_.

`Brett Cannon <https://twitter.com/brettsky>`_ gave a presentation at the `2021
Python Language Summit <https://pyfound.blogspot.com/2021/05/the-2021-python-
language-summit.html>`_ about the standard library in order to start a
conversation about whether it's time to write a PEP that more clearly defines
it.  

`![Brett
Cannon <https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg52_zbX4rA_ugKyIZA1AAeTunaOhfpLg6kkKwY5ZeVDp49v9JhZXM22ekTrahLRAutnHT0cszZyVN40ZKeVj1xW42-9c67OJKg9fxtju91thi05YgQNa8xdHYuyvMRInB_iB0/s16000/brett-
cannon.png>`_](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg52_zbX4rA_ugKyIZA1AAeTunaOhfpLg6kkKwY5ZeVDp49v9JhZXM22ekTrahLRAutnHT0cszZyVN40ZKeVj1xW42-9c67OJKg9fxtju91thi05YgQNa8xdHYuyvMRInB_iB0/s500/brett-
cannon.png)



What Is the stdlib?  
---------------------

He succinctly described the stdlib as "a collection of modules that ship with
CPython (usually)." This was the most accurate definition he could give,
considering how big it is, how varied its contents are, and how long it has
been around.

He didn't offer an answer to the question about whether or not there should be
a new informational PEP to define clear goals for the stblib, but he wanted
core developers to engage with the question. There are a variety of opinions
on the stdlib, but it could be beneficial to come to some kind of agreement
about:

  * What it should be
  * How to manage it
  * What it should focus on
  * How to decide what will or will not be added to it  

He shared that he semi-regularly sees requests for adding a TOML parser to the
stdlib. When he considers requests, he asks himself:

  * Should a module be added?
  * How should such a decision be made?
  * What API should it have?
  * Is there a limit to how big the stdlib should get?

So far, there haven't been basic guidelines for answering these kind of
questions. As a result, decisions have been made on a case-by-case basis.

How Big Is the stdlib?
----------------------

He did some data digging in March of 2021 and shared `his
findings <https://github.com/brettcannon/stdlib-stats/>`_. Here are the broad
strokes:

  * python -v -S -c pass imports 14 modules.  

  * The are 208 top-level modules in the standard library.
  * The ratio of modules to people registered to vote in the last Steering Council election is 2.3, but not all of those people are equally available to help maintain the stdlib.  

What Should the stdlib Cover?
-----------------------------

Some people have suggested that the stdlib should be focused on helping users
bootstrap pip and no more. Others have said that it should focus on system
administration or other areas. Considering that there are thirty-one thematic
groupings in the `index <https://docs.python.org/3/library/index.html>`_, the
people who maintain the stdlib don't seem to have come to a collective
decision either. The groupings cover everything from networking to GUI
libraries to REPLs and more.

The stdlib has been around for a long time, and we need to be careful about
breaking people's code, so the goal is not to deprecate what is already there
but to consider guidelines for making additions.  

How Do We Decide What Goes Into the stdlib?
-------------------------------------------

He compared PEP 603 and graphlib to show how this question has been answered
in different ways in the past. The goal of PEP 603 was to add the class
frozenmap to the collections module. However, the graphlib module was only
ever discussed in an issue and never got a PEP before it was added to the
stdlib. There is no standardized approach for making these kinds of decisions,
so he would like to know what approaches core developers think would be most
appropriate.

What Is the Maintenance Cost?
-----------------------------

The PR queue is already long, which can be overwhelming for maintainers and
discouraging for contributors.

The following modules aren't used in any of the top 4000 projects:

  * mailcap
  * binhex
  * chunk
  * nis

Seventy-six modules are used in less than 1% of the 4000 most downloaded
projects on PyPI. That's over 36% of all the modules in the stdlib. This
raises some questions:

  * Do we want to continue to ship these modules?
  * What does this tell us about what the community finds useful in the stdlib?
  * How can that inform future guidelines about what to include in the stdlib?

Based on the data from March 2021, there were:

  * 37 modules with no open PRs
  * 1,451 PRs involving the stdlib, which made up the bulk of all the PRs

The module with the highest number of PRs was asyncio, which had only 50.
That's only 3% of all of the open PRs at the time.



The standard library has a significant maintenance cost, but core developers
can formulate a plan to get the most out of the maintenance that goes into the
stdlib by deciding what it should focus on. They can discuss these issues and
work towards resolving them this year.

