cd src
celery -A notes worker -l info -P gevent