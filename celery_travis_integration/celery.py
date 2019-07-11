from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.decorators import task

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_travis_integration.settings')
app = Celery('celery_travis_integration')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

@task(bind=True)
def debug_task(self):
    return "Debug_task completed"