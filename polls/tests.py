from django.test import TestCase
from .tasks import debug_task_polls

class PollsPageTests(TestCase):
    def test_async_polls(self):
        print ("Starting test_async_polls")
        task_id = debug_task_polls.delay().task_id
        print ("Waiting result")
        debug_task_polls.AsyncResult(task_id).get(timeout=5)
        print ("Completed")