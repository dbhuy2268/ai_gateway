import os


REDIS_HOST = os.environ.get("REDIS_HOST", "localhost")
REDIS_PORT = os.environ.get("REDIS_PORT", 6379)

CELERY_REDIS_URL = f"redis://{REDIS_HOST}:{REDIS_PORT}/0"
