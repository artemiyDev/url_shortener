from pathlib import Path
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

ROOT_URLCONF = "app.urls"

WSGI_APPLICATION = "app.wsgi.application"
