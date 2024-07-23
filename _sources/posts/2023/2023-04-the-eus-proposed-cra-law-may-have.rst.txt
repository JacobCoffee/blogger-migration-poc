.. post:: 2023-04-11
   :tags: post, legacy-blogger
   :author: Python Software Foundation
   :category: Legacy
   :location: World
   :language: en

The EU's Proposed CRA Law May Have Unintended Consequences for the Python Ecosystem
===================================================================================

*This was originally posted on blogger* `here <https://pyfound.blogspot.com/2023/04/the-eus-proposed-cra-law-may-have.html>`_.

After reviewing the proposed `Cyber Resilience Act  <https://digital-
strategy.ec.europa.eu/en/library/cyber-resilience-act>`_and `Product Liability
Act <https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A52022PC0495>`_,
the PSF has found issues that put the mission of our organization and the
health of the open-source software community at risk. While we support the
stated goals of these policies of increasing security and accountability for
European software consumers, we are concerned that overly broad policies will
unintentionally harm the users they are intended to protect. We feel that it
is important to consider the role vendor-neutral nonprofit
organizations—especially public software repositories—play in the modern
development of software.

Many modern software companies rely on open-source software from public
repositories without notifying the author, and certainly without entering into
any kind of commercial or contractual relationship with them. If the proposed
law is enforced as currently written, the authors of open-source components
might bear legal and financial responsibility for the way their components are
applied in someone else’s commercial product. The existing language makes no
differentiation between independent authors who have never been paid for the
supply of software and corporate tech behemoths selling products in exchange
for payments from end-users. We believe that increased liability should be
carefully assigned to the entity that has entered into an agreement with the
consumer. We join our European open source colleagues at the `Eclipse
Foundation <https://eclipse-foundation.blog/2023/02/23/cyber-resilience-act-
good-intentions-and-unintended-consequences/>`_ and `NLnet
Labs <https://blog.nlnetlabs.nl/open-source-software-vs-the-cyber-resilience-
act/>`_ in voicing our concerns over how these policies could affect global open
source projects.  
*  
Why does the Python Software Foundation care about CRA?*  
  
The Python Software Foundation (PSF) is a nonprofit charitable organization
that exists to promote, protect, and advance the Python programming language,`
a cornerstone of the modern technology
sector <https://www.fullstackpython.com/companies-using-python.html>`_. We are
based in the US, but for more than 20 years we have served a global open
source community of students, teachers, entrepreneurs, academics, scientists,
artists, public sector workers, hobbyists and commercial software developers.
The PSF does not sell software, but we provide a public square for developers
to download code and talk about code, and we host components that other
entities may include in their products. We facilitate technical discussions
for the ecosystem generally and support many educational opportunities for the
worldwide community of Python developers.  
  
We do many other things in the service of `our charitable
mission <https://www.python.org/psf/mission/>`_, but there are two activities
that could be affected by the CRA:  
  

1) We host and provide the core Python programming language, standard library
and interpreter to any who wish to use it free of charge. It may be downloaded
from our website, and a version of Python is downloaded over 300 million times
per day.  
  
2) We host the Python Packaging Index (PyPI), a vast library of software
packages, written by thousands of different entities and individuals, that is
made available in a single place where all packages are public and freely
available. PyPI is critical infrastructure for the entire ecosystem, and
thousands of individuals and enterprises depend on it, downloading 10 billion
packages in an average month.  

  
To be absolutely clear, nobody pays us for software, either for the core
language or any of the packages that you can download from the repository we
maintain. At first glance, that might lead one to believe that there is no
money being made with Python or Python packages. In fact the reverse is true:
a large number of people who build things with Python, analyze data with
Python or create AI models with Python are doing so at a commercial company,
academic institution or government agency that pays them to work there, and in
fact a not-insignificant share of the profit-generating tech economy relies in
some part on Python. For instance, many well known applications including
YouTube, Instagram and Spotify are all built using Python code.  
  
*Hosting Python and Third-party Python Software in the Open is a Public
Good*  
  
We host a lot of software that is used in commercial applications and nearly
everyone—except the PSF itself—is making a lot of money selling products that
use Python code and libraries. We host that software so that it can be
examined by anyone for flaws or bugs. We also host that software so that it
can be used to teach new coders and the next generation of tech pioneers. Any
policy that does not provide clear carve outs for repositories offered for the
public good will do irreparable harm to the individual’s accessibility to the
power of modern software development.  
  
We’re concerned that some of the current proposed policy language doesn’t make
things clear enough for an ecosystem like Python’s. Under the current
language, the PSF could potentially be financially liable for any product that
includes Python code, while never having received any monetary gain from any
of these products. The risk of huge potential costs would make it impossible
in practice for us to continue to provide Python and PyPI to the European
public. Certainly, everyone wants security, for consumers to have reasonable
assurances, and for the software industry to be accountable to its customers.
However, it is critical that those assurances are expected from the correct
entity and that the legal burden for any lapse in accountability is levied
against the correct entity. Many of the software elements that end up in
commercial software or hardware products come from publicly available open
source repositories like PyPI where no compensation is given. Open source
languages and repositories shouldn’t be thanked for the public services they
freely provide with an open-ended risk of ruinously costly legal action. The
PSF should not be liable for every application or device that happens to
contain some Python code.  
  
Assigning liability to every upstream developer would create less security,
not more. Leaving individual and/or under-resourced developers in a legally
murky position when contributing to public repositories like the Python
Package Index would almost certainly create a chilling effect for them. Only
entities who are selling enough software or software/hardware combinations to
absorb the ramifications of product liability could continue to operate in the
open. The user improvements and shared security benefits of global software
collaboration would only be accessible to those developers working on behalf
of a few large companies. Growth and innovation would be stifled. The security
of languages like Python depends on the continued availability of a neutral,
non-commercial entity that can act as a clearinghouse for new software,
improvements, and bug fixes that can be shared freely by the entire software
community.  
  
*Increased Clarity is Needed*  
  
Rather than following the code all the way upstream, we would prefer to see
policy makers follow the money. Many components are not a product by
themselves and it is a mistake to risk any shift of financial burden from the
entity that compiles and sells a product to the open source developer that
they received a free bit of code from. All coders should be working towards a
world of greater security for end-users, but no one developer can imagine all
the ways in which an individual open source component will be used and
combined with other components for consumer use. Consumer liability and
responsibility cannot be assigned until a product is assembled and something
is for sale.  
  
In particular, we believe that there are two phrases in the CRA that cast too
wide of a net. In Article 16, “A natural or legal person, other than the
manufacturer, the importer or the distributor, that carries out a substantial
modification of the product with digital elements shall be considered a
manufacturer for the purposes of this Regulation.” is too broad. Open source
is full of people who make a substantial modification to a piece of public
code but do not have any contractual or financial relationship with the entity
or entities that might eventually use that code in a commercial product.
Secondly, in Recital 10, the phrase “…by providing a software platform through
which the manufacturer monetises other services.” is not specific enough.
Public code repositories and their hosts may offer paid classes or sell
tickets to conferences about shared open source code while still having no
control over the way commercial entities use that code in their products.
Disincentivizing educational activities or curtailing public patches from
third parties will not make European software consumers safer.  
  
The existing, publicly available open source ecosystem already provides robust
and evolving security mechanisms where we share news about where individual
components should be used and more importantly how they shouldn’t be used.
When a flaw is discovered in a popular piece of software, we publicize patches
and get potential vulnerabilities addressed across hundreds of products and
tools. Chilling participation in these processes makes us more vulnerable, not
less.*  
*

*Conclusion*  
  
We need it to be crystal clear who is on the hook for both the assurances and
the accountability that software consumers deserve. Language that specifically
exempts public software repositories that are offered as a public good for the
purpose of facilitating collaboration would make things much clearer. We'd
also like to see our community, especially the hobbyists, individuals and
other under-resourced entities who host packages on free public repositories
like PyPI be exempt. We believe these exemptions would help both consumers and
the open source ecosystem, as well as the economic actors who depend on it. We
hope that policy makers in the European Union will carefully consider complex
and vital ecosystems like Python when drafting landmark policies that affect
open-source software development.  
  
PSF members and Python users in Europe may wish to `write to their
MEP <https://www.europarl.europa.eu/meps/en/home>`_ voicing their concerns about
the proposed CRA law before April 26th, while amendments that will protect
public open source repositories are still being considered.

