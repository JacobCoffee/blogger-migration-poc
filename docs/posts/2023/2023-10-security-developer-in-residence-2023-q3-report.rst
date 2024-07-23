.. post:: 2023-10-17
   :tags: post, legacy-blogger
   :author: Python Software Foundation
   :category: Legacy
   :location: World
   :language: en

Security Developer-in-Residence 2023 Q3 Report
==============================================

*This was originally posted on blogger* `here <https://pyfound.blogspot.com/2023/10/security-developer-in-residence-2023-q3-report.html>`_.

It’s been three months since I was first hired as the inaugural Security
Developer-in-Residence. I’m quite proud of what I’ve accomplished so far and
think it shows the value of investing into the security of Open Source through
hiring folks to work full-time in roles like “Developer-in-Residence”
programs. I’m thankful to the `Alpha-Omega project at OpenSSF <https://alpha-
omega.dev/>`_ for funding this work. Let’s review all of the accomplishments in
the first quarter of this role and what to look forward to in the next
quarter.  
  
If you’d like to follow along with my work more closely you can subscribe to
my `personal blog <https://sethmlarson.dev/blog#archive>`_ where I publish
`weekly updates <https://sethmlarson.dev/security-developer-in-residence-
weekly-report-13>`_ about the work I’m doing. If you have questions or thoughts
about what I’m working on you can contact me via email:
`seth@python.org <mailto:seth@python.org>`_.  

The Python Software Foundation authorized as a CVE Numbering Authority
----------------------------------------------------------------------
(CNA)

Back in late August the Python Software Foundation received notice that we’d
successfully completed onboarding and had been `authorized by CVE as a CVE
Numbering Authority <https://pyfound.blogspot.com/2023/08/psf-authorized-as-
cna.html>`_ or “CNA”. The `Python Software Foundation CNA
scope <https://www.cve.org/PartnerInformation/ListofPartners/partner/PSF>`_
covers Python and pip, two projects which are fundamental to the rest of the
Python ecosystem.  
  
Being a CNA means that the PSF can offer staffing to improve the
sustainability and responsiveness of coordination and vulnerability disclosure
work for covered projects. The PSF CNA also provides `rich metadata for CVE
records and advisories <https://osv.dev/vulnerability/PSF-2023-8>`_, including
remediation information, so upgrading or patching for vulnerabilities is as
straightforward as possible for downstream users of Python.  
  

CPython vulnerability advisories available in Open Source Vulnerability
-----------------------------------------------------------------------
database

The Python Software Foundation now hosts a `vulnerability database on
GitHub <https://github.com/psf/advisory-database>`_ using the `Open Source
Vulnerability format <https://ossf.github.io/osv-schema/>`_ (OSV). This database
contains vulnerability information for CPython in addition to vulnerabilities
getting published to the security-announce@python.org mailing list. The
historical vulnerability information was sourced from Victor Stinner’s
“`python-security <https://python-security.readthedocs.io/>`_” project in order
to provide a complete history of vulnerabilities in CPython.  
  
By using the OSV format the vulnerabilities can be ingested and processed by
the Open Source Vulnerability database which can be searched or `queried using
an API <https://google.github.io/osv.dev/api/>`_ for machine-consumable
vulnerability information.  
  
Having vulnerability information in a machine-consumable format enables tools
that scan software deployments for vulnerabilities to easily provide accurate
and automatically updated reports for CPython. The Open Source Vulnerability
database also is more discoverable compared to the CVE database, having a
readily available public API to query for vulnerabilities, products, and
versions.  
  

Python Security Response Team
-----------------------------

I have been helping coordinate reports to the `Python Security Response
Team <https://www.python.org/dev/security/>`_ (PSRT) since joining the role.
This work includes reviewing all reports, gathering information from
reporters, discussing timelines, and working with core developers to create
and release fixes and advisories in a coordinated manner. I also worked with
CVE to get CVE IDs assigned on behalf of reports before the PSF was designated
as a CNA.  
  
I revitalized the `security-announce@python.org mailing
list <https://mail.python.org/mailman3/lists/security-announce.python.org/>`_ to
use for future advisory announcements so interested parties can be notified as
soon as new vulnerabilities are published (subscribe to the linked list if
you’d like to receive these). I coordinated the two recent vulnerabilities
affecting CPython (`CVE-2023-40217 <https://osv.dev/vulnerability/PSF-2023-8>`_
and `CVE-2023-41105 <https://osv.dev/vulnerability/PSF-2023-9>`_) end-to-end
from report to published advisory.  
  
Doing this coordination work frees up volunteers on the PSRT to focus on
determining whether a report is a vulnerability and working on fixes. I’m also
working to further reduce the manual coordination work required by PSRT by
moving the reporting and triage process to GitHub using GitHub Security
Advisories.

OpenSSF Day Europe 2023
-----------------------

I co-presented a talk titled “`We Make Python Safer than
Ever <https://sched.co/1P6TW>`_” at OpenSSF Day Europe 2023 with PSF Board
Member and OpenSSF Community Manager Cheuk Ting-Ho. The `slides are available
for
download <https://static.sched.com/hosted_files/openssfdayeu2023/a3/Final%20-%20OpenSSF%20Day%20Europe%202023.pdf>`_
and the `talk recording is available to watch on
YouTube <https://www.youtube.com/watch?v=jhzv5RU56V4>`_.  
  
The talk introduced the Security Developer-in-Residence role, went over the
challenges that are unique to securing Open Source and Python ecosystems,
described completed and future projects to make the Python ecosystem more
secure, and gave a list of items that viewers themselves could do right away
to make their own usage of Python more secure.  
  

Sigstore signatures for Python release artifacts
------------------------------------------------

Python releases include signatures from the Release Managers using the signing
tool “`Sigstore <https://www.sigstore.dev/>`_”. These signatures mean you can be
sure that a given release artifact wasn’t tampered with and was created and
vetted by the Release Manager for a given Python release.  
  
I did an audit of existing signatures and `found some
discrepancies <https://github.com/sigstore/sigstore-
python/issues/600#issuecomment-1634961707>`_ between the documented identities
and providers and what was published for each release. I worked with Release
Managers to fix the discrepancies and `added extra
safeguards <https://github.com/python/release-tools/pull/51>`_ to release
tooling to ensure signatures are verifiable as documented. I also was able to
back-fill the `new Sigstore signature
format <https://github.com/python/pythondotorg/issues/2300>`_ from existing
verification materials to make verifying signatures even easier!

> $ python -m sigstore verify identity \  
>     \--bundle Python-3.12.0.tgz.sigstore \  
>     \--cert-identity thomas@python.org \  
>     \--cert-oidc-issuer https://accounts.google.com \  
>     Python-3.12.0.tgz

Having consistent artifact signatures is important because any discrepancies
while consuming these signatures should raise red flags for downstream users
and redistributors. This also helps build confidence in the new signing method
over existing methods like GPG.  
  

Adoption of system trust stores via Truststore
----------------------------------------------

There are three packaging tools (pip, PDM, and Conda) that are important to
the Python ecosystem that are at various stages of adopting “Truststore”, a
library that I authored prior to joining the PSF to enable Python projects to
use system trust stores for verifying HTTPS certificates instead of relying on
certifi for certificates.  
  
PDM has started using Truststore by default starting in
`v2.9.0 <https://github.com/pdm-project/pdm/releases/tag/2.9.0>`_, Conda plans
to release `optional support for Truststore in
v23.9.0 <https://github.com/conda/conda/milestone/63>`_, and pip already has
`optional support for Truststore <https://pip.pypa.io/en/stable/topics/https-
certificates/#using-system-certificate-stores>`_ since v22.2 but has recently
bundled Truststore into pip to remove the need to “bootstrap” into Truststore
by pre-installing the library.  
  
Using the system trust store is important because any removals to a trust
store (`like for e-Tugra root
certificates <https://osv.dev/vulnerability/PYSEC-2023-135>`_) must be
propagated to all end systems in order to avoid “monster-in-the-middle”
attacks. Further challenging this propagation is that some tools like pip
bundle certifi as a means of bootstrapping, which means that you need to
upgrade both certifi and pip in order to completely propagate updates to
certifi’s certificate bundle.  
  
This propagation is better suited to a centralized system like an OS package
manager or an automatic centralized authority or IT department keeping the
trust bundles up-to-date, which can only happen through using system trust
stores.  
  
Recently the Python implementation PyPy added support for Python 3.10, thus
enabling PyPy to also use Truststore. I `subsequently added support and
backwards compatibility tests for PyPy to
Truststore <https://github.com/sethmlarson/truststore/pull/113>`_ to ensure all
compliant implementations of Python can take advantage of the benefits.

Future Projects and Challenges  
--------------------------------
  

Software Bills-of-Materials for CPython
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Software Bill-of-Materials (SBOMs) are a hot topic in the world of software
security due to new government requirements and improved software and
vulnerability management tooling. Many tools generate or consume SBOMs as a
universal format for describing software and its components and then matching
those components to known vulnerabilities.  
  
I've started working on an authoritative SBOM for the CPython project, you can
follow along in `this GitHub
repository <https://github.com/sethmlarson/cpython-sbom>`_ if you are
interested. This project is early and this will not be the final product or
place where this information is published, this is only a place to experiment
and get feedback on the approach and outputs before putting the final
infrastructure in place.  
  
I started with the most straightforward release artifact, the source tarball,
and I am planning to tackle the binary installers later since they'll require
more research into the release processes. There is a work-in-progress SBOM
file for Python-3.12.0.tgz available in the `sboms/ directory on the
repository <https://github.com/sethmlarson/cpython-sbom/blob/main/sboms>`_.  
  
Using vulnerability scanning tools I was able to see not only vulnerabilities
in CPython, but *crucially in the bundled subcomponents like expat and pip*.
Without an SBOM the subcomponents to a project like CPython likely wouldn’t
get detected properly and thus would be not covered by vulnerability
management tooling.  
  
The challenges here will be integrating the creation and maintenance of the
SBOMs into the CPython development and release processes while minimally
disrupting other core developers workflows and avoiding the need to develop
and maintain custom tooling for CPython’s specific use-case.  
  

Tracking bundled dependencies in Python packages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Python is the premier “glue” language, meaning that Python is often used
alongside many other programming languages like C, C++, Rust, Go, and more
thanks to Python C API. This benefit also means that Python packages can
include projects and source code from sources both within and external to the
Python ecosystem.  
  
Those projects and source code from outside the Python ecosystem present a
problem for vulnerability scanners *which typically rely on explicit metadata
about projects and dependencies in order to find vulnerabilities in software
manifests*. Without a clear way to encode this information into packaging
metadata it’s impossible to signal these dependencies even if a maintainer of
a project wants to do so.  
  
C and C++ projects in particular pose additional issues due to their existence
outside of a programming language packaging ecosystem like Python with PyPI or
JavaScript and NPM. This makes tracking usage and vulnerabilities in these
projects difficult and relies on other identification schemes like CPEs or
redistributions in other packaging ecosystems like RPM/DEB. Without this
information scanners today miss vulnerable components bundled in Python
packages, meaning developers won’t know how or when their Python deployments
are vulnerable.  
  
Solving this issue completely will be a multi-step process, starting with
being able to encode information about bundled projects into Python
distributions which will require a new packaging PEP. After the standard has
been decided, next is getting bundled project metadata automatically captured
to avoid needing an entire ecosystem to manually annotate every project.
Concurrently to this I’ll collaborate with SBOM generation tooling to add
support for consuming the new standard and adding that information to SBOMs
generated from Python environments.  
  

CPython and pip release process improvements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

CPython and pip are two of the most important projects in the Python ecosystem
and each have non-trivial release processes. In an effort to increase the
integrity of these projects’ releases I’ve `researched and documented their
release process <https://sethmlarson.dev/security-developer-in-residence-
weekly-report-9>`_ and with `SLSA’s list of historical supply chain attacks
against software projects <https://slsa.dev/spec/v1.0/threats-overview>`_ have
been making suggestions and implementing improvements.  
  
These improvements include reproducibility of built artifacts, extra
guarantees on the integrity of inputs, automating the build processes to
reduce attack surface area to only services like GitHub Actions and Azure
Pipelines instead of individuals’ computers, and making it so that in the
event of an attack that it would need to be publicly detectable and traceable.  
  
By improving the integrity of these processes I am hoping to prevent disaster
scenarios such as malware being injected into Python or pip at the “last mile”
before being published to python.org. *Injection of malware during build time
has happened to multiple other Open Source projects with disastrous results
for users*. This work means users can be even more confident in their usage
of Python and upgrade early and often to take advantage of Python’s latest
features.

