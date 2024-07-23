.. post:: 2020-05-13
   :tags: post, legacy-blogger
   :author: Python Software Foundation
   :category: Legacy
   :location: World
   :language: en

6 Ways Salesforce Gets Things Done with Python
==============================================

*This was originally posted on blogger* `here <https://pyfound.blogspot.com/2020/05/6-ways-salesforce-gets-things-done-with.html>`_.

Salesforce Engineering puts Python to work across many areas of their
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
business.

Read on to see how they use python in machine learning, security, internal
devops teams and more.  
  
The Python programming language has strong ties to both engineering and
science disciplines, which gives its users access to a wide number of
libraries to solve both practical and theoretical problems. We put it to work
across Salesforce.org (our non-profit product arm), Heroku, Salesforce
Einstein, Industries and Service Clouds, internal devops teams, and more.  

  

`![ <https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg6bIS0Id4Zp6-ToKe9HdIZbyZwm3XYEi7QQEb6AGvyUB4JjLl0fcsV43-krvXd9uoM_phV5uKUOrWU3ZchCXcrNZho9UNDkrbS22PJstw2UazLcoHokWbMan2YuN1G1Ed9UQ/s320/iStock-1136011446.jpg>`_](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg6bIS0Id4Zp6-ToKe9HdIZbyZwm3XYEi7QQEb6AGvyUB4JjLl0fcsV43-krvXd9uoM_phV5uKUOrWU3ZchCXcrNZho9UNDkrbS22PJstw2UazLcoHokWbMan2YuN1G1Ed9UQ/s1600/iStock-1136011446.jpg)

  

Here are 6 things we use Python to do (and you can too!) through
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
projects we’ve open sourced:

  

*1\. Conquer the Natural Language Decathlon by performing ten disparate
natural language tasks (`DecaNLP <http://decanlp.com/>`_).*

  
_Deep learning has significantly improved state-of-the-art performance for
natural language processing (NLP) tasks, but each one is typically studied in
isolation. The Natural Language Decathlon (decaNLP) is a new benchmark for
studying general NLP models that can perform a variety of complex, natural
language tasks. By requiring a single system to perform ten disparate natural
language tasks, decaNLP offers a unique setting for multitask, transfer, and
continual learning._

_  
_

*2\. Create SSL/TLS client fingerprints that are easy to produce on any
platform and can be easily shared for threat intelligence
(`JA3 <https://github.com/salesforce/ja3>`_).*

  
_JA3 gathers the decimal values of the bytes for the following fields in the
Client Hello packet; SSL Version, Accepted Ciphers, List of Extensions,
Elliptic Curves, and Elliptic Curve Formats. It then concatenates those values
together in order, using a “,” to delimit each field and a “-” to delimit each
value in each field._

_  
_*3\. Use Google Sheets like tables in code
(`pygsheetsorm <https://github.com/salesforce/pygsheetsorm>`_).*

_  
_

_Ever wanted to be able to use a Google Sheet like a table in your code? How
about if you could get a list of objects that automatically mapped column
headers into properties? Then this project is for you! This is a simple
interface on top of`pygsheets <https://pygsheets.readthedocs.io/en/stable/>`_._

_  
_

*4\. Get rid of silent errors in Perforce syncs
(`o4 <https://github.com/salesforce/o4>`_).*

*  
*

_At Salesforce, we use Perforce at a very large scale. A scale that exposes
some shortcomings in p4 itself. o4 was created to improve reliability of a
sync and increase scalability in our very large-scale CI. What that boils down
to is the rather horrendous reality that a p4 sync makes most of the changes
to your local files. o4 allows you to continue using Perforce and all the
associated tools and IDE plugins, without the uncertainty around a sync. Every
sync is guaranteed perfect, every single time. In the rare occurrence that a
sync could not be met to 100%, o4 will fail loudly. Crash and burn. No more
silent errors! In addition to that, o4 allows some dramatic improvements to
CI._

_  
_*5\. Automatically verify, de-duplicate, and suggest payouts for
vulnerability reports through HackerOne
(`AutoTriageBot <https://github.com/salesforce/AutoTriageBot>`_).*

*  
*

_This bot can automatically verify reports about XSS, SQLi, and Open Redirect
vulnerabilities (via both GET and POST). In addition, it is built in a modular
manner so that it can be easily expanded to add tests for other classes of
vulnerabilities._

_  
_*6\. Run continuous integration from the command line for Salesforce Managed
Package applications (`CumulusCI <https://github.com/SFDO-
Tooling/CumulusCI>`_).*

  
_Out of the box, CumulusCI provides a complete best practice development and
release process based on the processes used by Salesforce.org to build and
release managed packages to thousands of users. It offers a flexible and
pluggable system for running tasks (single actions) and flows (sequences of
tasks) and an OAuth-based org keychain allowing easy connection to Salesforce
orgs and stored in local files using AES encryption._

_  
_

_*.   .  .*_
^^^^^^^^^^^^^^

  

Still want more Python? Check out all of the Salesforce `Open Source projects
built in Python
 <https://github.com/salesforce?utf8=%E2%9C%93&q=&type=&language=python>`_on
GitHub.

_  
_

WRITTEN BY

  

Laura Lindeman

Voracious reader & crafter of words. organizer extraordinaire. #peoplegeek at
Salesforce on the Tech & Products Innovation & Learning team.

  

