from celery import Celery

import mihai as wishMihai


app = Celery('tasks', broker='amqp://guest@localhost//')
app.config_from_object('celeryconfig')


@app.task
def send_message():
    wishMihai.send_message_to_mihai()
