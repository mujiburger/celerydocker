from __future__ import absolute_import

from celery import Celery

job2Queue = Celery('job2Queue')
job2Queue.config_from_object('celeryconfig')

if __name__ == '__main__':
    job2Queue.start()
