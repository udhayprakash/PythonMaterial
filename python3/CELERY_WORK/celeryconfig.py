CELERY_IMPORTS = "tasks"
CELERY_IGNORE_RESULTS = False
BROKER_HOST = "127.0.0.1"
BROKER_PORT = 5672
BROKER_URL = "amqp://"

from datetime import timedelta

CELERY_BEAT_SCHEDULE = {"doctor-every-10-seconds": {"task": ""}}
