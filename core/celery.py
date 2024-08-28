import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

app = Celery("core")

app.config_from_object("django.conf:settings", namespace="CELERY")
app.conf.broker_url = os.environ.get("CELERY_BROKER_URL")
app.autodiscover_tasks()
