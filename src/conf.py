# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Velour'
copyright = '2025, CouchDB Contributors'
author = 'CouchDB Contributors'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinxext.opengraph",
    "sphinx_inline_tabs",
    "sphinx_copybutton",
    "sphinx.ext.todo",
    "sphinx.ext.extlinks",
    "sphinxcontrib.httpdomain",
    # "configdomain",
    "sphinx.ext.intersphinx",
]

templates_path = ['_templates']
exclude_patterns = []


intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "couchdb": ("https://docs.couchdb.org/en/stable", None),
    "chaise": ("https://chaise.readthedocs.io/en/stable/", None),
}


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']

html_logo = "_static/logo.svg"
html_title = "Velour Specification"

html_theme_options = {
    "source_repository": "https://github.com/AstraLuma/velour",
    "source_branch": "trunk",
    "source_directory": "src/",
}
