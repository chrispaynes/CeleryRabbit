from __future__ import absolute_import
from celerie_queue.celery import app
import time
import requests
import toml
from pymongo import MongoClient

config = toml.load('app.toml')
client = MongoClient(config.get('MONGODB_URL'))
db = client.celerie_queue
collection = db.tasks

# import the app celery module app and use it as a decorator for the task method
@app.task(name='celerie_queue.task', bind=True, default_retry_delay=20)
def addTime(self, i):
    print('starting long task')

    try:
        # r = requests.get(i)
        # insert long running task
        collection.insert({'status': 200, "created_at": time.time()})
        print('finished task: ', i)
    except Exception as e:
        print("Hit Exception: ", e)
        raise self.retry(e=e)
    return 200
