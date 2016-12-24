from celerydocker.celeryconfig import *  # NOQA

# List of modules to import when celery starts.
CELERY_IMPORTS = ('job2')

CELERY_DEFAULT_QUEUE = 'job2'

CELERY_QUEUES = {
    'job2': {
        'exchage': 'job2',
        'binding_key': 'job2',
        'routing_key': 'job2',
    },
}
