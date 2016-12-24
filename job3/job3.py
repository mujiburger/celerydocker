from celerydocker.redis import Redis

from job3Queue import job3Queue


@job3Queue.task(ignore_result=True)
def do_job3(job_id):
    """
    job3 receives a job_id. It pulls out the work string
    out that job2 created in redis. It appends ":job3" to the
    string, places it in another redis db and then deletes
    the key from the job2 redis store
    """

    j2_redis = Redis("job2")
    work = j2_redis.get(job_id)

    work = "%s:job3" % work

    j3_redis = Redis("job3")
    j3_redis.set(job_id, work)

    j2_redis.delete(job_id)

    print(
        "job3 did %s with id %s and put it in redis. Job Complete!" %
        (work, job_id))
