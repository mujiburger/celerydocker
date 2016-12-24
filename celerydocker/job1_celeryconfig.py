from celerydocker.celeryconfig import *  # NOQA

# List of modules to import when celery starts.
CELERY_IMPORTS = ('job1')

CELERY_DEFAULT_QUEUE = 'job1'

CELERY_QUEUES = {
    'job1': {
        'exchage': 'job1',
        'binding_key': 'job1',
        'routing_key': 'job1',
    },
}
