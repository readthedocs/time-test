import datetime

# Default settings
project = 'Time Test'
master_doc = 'index'

# Include all your settings here
html_theme = 'sphinx_rtd_theme'

html_context = {
   'date': datetime.datetime.utcnow()
}
