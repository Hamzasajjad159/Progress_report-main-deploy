import os
import sys
from progress_reporting.wsgi import application

sys.path.insert(0, os.path.dirname(__file__))
print("Asada")
environ = os.environ.setdefault("DJANGO_SETTINGS_MODULE", "progress_reporting.settings")