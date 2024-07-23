.. post:: 2024-02-08
   :tags: post, legacy-blogger
   :author: Python Software Foundation
   :category: Legacy
   :location: World
   :language: en

Software Bill-of-Materials documents are now available for CPython
==================================================================

*This was originally posted on blogger* `here <https://pyfound.blogspot.com/2024/02/software-bill-of-materials-now-available-for-cpython.html>`_.

Our Security Developer-in-Residence, `Seth Larson <https://sethmlarson.dev/>`_,
has been working to improve the management of vulnerabilities for Python
users. Seth has championed progress on this goal in a variety of areas:  

  * `Authorizing the Python Software Foundation as a CVE Numbering Authority <https://www.cve.org/Media/News/item/news/2023/08/29/Python-Software-Foundation-Added-as-CNA>`_ (CNA) to publish CVE IDs and records
  * Revitalizing the security advisory mailing list (`security-announce@python.org <https://mail.python.org/mailman3/lists/security-announce.python.org/>`_)
  * Migrating all historical vulnerabilities to the `Open Source Vulnerability format <https://ossf.github.io/osv-schema/>`_ (OSV) and having the records indexed into the `global OSV database <https://osv.dev/list?ecosystem=&q=PSF>`_

With the `release of CPython
3.12.2 <https://www.python.org/downloads/release/python-3122/>`_, the next step
of the Python Software Foundation’s vulnerability management strategy is now
available in the form of Software Bill-of-Materials (SBOM) documents for
CPython source releases. The documents are available for download in their own
column labeled “SBOM” in the “Files” table `on the release
page <https://www.python.org/downloads/release/python-3122/>`_. User
documentation and a getting started guide for CPython SBOMs is `available on
python.org <https://www.python.org/download/sbom/>`_.  
  
These documents are relatively new but have been tested with multiple tools
that accept SPDX SBOM documents. Please report any feedback on the SBOM to the
`CPython issue tracker <https://github.com/python/cpython/>`_.

What is a Software Bill-of-Materials (SBOM)?
--------------------------------------------

Software Bill-of-Materials are machine-readable documents using an ecosystem-
independent format like `SPDX <https://spdx.github.io/spdx-spec/v2.3/>`_ or
`CycloneDX <https://cyclonedx.org/>`_ to describe what a piece of software is
made of and how each component within the software relates to other
components. There are multiple use-cases for SBOMs, but for CPython we
primarily focused on software supply chain and vulnerability management.  
  
Many vulnerability scanning tools support passing an SBOM document as input to
provide a comprehensive scan for software vulnerabilities without needing to
rely on fallible software discovery. This means there’s less chances for
vulnerabilities to be missed by scanners.  
  
There are existing tools for automatically creating SBOMs for software, but
SBOMs which aren’t accurate are sometimes more dangerous than having no SBOM
due to causing a false sense of security. This is especially true for complex
pieces of software or projects which exist outside of package ecosystems, both
of which apply to CPython and make generating an SBOM difficult. For this
reason the content of CPython SBOMs is curated by hand on first pass to ensure
accuracy and completeness and then automated to track updates as the software
changes.  
  
SBOM documents are becoming a requirement for compliance in multiple areas and
industries. In order to meet those requirements we are providing a
comprehensive and accurate SBOM for CPython that will provide assurance for
Python users.

What is included in CPython SBOMs?
----------------------------------

CPython SBOMs use the SPDX SBOM standard. SBOM documents include a description
of the contained software, including all of its dependencies. Information in
CPython SBOMs includes:  

  * Names and versions of all software components
  * Software identifiers (like `CPE <https://nvd.nist.gov/products/cpe>`_ and `Package URLs <https://github.com/package-url/purl-spec>`_)
  * Download URLs for source code with checksums
  * File names and content checksums
  * Dependency relationships between each component

CPython SBOMs satisfy the requirements listed in the `NTIA Minimum Elements
for a Software Bill of
Materials <https://www.ntia.gov/sites/default/files/publications/sbom_minimum_elements_report_0.pdf>`_.
Software identifiers can be used for correlating software in use to
vulnerability databases like the `CVE database <https://www.cve.org/>`_ and
`Open Source Vulnerability database <https://osv.dev/>`_, typically done
automatically using vulnerability scanning tools.  

What _isn’t_ included in CPython SBOMs?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Keep in mind that software libraries that you supply yourself to compile
CPython, such as OpenSSL and zlib, are *not included in the SBOMs for source
artifacts*.  
  
This is due to these libraries not being included in source artifacts, so
CPython users have a choice of which version and sources to use for these
third-party libraries. Folks who are compiling CPython from source are
responsible for tracking their own dependencies either in a separate SBOM
document or by appending new entries to your local CPython SBOM.  
  
CPython’s SBOMs don’t include licensing information for dependencies. See the
CPython licensing page for licensing information.

What is coming next for CPython SBOMs?
--------------------------------------

This is only the beginning for CPython SBOMs, as mentioned above there are
only SBOM documents published for source releases today. The CPython release
managers also publish binary installers for
`Windows <https://www.python.org/downloads/windows/>`_ and
`macOS <https://www.python.org/downloads/macos/>`_ on a variety of distribution
channels. These artifacts will need their own SBOM documents as they are
compiled with software that’s typically not available on those platforms (e.g.
OpenSSL).  
  
There’s also more infrastructure needed to reduce noise and churn for Python
users and Python Security Response Team members alike. Vulnerability EXchange
(VEX) statements are a set of standards which allows software producers to
signal to user tooling whether a piece of software in use is affected by a
vulnerability, even for vulnerabilities affecting dependencies. This is an
area of active development and is being explored alongside the `OpenSSF
Security Tooling Working Group <https://github.com/ossf/wg-security-tooling>`_.  
  
The Security Developer-in-Residence role and this work is funded by a
substantial investment from the OpenSSF `Alpha-Omega
Project <https://openssf.org/community/alpha-omega/>`_. Thanks to Alpha-Omega
for their support in improving the security posture of the entire Python
ecosystem.The OpenSSF is a non-profit cross-industry collaboration that
unifies security initiatives and brings together leaders to improve the
security of open source software by building a broader community, targeted
initiatives, and best practices.  

