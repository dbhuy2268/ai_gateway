from celery import Celery
from src.configs.base import CELERY_REDIS_URL

from .controller import router

celery_task = Celery("ai-service", broker=CELERY_REDIS_URL)


@router.get("/")
def health_check():
    celery_task.send_task("tasks.health_check")
    return {"status": 200, "message": "OK"}
