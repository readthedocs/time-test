import datetime

# Default settings
project = 'Time Test'

# Include all your settings here
html_theme = 'sphinx_rtd_theme'

html_context = {
   'date': datetime.datetime.utcnow()
}
