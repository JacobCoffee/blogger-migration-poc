.. post:: 2020-05-01
   :tags: post, legacy-blogger
   :author: Python Software Foundation
   :category: Legacy
   :location: World
   :language: en

Should All Strings Become f-strings? - Python Language Summit 2020
==================================================================

*This was originally posted on blogger* `here <https://pyfound.blogspot.com/2020/04/all-strings-become-f-strings-python.html>`_.

`![ <https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEikEBxyX3QjlRyq5sdnwlB_y-7ZFKYAYk8LmEI7kDgHTAZ_mebLKrRFb4_4X7ZF3lMy7x9NBkVhNbVHs_1XE7KieU4kUVlxzj968yzr5xytlsGEq9uG0R6blu5jwellmv1ZAw/s320/eric-
smith.jpg>`_](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEikEBxyX3QjlRyq5sdnwlB_y-7ZFKYAYk8LmEI7kDgHTAZ_mebLKrRFb4_4X7ZF3lMy7x9NBkVhNbVHs_1XE7KieU4kUVlxzj968yzr5xytlsGEq9uG0R6blu5jwellmv1ZAw/s1600/eric-
smith.jpg)

  
The first language change proposed this year was the most radical: to make
f-strings the default. Eric V. Smith, who wrote `the PEP for
f-strings <https://www.python.org/dev/peps/pep-0498/>`_ in 2015, said they are
the killer feature of Python 3.6, and they are the motivation for many of his
clients to move to Python 3. However, they are error-prone. It's common to
forget the "f" prefix:  

    
    
    x = 1
    # Forgot the f prefix.
    print("The value is {x}")

Smith has observed programmers f-prefixing all strings, whether they include
substitutions or not, just to avoid this mistake.  
  
`Read more 2020 Python Language Summit
coverage. <https://pyfound.blogspot.com/2020/04/the-2020-python-language-
summit.html>`_  
  

* * *

When f-strings were added in 3.6, it was suggested to make them the default,
but this was too big a breaking change. Besides, replacing all literal brace
characters with double braces would be ugly:  

    
    
    "A single pair of braces: {{}}"

In this year's Summit, Smith proposed again to make f-strings the default. The
following kinds of strings would become f-strings:  

  * ` "string"` — an f-string  

  * `f"string"` — still an f-string  

  * `r"string"` — a raw f-string  

Binary literals like b"string" would not become f-strings. Smith would add a
new "p" string prefix for plain strings, which would behave like ordinary
strings today.  

  * `p"string"` — a plain string  

Performance would not be affected: the runtime behavior of a string without
any substitutions would be the same as today. Plain strings would still have
some uses; for example, regular expressions that include braces, or as the
input to `str.format`. In Smith's opinion, f-strings have superseded
`str.format`, but several in the audience objected that `str.format` with a
plain string allows for late binding, and f-strings don't obviate
`str.format_map`.  
  
Smith acknowledged some problems with his idea. It would introduce yet another
string prefix. Flipping the master switch to enable f-mode would break some
code, so there must be a way to gradually enable the change module by module,
perhaps like:  

    
    
    from __future__ import all_fstrings
    

He was concerned the change was so drastic that the Python core developers
would never have the nerve to enable it without requiring a `future` import.
If so, the idea should be abandoned right away.  
  
Yarko Tymciurak asked via chat: "How do you describe to beginners what p'why
is this needed' is?" Smith conceded that p-strings make the language more
complicated, but, he said, "There's going to be very few p's in the wild, and
I think their explanation will be fairly obvious."  
  
Several attendees were enthusiastic to make the change. Brett Cannon said that
removing the need for f-prefix would make the language easier for beginners.  
  
Larry Hastings pointed out that PHP strings are format strings by default and
"the script kids love it." However, he wrote, "It seems to me this is solving
the problem of 'oh I forgot to put an f in front of my string', and not
noticing until it's too late. Is that problem bad enough that we have to
change the language? " Many agreed that f-strings by default would have been a
good idea if Python were beginning from scratch; however, Paul Moore, Guido
van Rossum, and others feared the disruption would outweigh the benefits.__
The group concluded that Smith should send his PEP to the mailing list for
further debate.

