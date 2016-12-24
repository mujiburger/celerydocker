FROM celerydocker/worker

RUN addgroup -S job2-celery -g 532 && \
    adduser -u 432 -S -g job2-celery -h /usr/src/app -s /sbin/nologin job2-celery

USER job2-celery

COPY ./celerydocker /usr/src/app/celerydocker
COPY ./job2 /usr/src/app/job2

WORKDIR /usr/src/app/job2

CMD ["python3","-u", "/usr/bin/celery", "worker", "-A", "job2", "--workdir=/usr/src/app/job2"]
