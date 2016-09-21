from datetime import timedelta

CELERYBEAT_SCHEDULE = {
    'sendMessageToFriend': {
        'task': 'tasks.send_message',
        'schedule': timedelta(seconds=60*30)
    },
}

CELERY_TIMEZONE = 'Europe/Bucharest'
