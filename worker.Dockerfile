FROM alpine:3.4

# we setup and install all of the requirements shared by
# all of the workers in this base image.  To speed up the
# development cycle, we some things that have the potential
# to change frequently AFTER we install requirements that
# are specifice to a single worker. See job1.Dockefile for
# an example.

RUN apk add --update --no-cache \
        python3 \
        python3-dev \
        wget \
        ca-certificates \
        && \
    wget "https://bootstrap.pypa.io/get-pip.py" -O /dev/stdout | python3 && \
    pip3 install \
        celery \
        redis \
        && \
    apk del python3-dev && \
    rm -r /root/.cache && \
    rm -r /usr/lib/python3.5/__pycache__ && \
    rm -r /usr/lib/python3.5/tkinter/__pycache__ && \
    rm -r /usr/lib/python3.5/pydoc_data/__pycache__ && \
    rm -r /usr/lib/python3.5/idlelib/__pycache__ && \
    rm -r /usr/lib/python3.5/encodings/__pycache__ && \
    rm -r /usr/lib/python3.5/asyncio/__pycache__ && \
    rm -r /usr/share/terminfo

ENV PYTHONPATH=${PYTHONPATH}:/usr/src/app
