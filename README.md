# Celery Docker Example

This is an example of running Celery workers using Docker.  It demonstrates the use of multiple celery queues in a single RabbitMQ instance to run asynchronous tasks. It assumes nothing is waiting on data to be returned by the sequence of jobs, so it doesn't use Celery's result backend.

## Usage

### Requirements

* [make](https://www.gnu.org/software/make/)
* [docker](https://docs.docker.com/compose/install/)
* [docker-compose](https://docs.docker.com/compose/install/)

### Build docker images

From the root of the project run:

```
make
```

### Run the Workers

From the root of the project run:

```
docker-compose up
```

### Run a test

From the root of the project run:

```
./testme
```

## Overview

In this example, there are 3 sequential jobs.  Each job performs the simple task of modifying a string and handing it off to the next job for further processing.

Two different methods of passing data between jobs are used. job1 hands its work off to job2 using pure celery. This method doesn't scale if the result of a job is a large chunk of data, but is perfectly fine for small data. job2 hands the off to job3 over redis. When you are working with a large data set, it is best to use a storage backend of some sort to pass data around.