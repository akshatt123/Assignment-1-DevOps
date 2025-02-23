from celery import Celery
import time

app = Celery(
    "worker",
    broker="redis://redis:6379/0",  # Redis as the message broker
    backend="db+postgresql://myuser:mypassword@db:5432/mydatabase"  # PostgreSQL as result backend

    )

@app.task
def process_task(data):
    time.sleep(5)
    return f"Processed: {data}"




