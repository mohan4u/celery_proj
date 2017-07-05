from celery.schedules import crontab
from celery.task import periodic_task


@periodic_task(run_every=crontab())
def example():
    print "Welcome Mohan..........."
