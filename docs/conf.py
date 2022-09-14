# Configuration file for the Sphinx documentation builder.

project = 'checkstyle-cli'
copyright = '2022, junghoon-vans'
author = 'junghoon-vans'

# -- General configuration ---------------------------------------------------

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
extensions = ['sphinx.ext.autodoc']

# -- Options for HTML output -------------------------------------------------

html_theme = 'furo'
html_static_path = ['_static']
