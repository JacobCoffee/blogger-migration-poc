.. post:: 2019-05-15
   :tags: post, legacy-blogger
   :author: Python Software Foundation
   :category: Legacy
   :location: World
   :language: en

Paul Ganssle: Time Zones In The Standard Library
================================================

*This was originally posted on blogger* `here <https://pyfound.blogspot.com/2019/05/paul-ganssle-time-zones-in-standard.html>`_.

Python boasts that it comes with “batteries included,” but programmers have
long been frustrated at one set of missing batteries: the standard library
does not include any time zone definitions. The datetime module supports the
_idea_ of time zones, but a programmer who wants to know when Daylight Saving
Time starts in Cleveland must install a third-party package. Paul Ganssle
spoke to the Python Language Summit to offer a solution. Ganssle maintains the
PyPI package dateutil, and contributes to the standard library datetime
module. He described the state of Python time zone support and how time zone
definitions could be added to the standard library.

  
`Read more 2019 Python Language Summit
coverage <https://pyfound.blogspot.com/2019/05/the-2019-python-language-
summit.html>`_.  
  

Python Comes With Limited Time Zone Support
===========================================

  
A time zone is a function that maps a naïve time to an unambiguous Coordinated
Universal Time (UTC). Individual time zones can be quite eccentric, so Python
does not attempt to define time zone logic, it simply provides an abstract
base class TZInfo that is subclassed by implementors. Although there could
theoretically be unlimited kinds of time zones, most programmers encounter
three concrete types:  
  
1\. UTC or a fixed offset from it.  
  
2\. Local time.  
  
3\. A time zone from the `IANA
database <https://en.wikipedia.org/wiki/Tz_database>`_.  
  
The first of these was added to the standard library in Python 3.2. Ganssle
said, “Whenever I teach people about datetimes, it's really nice to be able to
say, if you're using Python 3, you can just have a UTC object.” The purpose of
Ganssle’s proposal was to add the second and third.  
  

Ambiguous Times
===============

  
Ganssle explained that when Eastern Daylight Time ends, clocks are set back
from 2:00am to 1:00am, thus there are two UTC times that map to 1:30am local
time on that day:  
  

    
    
    >>> NYC = tz.gettz("America/New_York")
    >>> dt0 = datetime(2004, 10, 31, 5, 30, tzinfo=tz.UTC)
    >>> print(dt0.astimezone(NYC))
    2004-10-31 01:30:00-04:00
    >>> print((dt0 + timedelta(hours=1)).astimezone(NYC))
    2004-10-31 01:30:00-05:00
    

  
`PEP 495 <https://www.python.org/dev/peps/pep-0495/>`_ solved the problem of
ambiguous times by adding the “fold” attribute to datetime objects. A datetime
with fold=0 is the first occurrence of that local time, the second occurrence
has fold=1. With this addition, standard Python provides all the prerequisites
for proper time zones, so Ganssle argued they should now be added to the
standard library.  
  

How To Maintain The Time Zone Definitions?
==========================================

  
`![ <https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiL5lRvZsHGGrOmc3g4FtbMXfib5w651GYduMF96UlvFr06j_PwtS5tNjYQFBknoTQYsDMsum0G37k7y9CPq8KaKkCJv_WQ0P_gjFWMRs-
nRqGQOTYlJmLaMrpehG-QGPW0KA/s400/paul-
ganssle.jpg>`_](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiL5lRvZsHGGrOmc3g4FtbMXfib5w651GYduMF96UlvFr06j_PwtS5tNjYQFBknoTQYsDMsum0G37k7y9CPq8KaKkCJv_WQ0P_gjFWMRs-
nRqGQOTYlJmLaMrpehG-QGPW0KA/s1600/paul-ganssle.jpg)IANA time zones are the de
facto standard for time zone data, and they ship with many operating systems.
Both Ganssle’s dateutil and the competing pytz package use the IANA database
as their source of truth. Therefore it would be natural to include the IANA
time zones in the Python standard library, but this presents a problem: the
IANA database changes every time a government changes a time zone, which
occurs as often as 20 times a year. Time zone changes are far more frequent
than Python releases.  
  
Ganssle offered two solutions for updating time zone data, and then offered a
compromise between them as his actual proposal. The first solution is to rely
on the operating system’s time zone database. Python could rely on the system
update mechanism to refresh this data, and it would use the same time zone
definitions as most other applications. System time zone data is not
officially supported on Windows, however, and is not always installed on
Linux.  
  
The second solution is to publish IANA time zone definitions as a PyPI
package. It could be updated frequently, but the core team would have to
invent some way to notify users when it is time to update their time zone
data. Plus, it would be risky for Python to use different time zones than the
rest of the system.  
  
Ganssle proposed a hybrid: the Python standard library should use the system’s
time zone data if possible, otherwise fall back to a PyPI package which would
be installed conveniently, analogous to installing pip with “ensurepip” today.  
  

The Local Time Zone
===================

  
Naïve times in Python are sometimes treated as times in the local time zone,
sometimes not. Ganssle showed an example demonstrating that if a programmer
converts a naïve time to UTC, Python assumes its original time zone is local:  
  

    
    
    >>> dt = datetime(2020, 1, 1, 12)
    >>> dt.astimezone(timezone.utc)
    2020-01-01 17:00:00+00:00
    

  
However, adding a naïve time to a UTC time is prohibited:  
  

    
    
    >>> datetime(2020, 1, 1, 12) - datetime(2020, 1, 1, tzinfo=timezone.utc)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: can't subtract offset-naive and offset-aware datetimes
    

  
Ganssle’s dateutil package offers a more thorough implementation of “local
time zone”, and he thinks Python programmers would appreciate local times in
the standard library. To add them, however, the core team must first handle
the astonishing behavior of local times when the system time zone changes. The
first surprise is that changing the system time zone has no effect until the
Python program calls time.tzset(). (And on Windows, time.tzset() is not
available.) The second surprise is that changing system time and then calling
time.tzset() changes the UTC offset of _existing_ times created before the
change.  
  
Ganssle proposed several ways the standard library could act in this scenario.
It could ignore changes to the system time zone while a Python program is
running, or it could detect time zone changes but avoid mutating the offsets
of existing time objects. He had no opinion about the best outcome.  
  

Conclusion
==========

  
Ned Deily wondered what Ganssle’s proposal would solve that which
`pytz <https://pypi.org/project/pytz/>`_ does not. Ganssle responded that pytz’s
author has stopped maintaining the package because he believes time zones
should move to the standard library. Full time zone is a basic feature that
should always be available. In Ganssle’s view, however, his own dateutil is a
better package to emulate than pytz. “I would take dateutil, clean up some of
the rough edges, and propose it as some of the batteries that would be
included.”  
  
Łukasz Langa said that he planned, as Python 3.8’s release manager, to issue
monthly patch releases, and he thought that should be frequent enough to keep
users’ time zone data updated. Russell Keith-Magee said no, `North Korea once
announced a time zone change with three days’
notice <https://www.washingtonpost.com/news/worldviews/wp/2018/05/04/the-
brief-history-of-north-koreas-time-
zone/?noredirect=on&utm_term=.d329bf1cf474>`_. Other audience members thought
this scenario was obscure, and the PEP should not be required to handle such
emergencies.  
  
At the end of his talk Ganssle summarized his proposal. He believes that the
standard library should support IANA time zones, using the operating system as
the source of time zone data or falling back to a PyPI package. There are
several options for handling local time zone changes at runtime. The design
should be formalized in at least an informational PEP, “if not one where it's
contentious and we all hate each other at the end of it.”

