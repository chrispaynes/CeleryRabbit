# CeleryRabbit
Celery + RabbitMQ + Django + Mongo App

## Features

- Celery Task Queue
- Danjo
- MongoDB
- RabbitMQ

## Requirements

  - [Docker](https://www.docker.com/) and [Docker-Compose](https://docs.docker.com/compose/install/)

## Configuration

The following tables lists the configurable application environment variables that need to be defined in the `configs/app.toml`.

| Parameter        | Description           | Example  |
| ------------- |-------------| -----|
| MONGODB_URL | | 'mongodb://0.0.0.0:0000/' |
| SECRET_KEY | Django App Secret Key | 'secretkey' |
| HOST_IP | | "0.0.0.0" |
| RABBITMQ_DEFAULT_USER | | "user" |
| RABBITMQ_DEFAULT_PASS | | "pass" |


## Quickstart

1. Start the docker services with `make start`

1. Open the RabbitMQ Management UI at `http://localhost:15672` and enter your credentials

1. Generate some tasks for Celery `make tasks`

## Architecture
```
├── app
│   ├── manage.py
│   ├── rabbittasker
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   └── requirements.txt
├── celery
│   ├── celerie_queue
│   │   ├── celery.py
│   │   ├── __init__.py
│   │   ├── run_tasks.py                # generates multiple tasks
│   │   └── tasks.py                    # defines a singular worker task
│   └── requirements.txt
├── configs
│   └── app.toml
├── docker
│   ├── celery
│   │   └── Dockerfile
│   ├── django
│   │   └── Dockerfile
│   ├── mongo
│   │   ├── data                        # DB data volume
│   │   ├── docker-entrypoint-initdb.d
│   │   │   └── tasks.sh
│   │   └── Dockerfile
│   └── rabbitmq
│       ├── Dockerfile
│       └── rabbitmq.env
├── docker-compose.yaml
├── LICENSE
├── Makefile
└── README.md

```
