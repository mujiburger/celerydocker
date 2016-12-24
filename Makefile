.PHONY: all worker test job1 job2 job3

DOCKER_REPO := celerydocker
IMAGE_BASE := $(DOCKER_REPO)/
MY_PWD := $(shell pwd)
UNAME_S := $(shell uname -s)

ifeq ($(UNAME_S),Darwin)
	SED_I := sed -i '.bak'
else
	SED_I := sed -i
endif

all: worker test job1 job2 job3

worker:
	docker build --rm -t $(IMAGE_BASE)worker -f $(MY_PWD)/worker.Dockerfile $(MY_PWD)
ifdef PUSH
	docker push $(IMAGE_BASE)worker
endif

test:
	docker build --rm -t $(IMAGE_BASE)test -f $(MY_PWD)/test.Dockerfile $(MY_PWD)
ifdef PUSH
	docker push $(IMAGE_BASE)test
endif
	docker run --rm -v $(MY_PWD):/usr/src/app $(IMAGE_BASE)test /usr/bin/python3 /usr/bin/flake8 /usr/src/app 1>&2;

job1:
	docker build --rm -t $(IMAGE_BASE)job1 -f $(MY_PWD)/job1.Dockerfile $(MY_PWD)
ifdef PUSH
	docker push $(IMAGE_BASE)job1
endif

job2:
	docker build --rm -t $(IMAGE_BASE)job2 -f $(MY_PWD)/job2.Dockerfile $(MY_PWD)
ifdef PUSH
	docker push $(IMAGE_BASE)job2
endif

job3:
	docker build --rm -t $(IMAGE_BASE)job3 -f $(MY_PWD)/job3.Dockerfile $(MY_PWD)
ifdef PUSH
	docker push $(IMAGE_BASE)job3
endif
