from __future__ import absolute_import

from celery import Celery

job1Queue = Celery('job1Queue')
job1Queue.config_from_object('celeryconfig')

if __name__ == '__main__':
    job1Queue.start()
