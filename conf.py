import datetime
import os
import sys

sys.path.insert(0, os.path.abspath('.'))

from jinja import render_rst_with_jinja

# Default settings
project = 'Time Test'
master_doc = 'index'

# Include all your settings here
html_theme = 'sphinx_rtd_theme'

html_context = {
    'date': repr(datetime.datetime.utcnow())
}


def setup(app):
    app.connect("source-read", render_rst_with_jinja)
