.. post:: 2023-05-29
   :tags: pycon, post, legacy-blogger
   :author: Python Software Foundation
   :category: Legacy
   :location: World
   :language: en

The Python Language Summit 2023: Pattern Matching, __match__, and View Patterns
===============================================================================

*This was originally posted on blogger* `here <https://pyfound.blogspot.com/2023/05/the-python-language-summit-2023-pattern.html>`_.

One of the most exciting new features in Python 3.10 was `the introduction of
pattern
matching <https://docs.python.org/3/whatsnew/3.10.html#pep-634-structural-
pattern-matching>`_ (introduced in PEPs
`634 <https://peps.python.org/pep-0634/>`_,
`635 <https://peps.python.org/pep-0635/>`_ and
`636 <https://peps.python.org/pep-0636/>`_). Pattern matching has a wide variety
of uses, but really shines in situations where you need to undergo complex
destructurings of tree-like datastructures.

That’s a lot of words which may or may not mean very much to you – but
consider, for example, using `the `ast`
module <https://docs.python.org/3/library/ast.html>`_ to parse Python source
code. If you’re unfamiliar with the `ast` module: the module provides tools
that enable you to compile Python source code into an “abstract syntax tree”
(AST) representing the code’s structure. The Python interpreter itself
converts Python source code into an AST in order to understand how to run that
code – but parsing Python source code using ASTs is also a common task for
linters, such as plugins for `flake8 <https://flake8.pycqa.org/en/latest/>`_ or
`pylint <https://www.pylint.org>`_. In the following example, `ast.parse()` is
used to parse the source code `x = 42` into an `ast.Module` node, and
`ast.dump()` is then used to reveal the tree-like structure of that node in a
human-readable form:

  

    
    
    >>> import ast
    >>> source = "x = 42"
    >>> node = ast.parse(source)
    >>> node
    <ast.Module object at 0x000002A70F928D80>
    >>> print(ast.dump(node, indent=2))
    Module(
      body=[
        Assign(
          targets=[
            Name(id='x', ctx=Store())],
          value=Constant(value=42))],
      type_ignores=[])
    

  

How does working with ASTs relate to pattern-matching? Well, a function to
determine whether (to a reasonable approximation) an arbitrary AST node
represents the symbol `collections.deque` might have looked something like
this, before pattern matching…

  

    
    
    import ast
    
    # This obviously won't work if the symbol is imported with an alias
    # in the source code we're inspecting
    # (e.g. "from collections import deque as d").
    # But let's not worry about that here :-)
    
    def node_represents_collections_dot_deque(node: ast.AST) -> bool:
        """Determine if *node* represents 'deque' or 'collections.deque'"""
        return (
            isinstance(node, ast.Name) and node.id == "deque"
        ) or (
            isinstance(node, ast.Attribute)
            and isinstance(node.value, ast.Name)
            and node.value.id == "collections"
            and node.value.attr == "deque"
        )
    

  

But in Python 3.10, pattern matching allows an elegant destructuring syntax:

  

    
    
    import ast
    
    def node_represents_collections_dot_deque(node: ast.AST) -> bool:
        """Determine if *node* represents 'deque' or 'collections.deque'"""
        match node:
            case ast.Name("deque"):
                return True
            case ast.Attribute(ast.Name("collections"), "deque"):
                return True
            case _:
                return False
    

  

I know which one _I_ prefer.

For some, though, this still isn’t enough – and Michael “Sully” Sullivan is
one of them. At the `Python Language Summit
2023 <https://pyfound.blogspot.com/2023/05/the-python-language-
summit-2023_29.html>`_, Sullivan shared ideas for where pattern matching could
go next.

  

* * *

Playing with matches (`without getting
--------------------------------------
burned <https://www.youtube.com/watch?v=DJeMfTdvVo8>`_)

  

Sullivan’s contention is that, while pattern matching provides elegant
syntactic sugar in simple cases such as the one above, our ability to chain
destructurings using pattern matching is currently fairly limited. For
example, say we want to write a function inspecting Python AST that takes an
`ast.FunctionDef` node and identifies whether the node represents a
synchronous function with exactly two parameters, both of them annotated as
accepting integers. The function would behave so that the following holds
true:

  

    
    
    >>> import ast
    >>> source = "def add_2(number1: int, number2: int): pass"
    >>> node = ast.parse(source).body[0]
    >>> type(node)
    <class 'ast.FunctionDef'>
    >>> is_function_taking_two_ints(node)
    True
    

  

With pre-pattern-matching syntax, we might have written such a function like
this:

  

    
    
    def is_int(node: ast.AST | None) -> bool:
        """Determine if *node* represents 'int' or 'builtins.int'"""
        return (
            isinstance(node, ast.Name) and node.id == "int"
        ) or (
            isinstance(node, ast.Attribute)
            and isinstance(node.value, ast.Name)
            and node.value.id == "builtins"
            and node.attr == "int"
        )
    
    def is_function_taking_two_ints(node: ast.FunctionDef) -> bool:
        """Determine if *node* represents a function that accepts two ints"""
        args = node.args.posonlyargs + node.args.args
        return len(args) == 2 and all(is_int(node.annotation) for node in args)
    

  

  

If we wanted to rewrite this using pattern matching, we could possibly do
something like this:

  

    
    
    def is_int(node: ast.AST | None) -> bool:
        """Determine if *node* represents 'int' or 'builtins.int'"""
        match node:
            case ast.Name("int"):
                return True
            case ast.Attribute(ast.Name("builtins"), "int"):
                return True
            case _:
                return False
    
    def is_function_taking_two_ints(node: ast.FunctionDef) -> bool:
        """Determine if *node* represents a function that accepts two ints"""
        match node.args.posonlyargs + node.args.args:
            case [ast.arg(), ast.arg()] as arglist:
                return all(is_int(arg.annotation) for arg in arglist)
            case _:
                return False
    

  

That leaves a lot to be desired, however! The `is_int()` helper function can
be rewritten in a _much_ cleaner way. But integrating it into the
`is_function_taking_two_ints()` is… somewhat icky! The code feels _harder_ to
understand than before, whereas the goal of pattern matching is to improve
readability.

Something like this, (ab)using metaclasses, gets us a lot closer to what it
feels pattern matching _should_ be like. By using one of Python’s hooks for
customising `isinstance()` logic, it’s possible to rewrite our `is_int()`
helper function as a class, meaning we can seamlessly integrate it into our
`is_function_taking_two_ints()` function in a very expressive way:

  

    
    
    import abc
    import ast
    
    class PatternMeta(abc.ABCMeta):
        def __instancecheck__(cls, inst: object) -> bool:
            return cls.match(inst)
    
    class Pattern(metaclass=PatternMeta):
        """Abstract base class for types representing 'abstract patterns'"""
        @staticmethod
        @abc.abstractmethod
        def match(node) -> bool:
            """Subclasses must override this method"""
            raise NotImplementedError
    
    class int_node(Pattern):
        """Class representing AST patterns signifying `int` or `builtins.int`"""
        @staticmethod
        def match(node) -> bool:
            match node:
                case ast.Name("int"):
                    return True
                case ast.Attribute(ast.Name("builtins"), "int"):
                    return True
                case _:
                    return False
    
    def is_function_taking_two_ints(node: ast.FunctionDef) -> bool:
        """Determine if *node* represents a function that accepts two ints"""
        match node.args.posonlyargs + node.args.args:
            case [
                ast.arg(annotation=int_node()), 
                ast.arg(annotation=int_node()),
            ]:
                return True
            case _:
                return False
    

  

This is still hardly ideal, however – that’s a lot of boilerplate we’ve had to
introduce to our helper function for identifying `int` annotations! And who
wants to muck about with metaclasses?

  

`![ <https://blogger.googleusercontent.com/img/a/AVvXsEjz18FEpI2W8Dx9w0LUFcj4KhCu2ml9sKxdPh33P6IBGuLx65qgBsTMJTwHPXtX7CzPYtkL81sxGJv8RJ8RQlCwKKkGy7epUxp4io7PRMeO6_ZAWF1yvlWqtg6cEiGtwhcRUl-8F7g8M3p8jwKK2b-9YHEbaacoz8OUi4LglXSPXvo3maY>`_](https://blogger.googleusercontent.com/img/a/AVvXsEjz18FEpI2W8Dx9w0LUFcj4KhCu2ml9sKxdPh33P6IBGuLx65qgBsTMJTwHPXtX7CzPYtkL81sxGJv8RJ8RQlCwKKkGy7epUxp4io7PRMeO6_ZAWF1yvlWqtg6cEiGtwhcRUl-8F7g8M3p8jwKK2b-9YHEbaacoz8OUi4LglXSPXvo3maY)  
---  
A slide from Sullivan's talk  
  
  

* * *




A `__match__` made in heaven?
-----------------------------

  

Sullivan proposes that we make it easier to write helper functions for pattern
matching, such as the example above, without having to resort to custom
metaclasses. Two competing approaches were brought for discussion.

The first idea – a `__match__` special method – is perhaps the easier of the
two to immediately grasp, and appeared in early drafts of the pattern matching
PEPs. (It was eventually removed from the PEPs in order to reduce the scope of
the proposed changes to Python.) The proposal is that any class could define a
`__match__` method that could be used to customise how match statements apply
to the class. Our `is_function_taking_two_ints()` case could be rewritten like
so:

  

    
    
    class int_node:
        """Class representing AST patterns signifying `int` or `builtins.int`"""
        # The __match__ method is understood by Python to be a static method,
        # even without the @staticmethod decorator,
        # similar to __new__ and __init_subclass__
        def __match__(node) -> ast.Name | ast.Attribute:
            match node:
                case ast.Name("int"):
                    # Successful matches can return custom objects,
                    # that can be bound to new variables by the caller
                    return node
                case ast.Attribute(ast.Name("builtins"), "int"):
                    return node
                case _:
                    # Return `None` to indicate that there was no match
                    return None
    
    def is_function_taking_two_ints(node: ast.FunctionDef) -> bool:
        """Determine if *node* represents a function that accepts two ints"""
        match node.args.posonlyargs + node.args.args:
            case [
                ast.arg(annotation=int_node()), 
                ast.arg(annotation=int_node()),
            ]:
                return True
            case _:
                return False
    

  

The second idea is more radical: the introduction of some kind of new syntax
(perhaps reusing Python’s `->` operator) that would allow Python coders to
“apply” functions during pattern matching. With this proposal, we could
rewrite `is_function_taking_two_ints()` like so:

  

    
    
    def is_int(node: ast.AST | None) -> bool:
        """Determine if *node* represents 'int' or 'builtins.int'"""
        match node:
            case ast.Name("int"):
                return True
            case ast.Attribute(ast.Name("builtins"), "int"):
                return True
            case _:
                return False
    
    def is_function_taking_two_ints(node: ast.FunctionDef) -> bool:
        """Determine if *node* represents a function that accepts two ints"""
        match node.args.posonlyargs + node.args.args:
            case [
                ast.arg(annotation=is_int -> True),
                ast.arg(annotation=is_int -> True),
            ]
            case _:
                return False
    

  

  

* * *




Match-maker, match-maker, `make me a
------------------------------------
`__match__` <https://www.youtube.com/watch?v=59Hj7bp38f8>`_…

  

  

`![ <https://blogger.googleusercontent.com/img/a/AVvXsEjMxObGvaIvslDc98eA-L5NJPCh56mPTurCwLIsqKxY3BHmVUaXFKcXLdFJgNMG2Ag0MxL3Q4kagE0SAAIFH-
KNhuSa3k6BL0sWhn5dWK1ro1DJy7FhPwVDaZKr1o0aToh_MTmnIKy6NAFZGSSfPj1CDSBlw1tdPoUm_R-N4Z-hMnRTl4M>`_](https://blogger.googleusercontent.com/img/a/AVvXsEjMxObGvaIvslDc98eA-L5NJPCh56mPTurCwLIsqKxY3BHmVUaXFKcXLdFJgNMG2Ag0MxL3Q4kagE0SAAIFH-
KNhuSa3k6BL0sWhn5dWK1ro1DJy7FhPwVDaZKr1o0aToh_MTmnIKy6NAFZGSSfPj1CDSBlw1tdPoUm_R-N4Z-hMnRTl4M)  
---  
A slide from Sullivan's talk  
  
  

The reception in the room to Sullivan’s ideas was positive; the consensus
seemed to be that there was clearly room for improvement in this area. Brandt
Bucher, `author of the original pattern matching implementation in Python
3.10 <https://www.youtube.com/watch?v=XpxTrDDcpPE>`_, concurred that this kind
of enhancement was needed. Łukasz Langa, meanwhile, said he’d received many
queries from users of other programming languages such as C#, asking how to
tackle this kind of problem.

The proposal for a `__match__` special method follows a pattern common in
Python’s data model, where double-underscore “dunder” methods are overridden
to provide a class with special behaviour. As such, it will likely be less
jarring, at first glance, to those new to the idea. Attendees of Sullivan’s
talk seemed, broadly, to slightly prefer the `__match__` proposal, and
Sullivan himself said he thought it “looked prettier”.

Jelle Zijlstra argued that the `__match__` dunder would provide an elegant
symmetry between the construction and destruction of objects. Brandt Bucher,
meanwhile, said he thought the usability improvements weren’t significant
enough to merit new syntax.

Nonetheless, the alternative proposal for new syntax also has much to
recommend it. Sullivan argued that having dedicated syntax to express the idea
of “applying” a function during pattern matching was more explicit. Mark
Shannon agreed, noting the similarity between this idea and features in the
Haskell programming language. “This is functional programming,” Shannon
argued. “It feels weird to apply `OOP <https://en.wikipedia.org/wiki/Object-
oriented_programming>`_ models to this.”

  

* * *




Addendum: pattern-matching resources and recipes
------------------------------------------------

  

In the meantime, while we wait for a PEP, there are plenty of innovative uses
of pattern matching springing up in the ecosystem. For further
reading/watching/listening, I recommend:

  * `“A perfect `match`: The history, design and future of Python’s structural pattern matching” <https://www.youtube.com/watch?v=XpxTrDDcpPE>`_ – A talk by Brandt Bucher at PyCon 2022
  * `“Structural Pattern Matching in the Real World” <https://www.youtube.com/watch?v=ZTvwxXL37XI>`_ – A talk by Raymond Hettinger at Pycon Italia 2022
  * ``RegexMatcher` <https://github.com/nedbat/adventofcode2022/blob/main/day07.py>`_: a class integrating pattern matching with Python’s `re` module. A 2022 Advent of Code solution by Ned Batchelder.
  * ``approximately` <https://stackoverflow.com/questions/72596436/how-to-perform-approximate-structural-pattern-matching-for-floats-and-complex>`_: A way to compare `float` and `complex` numbers using pattern matching, while avoiding the `perils of floating-point arithmetic <https://docs.python.org/3/tutorial/floatingpoint.html>`_. A StackOverflow Q&A by Raymond Hettinger.
  * `“A few related schemes for implementing view patterns in Python” <https://gist.github.com/msullivan/7f533f927a4ba3fffd856cb0c9527106>`_: A gist by Michael Sullivan (from February 2023)

