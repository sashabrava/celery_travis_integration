from celery.decorators import task

@task(bind=True)
def debug_task_polls(self):
    return "Debug_task_polls completed"