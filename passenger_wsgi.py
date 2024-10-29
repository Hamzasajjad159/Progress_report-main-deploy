import os
import sys
from progress_reporting.progress_reporting.wsgi import application

sys.path.insert(0, os.path.dirname(__file__))

environ = os.environ.setdefault("DJANGO_SETTINGS_MODULE", "progress_reporting.settings")