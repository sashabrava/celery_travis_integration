from .celery import debug_task
from django.test import TestCase

class CeleryTravisIntegration(TestCase):
    def test_broker(self):
        print ("Starting test_broker")
        task_id = debug_task.delay().task_id
        print ("Waiting result")
        debug_task.AsyncResult(task_id).get(timeout=5)
        print ("Completed")