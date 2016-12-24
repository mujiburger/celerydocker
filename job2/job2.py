from celerydocker.job3 import job3
from celerydocker.redis import Redis

from job2Queue import job2Queue


@job2Queue.task(ignore_result=True)
def do_job2(job_id, work):
    """
    job2 receives a job_id and the work peformed by job1 via
    celery.  It appends ":job2" to the work string, places the
    new string in redis and schedules a job3 task.
    """

    work = "%s:job2" % work

    j2_redis = Redis("job2")
    j2_redis.set(job_id, work)

    j = job3()
    j.do_job3(job_id)

    print(
        "job2 did %s with id %s, put it in redis and scheduled job3" %
        (work, job_id))
