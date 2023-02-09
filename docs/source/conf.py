# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Foxus'
copyright = '2023, Foxus.com'
author = 'Zelle Marcovicci'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
html_logo = 'foxus-logo-favicon.webp'
html_favicon = 'foxus-logo-favicon.webp'

html_theme_options = {
    'display_version': False,
    'style_nav_header_background': 'rgba(0,0,0,.05)'
}

# -- Options for EPUB output
epub_show_urls = 'footnote'
