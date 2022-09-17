import os
import sys
sys.path.insert(0, os.path.abspath('../../src/'))

# -- Project information -----------------------------------------------------
project = 'checkstyle-cli'
copyright = '2022, junghoon-vans'
author = 'junghoon-vans'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
]

source_suffix = '.rst'
master_doc = 'index'
pygments_style = 'sphinx'

templates_path = ['_templates']
exclude_patterns = ['Thumbs.db', '.DS_Store']

language = 'en'

# -- Options for HTML output -------------------------------------------------
html_theme = 'furo'

# -- Autodoc configuration ---------------------------------------------------
autodoc_member_order = 'bysource'
autoclass_content = "both"
autosummary_generate = True

autodoc_default_options = {
    'members': True,
    'show-inheritance': True,
    'inherited-members': True,
    'no-special-members': True,
}

napoleon_google_docstring = True
