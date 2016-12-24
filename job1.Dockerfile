FROM celerydocker/worker

RUN apk add --update --no-cache  bash && \
    addgroup -S job1-celery -g 531 && \
    adduser -u 431 -S -g job1-celery -h /usr/src/app -s /sbin/nologin job1-celery

USER job1-celery

# Because adding our (fake) bash requirment via apk is slow
# we do it BEFORE we copy the common clerydocker directory
# that gets shared between all of the workers. The time
# saved during development cycles by not having to reinstall
# bash every time something in the shared library changes is
# well worth the deviation from a "pure" image inheritance
# tree.  If the shared library was copied in worker.Dockerfile,
# then every time you make a change in the celerydocker directory,
# docker will invalidate the build cache for everything that happens
# after the change and the slow running apk add above would run during
# job1 worker build.

COPY ./celerydocker /usr/src/app/celerydocker
COPY ./job1 /usr/src/app/job1

WORKDIR /usr/src/app/job1

CMD ["python3","-u", "/usr/bin/celery", "worker", "-A", "job1", "--workdir=/usr/src/app/job1"]
