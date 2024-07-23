.. post:: 2018-05-09
   :tags: post, pycon2018, microsoft, legacy-blogger
   :author: Python Software Foundation
   :category: Legacy
   :location: World
   :language: en

Updates from Microsoft, PyCon 2018 Keystone Sponsor
===================================================

*This was originally posted on blogger* `here <https://pyfound.blogspot.com/2018/05/updates-from-microsoft-pycon-2018.html>`_.

  

_Microsoft has been a big supporter of the Python language through sponsored
development of Python Tools for Visual Studio, Jupyter, CPython, Azure Machine
Learning and organizations such as the PSF and NumFocus. This year the PSF is
proud to have Microsoft as our Keystone Sponsor for PyCon 2018 in Cleveland.
We also spoke with them to find out more about their recent efforts in the
Python community, and here’s what they had to share:_

  

  

*_Q: The Microsoft Python extension for Visual Studio code is now available.
We’d be interested in hearing about some of the linting improvements that were
made in this release._*

  

*Microsoft:* That's right, we are excited about the Microsoft Python
extension! The extension was originally developed by `Don
Jayamanne <https://twitter.com/donjayamanne>`_ who has now joined Microsoft, and
we started publishing the extension as Microsoft in November of 2017. We
`release a new version <https://github.com/Microsoft/vscode-
python/blob/master/CHANGELOG.md>`_ every month, and it is currently the most
popular extension for `VS Code <https://code.visualstudio.com/>`_. We have been
focused on improving the core Python development experience: linting,
IntelliSense, debugging, and support for various environments (virtualenv,
pipenv, pyenv, conda). Linting specifically is important to Python developers,
with Python being a dynamic language we often depend on linters to give
feedback to catch coding errors without having to hit them later at runtime.
PyLint is enabled by default in the extension because it has a comprehensive
set of rules, and we also support many linters used by Python developers:
flake8, mypy, pydocstyle, pep8, prospector and pylama.

  

One of the improvements we made early was to define a default set of linting
rules that help developers catch errors, without the distraction of too many
optional warnings about coding convention. Developers can enable the coding
convention rules or otherwise customize rulesets to match their development
style by `adding a .pylintrc file to their
workplace <https://code.visualstudio.com/docs/python/linting#_pylint>`_. We are
continuing to make linting improvements in the coming months.

  

`Get the Python extension for VS Code and join the conversation
here. <https://aka.ms/l699u2>`_

  

  

*_Q: Microsoft is known for being highly invested in security. What can you
tell us about adding security enhancements to Python, similar to those already
in PowerShell?_*

  

*Microsoft:* We have an incredibly strong security culture at Microsoft with
experts on everything from cloud and operating systems to CPU vulnerabilities.
As we saw Python usage increasing, we had some of our scripting language
specialists investigate how system administrators could integrate Python into
their existing security auditing and management systems, much like we enabled
for PowerShell in recent releases. One result of this is `PEP
551 <https://www.python.org/dev/peps/pep-0551/>`_, and while that proposal is
yet to be accepted, we are maintaining source implementations against the
latest `Python 3.6 <https://github.com/zooba/cpython/tree/pep551_36>`_ and
`3.7 <https://github.com/zooba/cpython/tree/pep551>`_ releases. For a good
overview of why we believe these security transparency features are valuable
for Python, see `this presentation <http://youtu.be/K7qUVyeh10U>`_ by Steve
Dower, one of our engineers and CPython contributors.

  

  

*_Q: How does the Microsoft Software Donation Program at TechSoup work?_*

  

*Microsoft:* TechSoup and its international network of 65 other partner
organizations help Microsoft in facilitating software donations for
nonprofits, charities, and NGOs in 236 countries and territories. This
includes quickly and reliably verifying an organization's nonprofit status.
Serving as a dynamic bridge between civil society and corporate donor partners
like Microsoft, TechSoup provides transformative technology products,
knowledge, and services that enable people to work together toward a more
equitable world. `To find out more, please visit their site
here. <https://www.techsoup.org/>`_

  

  

*_Q: What does the future of Python look like from Microsoft’s vantage point?
What sorts of things do you see for the community as a whole as well as Python
within Microsoft itself?_*

  

*Microsoft:* The future is bright for Python with its broad applicability
and low bar to entry. Microsoft will continue to invest in Python tooling
(through `Visual Studio <https://aka.ms/python>`_ and our free, open source and
cross-platform Visual Studio Code), in better support for Python running on
the Microsoft platforms, e.g. on Windows and on
`Azure <https://azure.microsoft.com/en-us/develop/python/>`_ (whether on Linux
or Windows VMs), and of course Microsoft will continue to contribute to the
Python community. Whether someone is using Python for scripting scenarios and
automating tasks, or for web and backend development, or for Data Science and
machine learning, Microsoft’s goal is to help them be successful. The real
question isn’t what Microsoft thinks of the future of Python, but what the
Python community sees as the future and how can Microsoft help towards that
future.

  

  

*_Q: We’re thrilled that Microsoft has stepped forward to make such a big
investment in PyCon and its community. What would you like attendees to take
away from your presence at PyCon?_*

  

*Microsoft:* Microsoft loves Python and we are committed to be a supportive
and productive member of the community. We employ more active Python Core
developers than any other company, and they contribute to both Python itself
as well as Microsoft's products for our Python customers. Plus, we are hiring
more! If you are interested in working on our hosted Jupyter notebooks
service, check out the `job
description <https://careers.microsoft.com/us/en/job/402347/SR-SOFTWARE-
ENGINEER>`_ and send your resume to
`PythonJobs@microsoft.com <mailto:PythonJobs@microsoft.com>`_. There has been
support for Python in the flagship Visual Studio product for some time now,
and recently we added Python support in Visual Studio Code, our free, open
source, and lightweight editor for macOS, Linux and Windows. We continue to
improve and deepen support for Python in our Azure cloud and we are proud to
say that you can already use our cloud infrastructure and services to build
great apps in any language for any platform. Most of all, we would love to
hear your feedback – what else can we do for the Python community? We are
listening!

  

  

_Again, a big thanks to Microsoft for their continued support in the Python
community and Pycons specifically. Be sure to look for their booths and
workshops if you are at PyCon this year._

  

_Additionally, if you are interested in being a sponsor for PyCon in the
future, please contact_` _pycon-sponsors@python.org_ <mailto:pycon-
sponsors@python.org>`_ _for more information. Depending on your level of
sponsorship, packages include complimentary conference passes, booth space,
lead retrieval scanners, speaking opportunities, and a table in the Job Fair._

  

