import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "notes.settings")

app = Celery("notes")
app.config_from_object("django.conf:settings", namespace="CELERY")
