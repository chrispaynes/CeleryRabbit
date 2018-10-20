from __future__ import absolute_import
from celery import Celery
import toml

config = toml.load('app.toml')

user = config.get("RABBITMQ_DEFAULT_USER")
passwd = config.get("RABBITMQ_DEFAULT_PASS")
host = config.get("HOST_IP")
broker_url = f"amqp://{user}:{passwd}@{host}"

# backend = the task result store backend to use for this task (if access to the results is needed after task completion)
app = Celery('celerie_queue', broker=broker_url,
             backend='rpc://', include=['celerie_queue.tasks'])
