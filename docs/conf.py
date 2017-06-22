from __future__ import unicode_literals

import os
import re
import sys

sys.path.append(os.path.abspath('..'))

project = 'django-cabinet'
author = 'Feinheit AG'
copyright = '2017,' + author
version = __import__('cabinet').__version__
release = version
language = 'en'

#######################################
project_slug = re.sub(r'[^a-z]+', '', project)

extensions = []
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'

exclude_patterns = ['build', 'Thumbs.db', '.DS_Store']
pygments_style = 'sphinx'
todo_include_todos = False

html_theme = 'alabaster'
html_static_path = ['_static']
htmlhelp_basename = project_slug + 'doc'

latex_elements = {
    'papersize': 'a4',
}
latex_documents = [(
    master_doc,
    project_slug + '.tex',
    project + ' Documentation',
    author,
    'manual',
)]
man_pages = [(
    master_doc,
    project_slug,
    project + ' Documentation',
    [author],
    1,
)]
texinfo_documents = [(
    master_doc,
    project_slug,
    project + ' Documentation',
    author,
    project_slug,
    '',  # Description
    'Miscellaneous',
)]
