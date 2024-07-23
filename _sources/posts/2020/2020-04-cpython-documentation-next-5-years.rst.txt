.. post:: 2020-04-30
   :tags: post, legacy-blogger
   :author: Python Software Foundation
   :category: Legacy
   :location: World
   :language: en

CPython Documentation: The Next 5 Years - Python Language Summit 2020
=====================================================================

*This was originally posted on blogger* `here <https://pyfound.blogspot.com/2020/04/cpython-documentation-next-5-years.html>`_.

`![ <https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi7WSiAR219ao2GGAxQPp79AD6jezdwSHpASJX65OtfDXiL-
baElS_2WxHusWvKzlvZbVtmGoXUQCT5XD9q_36ccw3INzTBAaAKt5ioXGIgfnj6z5m5wV1MNEtDrMKzmKiLig/s1600/carol-
willing-and-ned-
batchelder.jpg>`_](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi7WSiAR219ao2GGAxQPp79AD6jezdwSHpASJX65OtfDXiL-
baElS_2WxHusWvKzlvZbVtmGoXUQCT5XD9q_36ccw3INzTBAaAKt5ioXGIgfnj6z5m5wV1MNEtDrMKzmKiLig/s1600/carol-
willing-and-ned-batchelder.jpg)  

"Documentation is the way we communicate with each other," said Willing.
"Historically, we've done a great job with documentation." But the environment
is changing: Python's BDFL has retired, and Python's user base is expanding,
becoming more global, and moving away (to some degree) from lower-level
programming to higher-level applications. These changes impose new
documentation burdens on the small core team. Willing said, "We don't scale
well."  

`Read more 2020 Python Language Summit
coverage <https://pyfound.blogspot.com/2020/04/the-2020-python-language-
summit.html>`_.  

* * *

Willing and Ned Batchelder proposed a new `Python Steering
Council <https://www.python.org/dev/peps/pep-0013/>`_ workgroup called the
"Documentation Editorial Board". Its members would include core developers and
community members; they would write style guides, manage translations into
non-English languages, and create a landing page that guides different kinds
of users to the documentation that suits them. (Daniele Procida had shared
earlier `a guide to writing docs <https://documentation.divio.com/>`_ for a
variety of users' needs.) The core team need not write all the docs
themselves—they should be owned and written by the community, along with the
core team, overseen by the new Editorial Board.  

In the Editorial Board's first year it would focus on governance,
translations, the new landing page, and tutorials. Willing was inspired by the
core team's `overhaul of the asyncio
docs <https://bugs.python.org/issue33649>`_; they added tutorials and split the
high-level information from the low-level. The rest of the standard library
would serve users better with more tutorials like asyncio's. Style guides
would ensure consistency and best practices. As Ned Batchelder pointed out,
Python has two PEPs for code style (`one for
C <https://www.python.org/dev/peps/pep-0007/>`_ and `one for
Python <https://www.python.org/dev/peps/pep-0008/>`_), but none for
documentation.  

In its second year, the Board would measure its effectiveness so far, and
begin running documentation sprints. Willing recommends the Board begin annual
editorial reviews, seeking patterns of user confusion: "When users ask
questions on mailing lists and the bug tracker, it means something's not clear
to them." Updating the documentation to fix common misunderstandings would
save time in the long run for users and the core team.  

Batchelder observed that "twenty-five years ago, our main audience seemed to
be refugees from C," but most readers of the Python docs today are not career
software developers at all; they need different docs.  

Raymond Hettinger asked, "Any thoughts on why no one stepped up to write
*any* docs for the `walrus
operator <https://www.python.org/dev/peps/pep-0572/>`_? I'm not seeing people
volunteering for major documentation efforts. Mostly the contributions are
minor, micro edits." Willing replied that the walrus operator specifically was
a "hot potato" that deterred volunteers. In general, the Python core team
doesn't encourage others to lead big documentation projects; community members
don't have a sense of ownership over the docs, nor the authority to merge
their changes, so skilled writers take their efforts elsewhere. The proposed
new Editorial Board would help to change that.  

Sumana Harihareswara asked how documentation work would be funded, and whether
professional technical writers might be involved. Willing replied that the PSF
will fund some work, but she emphasized recruiting volunteers from the
community. Several in the audience asked about making a "core documenter" role
analogous to "core developer"; Batchelder replied that fine-grained roles and
permissions in open source projects are counterproductive. People who write
excellent documentation should simply be promoted to core developers.  

