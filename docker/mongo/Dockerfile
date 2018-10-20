FROM mongo:3.2.21-jessie

RUN apt-get update

COPY ./docker/mongo/docker-entrypoint-initdb.d /docker-entrypoint-initdb.d

RUN chmod +x -R /docker-entrypoint-initdb.d

CMD ["mongod"]
