from os import environ

from celery import Celery

PASSWORD = environ.get('BROKER_PASSWORD')
HOST = environ.get('HOST')

# redis://:<password>@<server || localhost>
app = Celery(
    'tasks',
    backend=f'redis://:{PASSWORD}@{HOST}',
    broker=f'redis://:{PASSWORD}@{HOST}'
)

@app.task
def add(x, y):
    return x + y

# call tasks with <function>.delay()
# get status with result.ready() and value with result.get()