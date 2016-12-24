from datetime import datetime
from celery import Celery


class job3:
    def __init__(self):
        self.celery = Celery()
        self.celery.config_from_object('celerydocker.job3_celeryconfig')

    def do_job3(self, job_id, eta=datetime.now()):

        res = self.celery.send_task(
            'job3.do_job3',
            args=[job_id],
            eta=eta,
            retry_policy={
                'max_retries': 0  # retry forever
            },
            queue='job3'
        )

        return res
