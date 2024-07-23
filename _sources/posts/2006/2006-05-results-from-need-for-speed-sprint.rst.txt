.. post:: 2006-05-27
   :tags: post, legacy-blogger
   :author: Python Software Foundation
   :category: Legacy
   :location: World
   :language: en

Results from the Need For Speed sprint
======================================

*This was originally posted on blogger* `here <https://pyfound.blogspot.com/2006/05/results-from-need-for-speed-sprint.html>`_.

The Need For Speed sprint in Reykjavik, Iceland, is winding down today, and
Steve Holden has posted `a summary of the
results <http://holdenweb.blogspot.com/2006/05/need-for-speed-wrap-up.html>`_.
The gains are impressive:

  * Several string methods such as `.find()` and `.replace()` are now much faster; some methods are up to 4 times or even 25 times faster! (Work by Andrew Dalke and Fredrik Lundh.) 
  * Exception handling is now 30% faster than in Python 2.4. (Work by Georg Brandl, Richard Jones, and Sean Reifschneider.) 
  * The `struct` module now precompiles format strings and is about 20% faster. (Work by Martin Blais, Bob Ippolito.) 
  * The interpreter can be built using Microsoft Visual Studio 8's profile-driven optimizations. (Work by Kristjan Jonsson, Richard Tew.) 
  * Georg Brandl and Jack Diederich began a rewrite of the `decimal` module into C, laying the foundations for a Summer of Code student to complete the work. 

And there's even more! A complete list of the improvements made at the sprint
are recorded in `the Successes wiki
page <http://wiki.python.org/moin/NeedForSpeed/Successes>`_.

Thanks to the participants, to CCP Games for their support, and to the
sprint's sponsor, EWT LLC.

