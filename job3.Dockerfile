FROM celerydocker/worker

RUN addgroup -S job3-celery -g 533 && \
    adduser -u 433 -S -g job3-celery -h /usr/src/app -s /sbin/nologin job3-celery

USER job3-celery

COPY ./celerydocker /usr/src/app/celerydocker
COPY ./job3 /usr/src/app/job3

WORKDIR /usr/src/app/job3

CMD ["python3","-u", "/usr/bin/celery", "worker", "-A", "job3", "--workdir=/usr/src/app/job3"]
