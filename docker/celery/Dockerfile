# use Python 3.6 until 3.7 "from . import async, base" syntax error is fixed
# https://stackoverflow.com/questions/51273659/trouble-in-setting-celery-tasks-backend-in-python/51308631
# https://github.com/celery/kombu/issues/896
FROM python:3.6.6-stretch

RUN apt-get update

WORKDIR /usr/src/app

COPY ./celery/requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

COPY ./celery/celerie_queue ./celerie_queue

CMD ["celery", "-A", "celerie_queue", "worker", "--concurrency=20", "--loglevel=info"]
