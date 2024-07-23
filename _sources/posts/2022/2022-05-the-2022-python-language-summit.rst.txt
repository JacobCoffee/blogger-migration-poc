.. post:: 2022-05-11
   :tags: pycon, post, legacy-blogger
   :author: Python Software Foundation
   :category: Legacy
   :location: World
   :language: en

The 2022 Python Language Summit: Lightning talks
================================================

*This was originally posted on blogger* `here <https://pyfound.blogspot.com/2022/05/the-2022-python-language-summit.html>`_.

These were a series of short talks, each lasting around five minutes.

  

`Read the rest of the 2022 Python Language Summit coverage
here. <https://pyfound.blogspot.com/2022/05/the-2022-python-language-
summit_01678898482.html>`_

  

* * *

Lazy imports, with Carl Meyer
-----------------------------

Carl Meyer, an engineer at Instagram, presented on a proposal that has since
blossomed into `PEP 690 <https://peps.python.org/pep-0690/>`_: lazy imports, a
feature that has already been implemented in
`Cinder <https://github.com/facebookincubator/cinder>`_, Instagram’s
performance-optimised fork of CPython 3.8.

What’s a _lazy import_? Meyer explained that the core difference with lazy
imports is that the import does not happen until the imported object is
referenced.

Examples
~~~~~~~~

In the following Python module, `spam.py`, with lazy imports activated, the
module `eggs` would never in fact be imported since `eggs` is never referenced
after the import:

    
    
      
    
    
    # spam.py
    import sys
    import eggs
    
    
    def main():
        print("Doing some spammy things.")
        sys.exit(0)
    
    
    if __name__ == "__main__":
        main()
    
    
      
    
    
      
    

And in _this_ Python module, `ham.py`, with lazy imports activated, the
function `bacon_function` _is_ imported – but only right at the end of the
script, after we’ve completed a for-loop that’s taken a very long time to
finish:

    
    
      
    
    
    # ham.py
    
    import sys
    
    import time
    
    from bacon import bacon_function
    
    
    def main():
        for _ in range(1_000_000_000):
            print('Doing hammy things')
            time.sleep(1)
    
        bacon_function()
    
        sys.exit(0)
    
    
    if __name__ == "__main__":
        main()
    
    
      
    
    
      
    

Meyer revealed that the Instagram team’s work on lazy imports had resulted in
startup time improvements of up to 70%, memory usage improvements of up to
40%, and the elimination of almost all import cycles within their code base.
(This last point will be music to the ears of anybody who has worked on a
Python project larger than a few modules.)

Downsides
~~~~~~~~~

Meyer also laid out a number of costs to having lazy imports. Lazy imports
create the risk that `ImportError` (or any other error resulting from an
unsuccessful import) could potentially be raised… anywhere. Import side
effects could also become “even less predictable than they already weren’t”.

Lastly, Meyer noted, “If you’re not careful, your code might implicitly start
to require it”. In other words, you might unexpectedly reach a stage where –
because your code has been using lazy imports – it now no longer runs without
the feature enabled, because your code base has become a huge, tangled mess of
cyclic imports.

Where next for lazy imports?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Python users who have opinions either for or against the proposal are
encouraged to join `the discussion on
discuss.python.org <https://discuss.python.org/t/pep-690-lazy-imports/>`_.

  

* * *

Python-Dev versus Discourse, with Thomas Wouters
------------------------------------------------

This was less of a talk, and more of an announcement.

Historically, if somebody wanted to make a significant change to CPython, they
were required to post on `the python-dev mailing
list <https://mail.python.org/mailman3/lists/python-dev.python.org/>`_. The
Steering Council now views the alternative venue for discussion,
`discuss.python.org <http://discuss.python.org>`_, to be a superior forum in
many respects.

Thomas Wouters, Core Developer and Steering Council member, said that the
Steering Council was planning on loosening the requirements, stated in several
places, that emails had to be sent to python-dev in order to make certain
changes. Instead, they were hoping that
`discuss.python.org <http://discuss.python.org>`_ would become the authoritative
discussion forum in the years to come.

  

* * *

Asks from Pyston, with Kevin Modzelewski
----------------------------------------

Kevin Modzelewski, core developer of the `Pyston <https://www.pyston.org>`_
project, gave a short presentation on ways forward for CPython optimisations.
Pyston is a performance-oriented fork of CPython 3.8.12.

Modzelewski argued that CPython needed better benchmarks; the existing
benchmarks on `pyperformance <https://github.com/python/pyperformance>`_ were
“not great”. Modzelewski also warned that his “unsubstantiated hunch” was that
the `Faster CPython <https://pyfound.blogspot.com/2022/05/the-2022-python-
language-summit_2.html?m=1>`_ team had already accomplished “greater than one-
half” of the optimisations that could be achieved within the current
constraints. Modzelewski encouraged the attendees to consider future
optimisations that might cause backwards-incompatible behaviour changes.

  

* * *

Core Development and the PSF, with Thomas Wouters
-------------------------------------------------

This was another short announcement from Thomas Wouters on behalf of the
Steering Council. After sponsorship from Google providing funding for `the
first ever CPython Developer-In-
Residence <https://pyfound.blogspot.com/2021/04/the-psf-is-hiring-developer-
in.html>`_ (Łukasz Langa), Meta has provided sponsorship for a second year. The
Steering Council also now has sufficient funds to hire a second Developer-In-
Residence – and attendees were notified that they were open to the idea of
hiring somebody who was not currently a core developer.

  

* * *

“Forward classes”, with Larry Hastings
--------------------------------------

Larry Hastings, CPython core developer, gave a brief presentation on a
proposal he had `sent round to the python-dev mailing
list <https://groups.google.com/g/dev-python/c/AuvirC3UNFU?pli=1>`_ in recent
days: a “forward class” declaration that would avoid all issues with two
competing `typing` PEPs: `PEP 563 <https://peps.python.org/pep-0563/>`_ and `PEP
649 <https://peps.python.org/pep-0649/>`_. In brief, the proposed syntax would
look something like this:

    
    
      
    
    
      
    
    
    forward class X()
    
    continue class X:
        # class body goes here
        def __init__(self, key):
            self.key = key
    
    
      
    
    
      
    

In theory, according to Hastings, this syntax could avoid `issues around
runtime evaluation of annotations that have plagued PEP
563 <https://github.com/samuelcolvin/pydantic/issues/2678>`_, while also
circumventing many of `the edge cases that unexpectedly
fail <https://discuss.python.org/t/finding-edge-cases-for-
peps-484-563-and-649-type-annotations/14314>`_ in a world where PEP 649 is
implemented.

The idea was in its early stages, and reaction to the proposal was mixed. The
next day, at the Typing Summit, there was more enthusiasm voiced for a plan
laid out by Carl Meyer for a tweaked version of Hastings’s earlier attempt at
solving this problem: `PEP 649 <https://peps.python.org/pep-0649/>`_.

  

* * *

Better fields access, with Samuel Colvin
----------------------------------------

Samuel Colvin, maintainer of the `Pydantic <https://pydantic-
docs.helpmanual.io>`_ library, gave a short presentation on a proposal
(`recently discussed on
discuss.python.org <https://discuss.python.org/t/better-fields-access-and-
allowing-a-new-character-at-the-start-of-identifiers/14529>`_) to reduce name
clashes between field names in a subclass, and method names in a base class.

The problem is simple. Suppose you’re a maintainer of a library,
`whatever_library`. You release Version 1 of your library, and one user start
to use your library to make classes like the following:

    
    
    
    
    from whatever_library import BaseModel
    
    class Farmer(BaseModel):
        name: str
        fields: list[str]
    
    
      
    
    
      
    

Both the user and the maintainer are happy, until the maintainer releases
Version 2 of the library. Version 2 adds a method, `.fields()` to BaseModel,
which will print out all the field names of a subclass. But this creates a
name clash with your user’s existing code, wich has `fields` as the name of an
instance attribute rather than a method.

Colvin briefly sketched out an idea for a new way of looking up names that
would make it unambiguous whether the name being accessed was a method or
attribute.

    
    
      
    
    
      
    
    
    class Farmer(BaseModel):
        $name: str
        $fields: list[str]
    
    farmer = Farmer(name='Jones', fields=['meadow', 'highlands'])
    print(farmer.$fields)  # -> ['meadow', 'highlands']
    print(farmer.fields())  # -> ['name', 'fields']
    

