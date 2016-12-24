FROM celerydocker/worker

RUN pip3 install flake8

COPY ./celerydocker /usr/src/app/celerydocker
COPY ./test /usr/src/app/test

WORKDIR /usr/src/app/test