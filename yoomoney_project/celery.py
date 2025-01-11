from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yoomoney_project.settings')

app = Celery('yoomoney_project')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'schedule-monthly-payments': {
        'task': 'payments.tasks.schedule_monthly_payments',
        'schedule': crontab(hour=0, minute=0),  # Каждый день в полночь
    },
}

app.autodiscover_tasks()
