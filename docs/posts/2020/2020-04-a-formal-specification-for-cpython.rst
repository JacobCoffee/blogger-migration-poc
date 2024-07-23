.. post:: 2020-04-30
   :tags: post, legacy-blogger
   :author: Python Software Foundation
   :category: Legacy
   :location: World
   :language: en

A formal specification for the (C)Python virtual machine - Python Language Summit 2020
======================================================================================

*This was originally posted on blogger* `here <https://pyfound.blogspot.com/2020/04/a-formal-specification-for-cpython.html>`_.

`![ <https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiSPQl1R9HZl2vs1mjLaITIeU56Oa6KEC-
hOTtVzWl80o73TXWSea0w5dhdWo21ReAPMvmtnHqLZzJ89XTmkjQp2_Fw2Xfc_8x8jY6x3n1i_YZx_TZ3nG7qzd0ulpxNjjYvug/s1600/mark-
shannon.jpg>`_](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiSPQl1R9HZl2vs1mjLaITIeU56Oa6KEC-
hOTtVzWl80o73TXWSea0w5dhdWo21ReAPMvmtnHqLZzJ89XTmkjQp2_Fw2Xfc_8x8jY6x3n1i_YZx_TZ3nG7qzd0ulpxNjjYvug/s1600/mark-
shannon.jpg)  
Mark Shannon began his presentation saying, "This should actually be titled A
_Semi_ -Formal Specification. I don't think we'll ever get to `the stage of
ML <http://www.scholarpedia.org/article/Standard_ML_language#Language_definition>`_,"
a language described with mathematical rigor. However, a _more_ formal
definition of Python would be useful. Authors of alternative Python
implementations would have a standard to go by, besides reading CPython's
source and testing for equivalent behavior on a variety of programs. "It seems
to work for Java so I don't see why it wouldn't work for Python," said
Shannon. It would be particularly helpful for anyone who wants to examine a
part of the language. Today, one cannot understand CPython's bytecode
interpreter without studying all its quirky interactions with the C API, the
code loader, and so on; a Python specification would break down the language
into domains that could be grasped separately.  
  
A specification would clean up edge cases. Shannon said there are "too many
weird bugs relating to interactions of threads and generators and locals and
various other bits and pieces." If the language were defined, developers would
at least know how it's supposed to behave.  
  
`Read more 2020 Python Language Summit
coverage <https://pyfound.blogspot.com/2020/04/the-2020-python-language-
summit.html>`_.  

* * *

Shannon proposed to split Python's specifications into major components: code
loading (including imports and parsing), execution, and the C API. The
components' specs would be allowed to refer to each other, but only at a high
level. In his Language Summit presentation, Shannon focused on the execution
component.  
  
A Python execution spec would define the virtual machine (VM) as a set of
variables, such as the list of threads and their call stacks, and it would
define small steps that transition from one VM state to the next. For example,
a Python function call involves these steps:  

  * Create a new stack frame  

  * Move arguments from current frame to the new one  

  * Save the next instruction pointer  

  * Push the new frame onto the call stack  

  * Continue

Every definition ends with "continue", meaning that the interpreter proceeds
to the next step.  
Writing a specification for Python is a chance to rethink how its parts
relate. CPython's generators are implemented in terms of iterators, because
iterators were built first. But generators are a more basic and flexible
concept; starting from scratch it's natural to _define_ iterators in terms of
generators. Shannon presented `a sketch of such a
definition <https://github.com/markshannon/python_formal_semantics/blob/master/examples/iteration_and_generators.md>`_.  
  
The next steps for Shannon's project are to define the spec's format, list its
components, and decide what to do about "awkward" language features such as
`sys.settrace()`. He concluded that a semi-formal spec of Python would help
alternative implementations match CPython, would make PEPs less ambiguous, and
would clarify whether any existing "odd behavior is a feature or a bug." It
would be possible to reason about the correctness of optimizations. However,
writing the spec is work, and it could deter good PEPs in the future if
authors are daunted by writing their proposals in terms of the spec.  
  
The audience's questions revealed their confusion about Shannon's idea. Larry
Hastings admitted he had "lots of trouble following this." Was Shannon
proposing a new language implementation based on the spec? Shannon said no,
the spec's purpose was to describe and reason about CPython and other
implementations. A. Jesse Jiryu Davis wondered if the spec would be written in
a formal modeling language like
`TLA+ <https://lamport.azurewebsites.net/tla/tla.html>`_ or
`Alloy <https://alloytools.org/about.html>`_, but Shannon felt that would
discourage contributors. English would be the language of the spec; the `JVM
spec <https://docs.oracle.com/javase/specs/jvms/se7/html/>`_ demonstrates this
approach.  
  
Brett Cannon asked if PEPs for new language features would require spec
patches. Shannon replied that PEPs for deep changes, similar to `the
introduction of yield from <https://www.python.org/dev/peps/pep-0380/>`_ in
Python 3.3, would benefit if they were described in terms of the spec.  
  
The presentation ended with the attendees saying a Python specification might
be a good idea, but struggling to envision it and how it would be used in
practice.

