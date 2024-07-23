.. post:: 2015-06-05
   :tags: Board of Directors, election, post, community, democracy, legacy-blogger
   :author: Python Software Foundation
   :category: Legacy
   :location: World
   :language: en

The Election Process and the new PSF Election Administrator
===========================================================

*This was originally posted on blogger* `here <https://pyfound.blogspot.com/2015/06/the-election-process-and-new-psf.html>`_.

Background:
~~~~~~~~~~~

As those of you who have been following recent events in the PSF know, there
were some difficulties and disagreements surrounding the election for the
2015-2016 Board of Directors. The initial attempt at an election for Board
members was cancelled due ambiguity concerning candidate nomination deadlines.

Then, as possible solutions were discussed on the PSF voting members list, it
became apparent that there were additional aspects of the previously used
system (E-vote) that were considered less than ideal by some members.

The Election Administrator at that time, due to newly undertaken professional
commitments, was unavailable to relaunch the election or to modify the
procedures to satisfy the desiderata expressed by many. Fortunately, Ian
Cordasco agreed to step into the position, and he has been hard at work since
the beginning of May getting the recently completed election back on track and
exploring long term solutions to newly identified problems.

Already some important changes have been made: First of all, with the hard
work of the Board of Directors and many volunteers, a precise and unambiguous
deadline was set for nominations, for the issuing and for the receipt of
ballots for both the Board election and the Sponsor election (See `New Board
Election <http://pyfound.blogspot.com/2015/05/new-board-election-important-
please-read.html>`_.) That election has been successfully conducted and we have
a new Board of Directors (and some new sponsors) as a result. (See
`Congratulations <http://pyfound.blogspot.com/2015/06/congratualations-to-new-
board-of.html>`_.)

Secondly, an Elections Working Group was formed to study the desirability of
an enhancement to the E-vote software developed by Massimo DiPierro and David
Mertz that had been used by the PSF for the past several years. An alternative
solution, switching to another system like Helios, is also being explored. For
those who wish to participate in this discussion and/or to contribute to this
important evaluative study, please subscribe to  `Elections-
wg@python.org <https://mail.python.org/mailman/listinfo/elections-wg>`_.

I recently had an email chat with Ian about his new role which I’d like to
share with you:

_Q: Why did you get involved?_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Ian: _There was a lot of conflict over the last Board Election. Unnecessary
conflict is something I really don’t want to see in the Python community, so I
stepped up to attempt to deescalate the situation._

_Q: What is your background/interest as election administration?_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Ian: _I have no background in running elections. The software is intriguing to
me. The way of verifying votes and ensuring anonymity is also intriguing._

_Q: What are some of your goals as election administrator?_
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ian: _To run elections well and improve the software we use to run our
elections._

_Q: What are the criteria for a good election process?_
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ian: _This list is probably incomplete, but,_

  * _User friendly: The nomination process should be easy as should voting._

  * _Transparent and Verifiable: Nominations and votes should be verifiable by any one observing the election._

  * _Secure: It’s unlikely someone might try to attack a PSF election, but users should know that their votes aren’t being altered when casting them and that the ballot they received was correct._

  * _Well documented: Voters and candidates should know the schedule. The software should be well documented for all involved - candidates, voters, and election administrators alike._

  * _Cooperative: I have the great pleasure of coordinating with Ewa Jodlowska who helps in the election process. Massimo DiPierro and David Mertz have been very helpful in learning and navigating E-Vote.This whole process would have been a lot more stressful if not for their help and support._

_Q: I understand that recent election yielded a tie in the number of
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
votes for the eleventh Director’s seat. How was that resolved?_

Ian: _I spoke with David and in the past, ties have been broken with code such
as:_

    
    
    if random.random() < 0.5:
        print('Candidate A')
    else:
        print('Candidate B')

_So in following with that, I ran that code and came up with the 11th… For
some amount of verifiability, I recorded the run of that
`script <https://asciinema.org/a/cm2gck0j1w9k9fqdaq5ezsags>`_._

_Q: How can we (PSF members) help?_
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ian: J _oin the Elections WG! We’re trying to improve the whole of the PSF
elections process. There are a few known issues with the current process. Many
hands make light work._

_I would love to hear from readers. Please send feedback, comments, or blog
ideas to me at  `msushi@gnosis.cx <mailto:msushi@gnosis.cx>`_._

