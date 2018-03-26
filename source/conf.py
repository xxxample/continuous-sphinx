# -*- coding: utf-8 -*-
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present. All configuration
# values have a default.

import sys
import os
import shlex
import sphinx_rtd_theme

# Redefine supported_image_types for the HTML builder
from sphinx.builders.html import StandaloneHTMLBuilder
StandaloneHTMLBuilder.supported_image_types = [
    'image/gif',
    'image/png',
    'image/jpeg',
    'image/svg+xml',
]

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath('.'))

# -- General configuration ------------------------------------------------

#site base url
site_url = 'https://continuous-sphinx.netlify.com/'


# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx_sitemap']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'Continuous Sphinx'
copyright = '2018, jdillard'
author = 'jdillard'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '1.0.0'
# The full version, including alpha/beta/rc tags.
release = '1.0.0'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = '_static/favicon.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = ''

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = True

# reST sources are included in the HTML build as _sources
html_copy_source = False

# -- Options for HTMLHelp output ---------------------------------------------

# Language to be used for generating the HTML full-text search index.
# Output file base name for HTML help builder.
htmlhelp_basename = 'ContinuousSphinxDoc'

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',

# Latex figure (float) alignment
#'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
  (master_doc, 'ContinuousSphinx.tex', 'Continuous Sphinx Documentation',
   'jdillard', 'manual'),
]
