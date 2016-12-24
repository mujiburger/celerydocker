from celerydocker.celeryconfig import *  # NOQA

# List of modules to import when celery starts.
CELERY_IMPORTS = ('job3')

CELERY_DEFAULT_QUEUE = 'job3'

CELERY_QUEUES = {
    'job3': {
        'exchage': 'job3',
        'binding_key': 'job3',
        'routing_key': 'job3',
    },
}

CELERYD_PREFETCH_MULTIPLIER = 20
CELERYD_CONCURRENCY = 20
