"""Sphinx configuration."""

from __future__ import annotations

from datetime import datetime

current_year = datetime.now().year

# -- Project information -----------------------------------------------------
project = "Python Blog"
copyright = f"{current_year}, Python Software Foundation"
author = "Python Software Foundation"

# -- General configuration ---------------------------------------------------
extensions = [
    "sphinx.ext.intersphinx",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_copybutton",
    "sphinx_toolbox.collapse",
    "sphinx_design",
    "ablog",
]

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}

napoleon_google_docstring = True
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = True
napoleon_use_admonition_for_notes = True
napoleon_use_admonition_for_references = False
napoleon_attr_annotations = True

autoclass_content = "both"
autodoc_default_options = {
    "members": True,
    "member-order": "bysource",
    "special-members": "__init__",
    "exclude-members": "__weakref__",
    "show-inheritance": True,
    "class-signature": "separated",
    "typehints-format": "short",
}

nitpicky = False  # This is too much of a headache right now
nitpick_ignore = []
nitpick_ignore_regex = []

autosectionlabel_prefix_document = True
suppress_warnings = [
    "autosectionlabel.*",
    "ref.python",  # TODO: remove when https://github.com/sphinx-doc/sphinx/issues/4961 is fixed
]
todo_include_todos = True

# -- Style configuration -----------------------------------------------------
html_theme = "shibuya"
html_static_path = ["_static"]
html_show_sourcelink = True
html_title = "Python Blog"
html_favicon = "_static/badge.svg"
html_logo = "_static/badge.svg"
html_sidebars = {
   '**': [...,
          'ablog/postcard.html', 'ablog/recentposts.html',
          'ablog/tagcloud.html', 'ablog/categories.html',
          'ablog/archives.html', ]
}
html_context = {
    "source_type": "github",
    "source_user": "JacobCoffee",
    "source_repo": "blogger-migration-poc",
}

html_theme_options = {
    "logo_target": "/",
    "page_layout": "default",
    "navigation_with_keys": True,
    "accent_color": "indigo",
    "nav_links": [
        {"title": "Home", "url": "index"},
        {
            "title": "Community",
            "children": [
                {
                    "title": "Contributing",
                    "summary": "Learn how to contribute to the Python project",
                    "url": "https://www.python.org/dev/",
                },
                {
                    "title": "Code of Conduct",
                    "summary": "Review the etiquette for interacting with the Python community",
                    "url": "https://policies.python.org/python.org/code-of-conduct/",
                },
                {
                    "title": "Security",
                    "summary": "Overview of PSFs's security protocols",
                    "url": "https://www.python.org/dev/security/",
                },
            ],
        },
        {
            "title": "About",
            "children": [
                {
                    "title": "Python Software Foundation",
                    "summary": "Details about the PSF",
                    "url": "https://www.python.org/psf-landing/",
                },
                {
                    "title": "Releases",
                    "summary": "Explore the latest Python releases",
                    "url": "https://www.python.org/downloads/",
                },
            ],
        },
        {
            "title": "Help",
            "children": [
                {
                    "title": "Discord Help Forum",
                    "summary": "Dedicated Discord help forum",
                    "url": "https://discord.gg/python",
                },
                {
                    "title": "Board Discussions",
                    "summary": "Board Discussions",
                    "url": "https://discuss.python.org/",
                },
            ],
        },
        {"title": "Sponsor", "url": "https://github.com/sponsors/python"},
    ],
}

# -- Ablog Config
blog_title = "Python Blog"
blog_authors = {
    'Python Software Foundation': ('PSF', 'https://python.org/psf')
}
blog_default_author = 'Python Software Foundation'
# blog_post_pattern = ["posts/**/*.rst", "posts/**/*.md"]
