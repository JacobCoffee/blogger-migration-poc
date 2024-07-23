.. post:: 2019-05-27
   :tags: post, legacy-blogger
   :author: Python Software Foundation
   :category: Legacy
   :location: World
   :language: en

Mariatta Wijaya: Let's Use GitHub Issues Already!
=================================================

*This was originally posted on blogger* `here <https://pyfound.blogspot.com/2019/05/mariatta-wijaya-lets-use-github-issues.html>`_.

`![ <https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgM_Ba_zMXGwdhCVD51P6udYLmPMAK77lDT3G8SEVrBv7KNGm1fjTVe_MoOI1f7O6AmjF0_i5LjSy1c7NPzXUYH0xl2rbnGXTVnMddKu8XQvmdXeLcvDik9bQkJIs-
uRGz2pA/s640/wijaya-2.jpg>`_](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgM_Ba_zMXGwdhCVD51P6udYLmPMAK77lDT3G8SEVrBv7KNGm1fjTVe_MoOI1f7O6AmjF0_i5LjSy1c7NPzXUYH0xl2rbnGXTVnMddKu8XQvmdXeLcvDik9bQkJIs-
uRGz2pA/s1600/wijaya-2.jpg)

  
Core developer Mariatta Wijaya addressed her colleagues, urging them to switch
to GitHub issues without delay. Before she began, Łukasz Langa commented that
the previous two sessions had failed to start any controversies. “Come on, we
can do better!”  
  
Wijaya replied, “Hold my tequila.”  
  
*`Read more 2019 Python Language Summit
coverage <http://pyfound.blogspot.com/2019/05/the-2019-python-language-
summit.html>`_.*  
  

Python’s Issue Tracker Is Stagnating
====================================

  
The current Python bug tracker is hosted at
`bugs.python.org <https://bugs.python.org/>`_ (“BPO”) and uses a bug tracker
called Roundup. Roundup’s development is stagnant, and it lacks many features
that the Python project could use. In theory, the Python community could
improve Roundup, but there are barriers: Roundup is versioned in Mercurial and
it has no continuous integration testing. “If the community cared about
improving bugs.python.org,” Wijaya asked, “why we haven't been doing it all
this time? Seems like you're interested in doing something else.”  
  
Compared to Roundup, GitHub issues have a number of superior features. Project
administrators can easily edit issues there or report abuse. GitHub issues
permit replying by email, and GitHub supports two-factor authentication. The
GitHub APIs allow the core team to write bots that take over many Python
development chores. Already, bots backport patches and enforce the Contributor
License Agreement (“CLA”); bots could become even more powerful once issues
are moved to GitHub.  
  

GitHub Issues: A Yearlong Debate
================================

  

`![ <https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjHRfs4TVT21tRv_P2tQWPT5C2qbxAA2-d6Wzh3uyVqSf01_zyl_NmaJVSf17-G3upgkfw3tijf9PKQEbblsWtA-b3byXDUQ3P5Ty50cYeuU2CEMMnRtNn2ZspwPfbQDCTPCg/s320/wijaya-1.jpg>`_](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjHRfs4TVT21tRv_P2tQWPT5C2qbxAA2-d6Wzh3uyVqSf01_zyl_NmaJVSf17-G3upgkfw3tijf9PKQEbblsWtA-b3byXDUQ3P5Ty50cYeuU2CEMMnRtNn2ZspwPfbQDCTPCg/s1600/wijaya-1.jpg)

Shortly after last year’s summit, Wijaya proposed in `PEP
581 <https://www.python.org/dev/peps/pep-0581/>`_ that Python migrate to GitHub
issues. She acknowledged that it was wrenching to give up on BPO and Roundup
after so many years. However, in her opinion, it is time to move to a
different issue tracker, and GitHub is the natural choice. The core developers
are all familiar with it, as well as most potential contributors.  
  
The plan for moving to GitHub issues is split into two PEPs: The rationale is
explained in PEP 581, and the migration plan is in `PEP
588 <https://www.python.org/dev/peps/pep-0588/>`_. The first steps are to back
up all GitHub data already associated with the repository, and to set up a CLA
assistant for issues—research for both tasks is in progress. Additionally, the
Python organization on GitHub needs a bug triage team for people with
permission to label or close tickets.  
  
Of course, the main job is to copy thousands of issues from Roundup to GitHub
with maximum fidelity, which requires knowledge of the Roundup codebase.
Wijaya asked for help from someone who could write the migration code or teach
her how to do it. Either way, it is likely to be the core team’s final
encounter with Roundup’s code.  
  
“Now,” said Wijaya, “Let's just use Github already! Why aren't we doing this
yet?” She asked the audience what anxieties GitHub issues provoked, or what
questions were still unanswered in her PEP. The sooner the migration is
complete, she believes, the better for the core developers and the entire
Python community.  
  

Discussion
==========

  
Ned Deily suggested revising the `Python Development
Guide <https://devguide.python.org/>`_ early to describe the GitHub issues
workflow before migration begins. This would prevent a period of confusion
among core developers after the migration. Besides, the process of updating
the Guide might flush out more details that the PEPs need to specify.  
  
Thomas Wouters made a proposal, which he feared was controversial: Don’t
migrate the old bugs. Wijaya and audience members responded with several
versions of this idea. BPO could be made read-only, with the addition of a
“Migrate to GitHub” button on bugs that anyone could press if they cared about
an old bug. Or BPO could stay read-write for a while; active bugs would be
automatically migrated until a sunset date. Some issues have useful patches or
comments which should not be lost, so either BPO must be kept online with
links from GitHub issues to their BPO ancestors, or else each BPO issue’s
entire history must be copied to GitHub.  
  
Guido van Rossum concluded that there were many decisions yet to be made
before the migration could begin. “I'm not trying to say let's spend another
year thinking about this,” he said. “I want this as badly as you want it.”
However, the team must consider the consequences more carefully before they
act.  
  
Steve Dower spoke up to say that he would prefer to stay on BPO. The current
tracker’s “experts index” is particularly useful: it automatically notifies
the Windows team, for example, when a relevant bug is filed, and there is no
equivalent GitHub feature. He rebelled at being told in effect, “Here is the
change, why haven't we done it already?” He felt the default decision on any
PEP ought to be maintaining the status quo.  
  
Barry Warsaw said, “Let's remember we have friends at GitHub that will help us
with the process.” If the core team finds missing features in GitHub issues,
perhaps GitHub will implement them.  
  
Carol Willing argued, “There comes a point in time when have to put a stake in
the ground. Nobody's saying Github is perfect, but you need to ask, are we
holding back other contributions by staying on BPO?” Many scientific Python
projects such as NumPy already track their issues on GitHub. If Python
migrates to GitHub issues it could interact better with them, as well as with
future projects that take Python in new directions. “By staying locked in
bugs.python.org, we're doing ourselves a disservice.”  
  

Postscript
==========

  
Two weeks after the Summit, `PEP 581 was officially
approved <https://mail.python.org/pipermail/python-dev/2019-May/157399.html>`_,
making the migration to GitHub inevitable.

