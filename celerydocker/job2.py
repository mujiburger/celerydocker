from datetime import datetime
from celery import Celery


class job2:
    def __init__(self):
        self.celery = Celery()
        self.celery.config_from_object('celerydocker.job2_celeryconfig')

    def do_job2(self, job_id, work, eta=datetime.now()):

        res = self.celery.send_task(
            'job2.do_job2',
            args=[job_id, work],
            eta=eta,
            retry_policy={
                'max_retries': 0  # retry forever
            },
            queue='job2'
        )

        return res
