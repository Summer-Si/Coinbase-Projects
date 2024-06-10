from __future__ import absolute_import, unicode_literals
from .celery import app as celery_app
from celery.schedules import crontab

celery_app.conf.beat_schedule = {
    'fetch_data': {
        'task': 'coinbase_app.tasks.fetch_data',
        'schedule': crontab(minute=0, hour='*'), # minute=0, hour='*'
    },
}

__all__ = ('celery_app',)