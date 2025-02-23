from flask import Flask, render_template
import redis
from celery import Celery

app = Flask(__name__)

# Configure Celery
app.config['CELERY_BROKER_URL'] = 'redis://redis:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://redis:6379/0'

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081, debug=True)
