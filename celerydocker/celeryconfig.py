"""
Celery config gets a little hairy.  We run three celery
queues.  One for each job.

This is the base config. It contains all of the common config
options.  There is a config for each worker queue that extends
this and defines ONLY the queue for that worker. If a worker
KNOWS about more than one queue it will try to pull jobs
from more than one queue.  Each worker also extends the queue
definition conf and sets up concurency and prefetch settins.
I define those settings inside of the worker so that they can
be tweaked in production without redeploying all of the workers.
job3 doesn't use this extra config extension so that you have an
example of a more simple configuration structure.
"""

rabbitmq_user = "rb_user"
rabbitmq_pw = "rb_password"
rabbitmq_host = "rabbitmq"
rabbitmq_port = 5672

BROKER_URL = "amqp://%s:%s@%s:%i" % (rabbitmq_user, rabbitmq_pw, rabbitmq_host, rabbitmq_port)  # NOQA

CELERY_TASK_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['json', 'pickle']

# confirm_publish is a poorly documented flag
# http://celery-users.narkive.com/W3xozmpA/strange-celery-producer-issue-when-using-django
# unfortunately the price for confirmation a 10 fold decrease in peformance.
# If you need a higher celery task throughput, turn this off. There is
# potential for tasks to be lost if whatever is triggering the inital task
# is using `send_task` and not waiting around for results.  That potential
# is very low under normal operation.
BROKER_TRANSPORT_OPTIONS = {'confirm_publish': True}

CELERYD_MAX_TASKS_PER_CHILD = 250
CELERY_DISABLE_RATE_LIMITS = True
