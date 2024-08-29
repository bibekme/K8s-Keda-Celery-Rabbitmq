from celery import shared_task
from time import sleep


@shared_task(bind=True, ignore_result=True)
def debug_task(self):
    sleep(20)
    print(f"Request: {self.request!r}")
