# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#

import os
import sys
import sphinx_rtd_theme
sys.path.append(os.path.abspath("./_ext"))


# -- Project information -----------------------------------------------------

project = 'alyvix_server_doc'
copyright = '2020, Charles Callaway'
author = 'Charles Callaway'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'sphinx.ext.todo',
    'sphinx_copybutton',       # pip install sphinx-copybutton
    'sphinx_rtd_theme',        # pip install sphinx-rtd-theme
    'iconlink'                 # Our custom theme for links with embedded icons at _ext/iconlink.py
]
#    'sphinx.ext.mathjax'
#    'rinoh.frontend.sphinx'  # pip install rinohtype

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Alyvix Server User Manual'
copyright = u'2020, Wuerth Phoenix Srl'
author = u'Charles Callaway'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = u'1.4.3'
# The full version, including alpha/beta/rc tags.
release = u'1.4.3'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', '_ext', 'pictures']

# The name of the Pygments (syntax highlighting) style to use.
# pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# If true, the `numfig` option will produce numbered labels
# Also:  `numfig_format`, `numfig_secnum_depth`
numfig = False
numfig_secnum_depth = 0


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Options for the Read the Docs (rtd) theme.
html_theme_options = {
    'display_version': True,                  # Show the version below the logo
    'prev_next_buttons_location': 'bottom',   # Where to put "Previous" and "Next" buttons
    'style_external_links': False,            # Don't add an icon to distinguish external from internal links
    'sticky_navigation': True,                # Don't scroll the left side of the page
    'includehidden': True                     # Show hidden ToC trees
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = [
    'css/custom.css'
]

# html_js_files = [
#     'js/custom.js',
# ]

html_logo = 'pictures/alyvix_icon_white_100x100.png'
html_favicon = 'pictures/alyvix_icon_100x107.png'

html_output_encoding = 'utf-8'
