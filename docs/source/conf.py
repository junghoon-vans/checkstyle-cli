import os
import sys

sys.path.insert(0, os.path.abspath('../../src/'))
import checkstyle  # noqa

# -- Project information -----------------------------------------------------
project = 'checkstyle-cli'
copyright = '2022, junghoon-vans'
author = 'junghoon-vans'
version = checkstyle.__version__
release = f'v{version}'

# -- General configuration ---------------------------------------------------
language = 'en'

templates_path = ['_templates']
exclude_patterns = ['Thumbs.db', '.DS_Store']

pygments_style = 'sphinx'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx_search.extension',
]

source_suffix = '.rst'
master_doc = 'index'

# -- Options for HTML output -------------------------------------------------
html_theme = 'furo'
html_title = f'{project} documentation {release}'

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
