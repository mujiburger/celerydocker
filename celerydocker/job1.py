from datetime import datetime
from celery import Celery


class job1:
    def __init__(self):
        self.celery = Celery()
        self.celery.config_from_object('celerydocker.job1_celeryconfig')

    def do_job1(self, job_id, eta=datetime.now()):

        res = self.celery.send_task(
            'job1.do_job1',
            args=[job_id],
            eta=eta,
            retry_policy={
                'max_retries': 0  # retry forever
            },
            queue='job1'
        )

        return res
