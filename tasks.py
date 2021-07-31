from celery import Celery

# redis://:<password>@<server || localhost>
app = Celery(
    'tasks',
    backend='redis://:s5JSAv3c7xlUarcGllNWZ+0WhEo7p+unCPkufdW1ENL8I3ZWF8lSsRIcUhf1jYA+13VBJxrgRkp0fOE2@localhost',
    broker='redis://:s5JSAv3c7xlUarcGllNWZ+0WhEo7p+unCPkufdW1ENL8I3ZWF8lSsRIcUhf1jYA+13VBJxrgRkp0fOE2@localhost'
)

@app.task
def add(x, y):
    return x + y

# call tasks with <function>.delay()
# get status with result.ready() and value with result.get()