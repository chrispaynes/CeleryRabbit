from __future__ import absolute_import
from celery import Celery

# backend = the task result store backend to use for this task (if access to the results is needed after task completion)
app = Celery('celerie_queue', broker='amqp://admin:pass@192.168.99.120', backend='rpc://', include=['celerie_queue.tasks'])
