#!/usr/bin/env python3
import uuid

from celerydocker.job1 import job1

j = job1()

j.do_job1(str(uuid.uuid4()))
