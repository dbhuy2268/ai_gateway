from celery import Celery

from src.configs.base import CELERY_REDIS_URL


celery_task = Celery("ai-service", broker=CELERY_REDIS_URL)
