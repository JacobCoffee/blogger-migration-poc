.. post:: 2016-08-22
   :tags: post, legacy-blogger
   :author: Python Software Foundation
   :category: Legacy
   :location: World
   :language: en

"In the beginning, there was one Python group": Community Service Award Recipient Stéphane Wirtel
=================================================================================================

*This was originally posted on blogger* `here <https://pyfound.blogspot.com/2016/08/in-beginning-there-was-one-python-group.html>`_.

“In the beginning, there was one Python group in Charleroi, the P3B (Python
Blanc Bleu Belge)”, `Stéphane Wirtel  <https://twitter.com/matrixise>`_recalls.
This first Python group was led by Denis Frère and Olivier Laurent. Together
with Aragne, the first company using Python in Belgium, and Marc-Andre Lemburg
the P3B helped organize the inaugural EuroPython in 2002. Over the years,
however, the P3B disbanded. “Other groups have organized some events for the
Belgian community”, Wirtel adds. These groups, however, have faced some of the
organizing challenges as the P3B.

*  
*  

As a Python user of 15 years, Wirtel contemplated what would be the best way
to sustainably build the Belgian Python community. He originally wanted to
organize the first PyCon in Belgium but eventually decided to invest his
energies elsewhere. Ludovic Gasc, Fabien Benetou and Wirtel began by hosting
Python events in Brussels and Charleroi.

*  
*  

The Python Software Foundation has awarded Wirtel in the `second quarter of
2016 <https://www.python.org/psf/records/board/minutes/2016-06-29/#id33>`_ with
a Community Service Award in recognition for his work organizing a Python User
Group in Belgium, for his continued work creating marketing material for the
PSF, for his continued outreach efforts with spreading the PSF's mission.

*  
*  

!`IMG_0137.JPG <https://lh3.googleusercontent.com/1Z3QZdNNFczR4Zk2hTOh1c4cwvs47SDDewvJAQ3irVk0DAQqkESiWKU6iaAdzUX4_9Ob2bLIFckivM9Q2GqcbZhK1UE6E41APuUN0_CbaQPp2_oXTH0FZwUEYzTIUc8oJoOsxvE_>`_

*  
*  

Outreach at PythonFOSDEM and Building a New Python Belgium Community

*  
*  

“FOSDEM is one of the most important events in the European development
community with over 5,000 attendees participating in a weekend event” Wirtel
explains. The importance of FOSDEM led Wirtel and Gasc to create the first
PythonFOSDEM.

*  
*  

Since 2013 Wirtel has organized the PythonFOSDEM devroom, expanding the room
from 80 participants in 2013 to well over 400 participants in 2016. Benetou,
who volunteered in the `FOSDEM 2016 Python
devroom <https://archive.fosdem.org/2016/schedule/track/python/\>`_), remembers
the excitement in the room explaining that the room was filled within five
minutes of opening.

  

> Python devroom at `@fosdem <https://twitter.com/fosdem>`_, it didn't even
> started and it's packed already!
> `pic.twitter.com/MRtzFt24ez <https://t.co/MRtzFt24ez>`_
>
> — utopiah (@utopiah) `January 30,
> 2016 <https://twitter.com/utopiah/status/693362681303187456>`_

*  
*  

With the growth of the PythonFOSDEM devroom and the return of AFPyro-BE, led
by Ludovic Gasc, Wirtel has been focusing efforts on building the
`belgium@python.org <mailto:belgium@python.org>`_ mailing list and registering a
Belgian Python website. “Stéphane continues to challenge us to organize bigger
and bigger events”, Gasc comments on Wirtel. His continued work promoting
Python in Belgium is helping provide the building blocks for a new Python
community in Belgium.

*  
*  

Python Software Foundation Marketing Work Group

*  
*  

As a member of the PSF marketing work group, Wirtel is an ongoing voice in the
discussion and creation of PSF marketing materials. Wirtel helped with flyer
development and distribution for  PythonFOSDEM 2015, PyCon North America 2015
and PyCon Ireland 2015.

*  
*  

Inspiring new CPython contributors at EuroPython 2016

*  
*  

Wirtel spoke at EuroPython this year on the topic of CPython. His talk, titled
“`Exploring our Python
Interprete <https://ep2016.europython.eu/conference/talks/exploring-our-
python-interpreter>`_r”, outlined the basics of how the Python interpreter
works. Of notable importance Wirtel framed his talk for CPython novices,
pointing out documentation on where to get started and resources for how to
find CPython core mentors. Wirtel also pointed to a CPython patch he recently
submitted for the __ltrace__ feature. With his
`patch <http://bugs.python.org/issue25571>`_ you can compile Python to easily
show the Python bytecode generated, a significant suggestion for beginners to
be able to play with in the Python interpreter. Here is an example of his
feature in action:

*  
*  

>>> __ltrace__ = None  # To enable tracing

>>> print("hello")     # Now, shows bytecodes run

0: LOAD_NAME, 0

push <built-in function print>

2: LOAD_CONST, 0

push 'hello'

4: CALL_FUNCTION, 1

ext_pop 'hello'

hello

ext_pop <built-in function print>

push None

6: PRINT_EXPR

pop None

8: LOAD_CONST, 1

push None

10: RETURN_VALUE

pop None

*  
*  

Some of Wirtel’s other projects includes working as a former core developer of
`Odoo <http://odoo.com/>`_ from 2008 to 2014, an open source enterprise resource
planner which is built with PostgreSQL and CPython. He has contributed to
Gunicorn and is working to contribute more to CPython. Wirtel is also a member
of the EuroPython Society and the Association Francophone de Python (AFPy) as
well as a PSF Fellow. Wirtel has supported EuroPython the last two years as a
volunteer and as a working group member too.

  

Wirtel’s passion for bringing new Pythonistas into the fold, be it through the
creation and continued organizing of the PythonFOSDEM Devroom or the
proliferation of CPython knowledge and tools particularly suited for the
beginner, is profound. As he noted in his EuroPython 2016 talk, he was
completely new to CPython at the 2014 PyCon North America at Montreal! “Simply
put Wirtel is the type of person who gets things done” Benetou says, adding
that “these are the type of people that inspire me, that I like”.

