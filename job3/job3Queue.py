from __future__ import absolute_import

from celery import Celery

job3Queue = Celery('job3Queue')
job3Queue.config_from_object('celerydocker.job3_celeryconfig')

if __name__ == '__main__':
    job3Queue.start()
