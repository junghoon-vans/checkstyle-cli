# -- Project information -----------------------------------------------------
project = 'checkstyle-cli'
copyright = '2022, junghoon-vans'
author = 'junghoon-vans'

# -- General configuration ---------------------------------------------------
extensions = ['sphinx.ext.autodoc']

templates_path = ['_templates']
exclude_patterns = ['Thumbs.db', '.DS_Store']

language = 'en'

# -- Options for HTML output -------------------------------------------------
html_theme = 'furo'
html_static_path = ['_static']
