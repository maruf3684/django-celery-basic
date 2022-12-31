from __future__ import absolute_import,unicode_literals
import os

from celery import Celery
from django.conf import settings
from celery.schedules import crontab

#from django_celery_beat.models import PeriodicTask

os.environ.setdefault('DJANGO_SETTINGS_MODULE','task_schedule.settings')
app = Celery('task_schedule')
app.conf.update(enable_utc = False,timezone='Asia/Dhaka')
app.config_from_object(settings,namespace='CELERY')

#app.loader.override_backends['django-db'] = 'django_celery_results.backends.database:DatabaseBackend'

################## celery beat  #############

#see time https://www.timeanddate.com/worldclock/bangladesh/dhaka


##periodic task
app.conf.beat_schedule = {
    'send-mail-every-day-at-8': {
        'task': 'task.tasks.send_mail_func',
        'schedule': crontab(hour=16, minute=26),
        #'schedule': crontab(hour=0, minute=46, day_of_month=19, month_of_year = 6),
        'args': [2]
    }
    
}

#interval task



#dynamic task



#########################

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request:{self.request!r}')