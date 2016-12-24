from celerydocker.job2 import job2
from job1Queue import job1Queue


@job1Queue.task(ignore_result=True)
def do_job1(job_id):
    """
    job1 appends ":job1" to the job, id and hands
    that string off to job2 via celery for further processing
    """

    work = "%s:job1" % job_id

    j = job2()
    j.do_job2(job_id, work)

    print(
        "job1 did %s with id %s and handed off to job2" %
        (work, job_id))
