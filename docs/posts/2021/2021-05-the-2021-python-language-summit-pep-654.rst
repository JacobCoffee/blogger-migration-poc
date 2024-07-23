.. post:: 2021-05-15
   :tags: post, legacy-blogger
   :author: Python Software Foundation
   :category: Legacy
   :location: World
   :language: en

The 2021 Python Language Summit: PEP 654 — Exception Groups and except*
=======================================================================

*This was originally posted on blogger* `here <https://pyfound.blogspot.com/2021/05/the-2021-python-language-summit-pep-654.html>`_.

`PEP 654 <https://www.python.org/dev/peps/pep-0654/>`_ was authored by Irit
Katriel, Yury Selivanov, and Guido van Rossum. This PEP is currently at the
draft stage. At the `2021 Python Language
Summit <https://pyfound.blogspot.com/2021/05/the-2021-python-language-
summit.html>`_, the authors shared what it is, why we need it, and which ideas
they rejected.

`![Irit Katriel, Yury Selivanov, and Guido van
Rossum <https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhe-_2H9U8orSlDfkOZUfyJt9-KAVscD7j3BTPUjP0UL3EPxi-
ZDQTJ3w8K0mrDvSzrbz6dYYc3zClMCtoYGG8cd0odseIxLltg6WNND-8LPZCRKuMIcCRzp10wpOwM1RVAQpg/w443-h146/talk-2-authors.png>`_](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhe-_2H9U8orSlDfkOZUfyJt9-KAVscD7j3BTPUjP0UL3EPxi-
ZDQTJ3w8K0mrDvSzrbz6dYYc3zClMCtoYGG8cd0odseIxLltg6WNND-8LPZCRKuMIcCRzp10wpOwM1RVAQpg/s1390/talk-2-authors.png)

 What Is PEP 654?  

The purpose of this PEP is to help Python users handle unrelated exceptions.
Right now, if you're dealing with several unrelated exceptions, you can:

  * *Raise one exception* and throw away the others, in which case you're losing exceptions  

  * *Return a list of exceptions* instead of raising them, in which case they become error codes rather than exceptions, so you can't handle them with exception-handling mechanisms
  * *Wrap the list of exceptions in a wrapper exception* and use it as a list of error codes, which still can't be handled with exception-handling mechanisms

PEP 654 proposes:

  * A `built-in exception type <https://www.python.org/dev/peps/pep-0654/#exceptiongroup-and-baseexceptiongroup>`_ that wraps other exceptions
  * New syntax with `except* <https://www.python.org/dev/peps/pep-0654/#except>`_ to handle exception groups

Each except* clause will be executed once, at most. Each leaf exception will
be handled by one except* clause, at most.

In the discussions about the PEP that have happened so far, there were no
major objections to these ideas, but there are still disagreements about how
to represent an exception group. Exception groups can be nested, and each
exception has its own metadata:

`![A nested ExceptionGroup, with
metadata <https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEibghDYoNeptJJ3h8Sp9KG7fZgaNKYuVeagkbkIKfZKjU5yR4saI1w1Fe37qpZJTgqDcHlh4fMvRuav2fCA1p0v-ZUNy-
qiBvNibDXU3G3wZ237OowXFSl8D_zoMIBYQPF3FWo/s16000/nested-
exceptions-500.png>`_](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEibghDYoNeptJJ3h8Sp9KG7fZgaNKYuVeagkbkIKfZKjU5yR4saI1w1Fe37qpZJTgqDcHlh4fMvRuav2fCA1p0v-ZUNy-
qiBvNibDXU3G3wZ237OowXFSl8D_zoMIBYQPF3FWo/s500/nested-exceptions-500.png)

Originally, the authors thought that they could make exception groups
iterable, but that wasn't the best option because metadata has to be
preserved. Their solution was to use a .split() operation to take a condition
on a leaf and copy the metadata:  

`![Splitting exception groups with
.split\(\) <https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi5Uh9SF2iKDnhMIh15b7qGFoUm_RxKYx23RrobVrU6aUa_RJQ-7yw8POAW-
Ca88aHaqx-0E3vRMgMqYWyO4IZK2ZgUZWS1PXSZ_qei_FCAuxF2Ej5FqAgFio-6iW9MetauuMo/s16000/split-500.png>`_](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi5Uh9SF2iKDnhMIh15b7qGFoUm_RxKYx23RrobVrU6aUa_RJQ-7yw8POAW-
Ca88aHaqx-0E3vRMgMqYWyO4IZK2ZgUZWS1PXSZ_qei_FCAuxF2Ej5FqAgFio-6iW9MetauuMo/s500/split-500.png)




Why Do We Need Exception Groups and except*?  
----------------------------------------------

There are some differences between operational errors and control flow errors
that you need to take into account when you're dealing with exceptions:

`![Operational errors vs control flow errors in
Python <https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgTFI4WBJaj-E8knN3T5oFmt1FWIa2qQtqWM5hdc63iamNZ4R0BQsGFTNP7kACUpesOSPXZjdJ1hNt6iAK_W4uDNoCo9C-SxO6vpPf6UXmdE8V_Yo7iTo-g6bTJCZJqX6kG_Gw/s16000/operational-
vs-control-flow-
errors.png>`_](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgTFI4WBJaj-E8knN3T5oFmt1FWIa2qQtqWM5hdc63iamNZ4R0BQsGFTNP7kACUpesOSPXZjdJ1hNt6iAK_W4uDNoCo9C-SxO6vpPf6UXmdE8V_Yo7iTo-g6bTJCZJqX6kG_Gw/s500/operational-
vs-control-flow-errors.png)

In _Example 1_ , there is a clearly defined operation with a straightforward
error. But in _Example 2_ , there are concurrent tasks that could contain any
number of lines of code, so you don't know what caused the KeyError. In this
case, handling one KeyError could potentially be useful for logging, but it
isn't helpful otherwise. But there are other exceptions that it could make
more sense to handle:  

`![asyncio.CancelledError <https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj8w-KAlaGie8YtFlLv4X_UsH0VxZlOQPaxGNiFaQDWXITQRpgWkfQ91TO-
wZ-pQ-
NazFBwl1u9LuG38ELEjoAd8LrdbGtwOYHshgIWZaVD2_1mENqUpaIQbfg_LNXZB1C366s/s16000/CancelledError.png>`_](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj8w-KAlaGie8YtFlLv4X_UsH0VxZlOQPaxGNiFaQDWXITQRpgWkfQ91TO-
wZ-pQ-
NazFBwl1u9LuG38ELEjoAd8LrdbGtwOYHshgIWZaVD2_1mENqUpaIQbfg_LNXZB1C366s/s500/CancelledError.png)

  
It's important to understand the differences between operational errors and
control flow errors, as they relate to try-except statements:

  * *Operational errors* are typically handled right where they happen and work well with try-except statements. 
  * *Control flow errors* are essentially signals, and the current semantics of the try-except statement doesn't handle them adequately.

Before `asyncio <https://docs.python.org/3/library/asyncio.html>`_, it wasn't as
big of a problem that there weren't advanced mechanisms to react to these
kinds of control flow errors, but now it's more important that we have a
better way to deal with these sorts of issues. asyncio.gather() is an unusual
API because it has two entirely different operation modes controlled by one
keyword argument, return_exceptions:

`![asyncio.gather\(\) <https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgTSd_jcdpyJocIN8h7zZzCekM73qD_6PkD21eKNSelK11Os5q-y-k2NcKFSDm3RosinMkl5QX5vnjPV_tgf5d3td_uXMGGd2OkRF6-nEFbJe2xRICAcXlbOzhYJq0ybZtDtvI/s16000/asyncio.gather%2528%2529.png>`_](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgTSd_jcdpyJocIN8h7zZzCekM73qD_6PkD21eKNSelK11Os5q-y-k2NcKFSDm3RosinMkl5QX5vnjPV_tgf5d3td_uXMGGd2OkRF6-nEFbJe2xRICAcXlbOzhYJq0ybZtDtvI/s500/asyncio.gather%2528%2529.png)

  
The problem with this API is that, if an error happens, you still wait for all
of the tasks to complete. In addition, you can't use try-except to handle the
exceptions but instead have to unpack the results of those tasks and manually
check them, which can be cumbersome.

The solution to this problem was to implement another way of controlling
concurrent tasks:

`![asyncio.TaskGroup <https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhm0DIoT7s4hMtOIpl8Gi7Zn5GzNz8IHHZFjKJoucKu386IX7lz41gLBo9YbeKpbUH5T2z3qJzizj4FRxZh9lQ2a9ByU_9J1f8mePVQIUr1tN5aixhjCoLklW2t7oe6PgST5bU/s16000/asyncio.TaskGroup.png>`_](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhm0DIoT7s4hMtOIpl8Gi7Zn5GzNz8IHHZFjKJoucKu386IX7lz41gLBo9YbeKpbUH5T2z3qJzizj4FRxZh9lQ2a9ByU_9J1f8mePVQIUr1tN5aixhjCoLklW2t7oe6PgST5bU/s500/asyncio.TaskGroup.png)

If one tasks fails, then all other tasks will be cancelled. Users of asyncio
have been requesting this kind of solution, but it needed a new way of dealing
with exceptions and was part of the inspiration behind PEP 654.

Which Ideas Were Rejected?
--------------------------

Whether or not exception groups should be iterable is still an open question.
For that to work, tracebacks would need to be concatenated, with shared parts
copied, which isn't very efficient. But iteration isn't usually the right
approach for working with exception groups anyway. A potential compromise
could be to have an iteration utility in traceback.py.

The authors considered teaching except to handle exception groups instead of
adding except*, but there would be too many backwards compatibility problems.
They also thought about using an except* clause on one exception at a time.
Backwards compatibility issues wouldn't apply there, but this would
essentially be iteration, which wouldn't help.  

