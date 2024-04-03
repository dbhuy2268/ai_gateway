from fastapi import APIRouter, WebSocket
from src.utils.celery import celery_task

router = APIRouter(
    prefix="/translate",
    tags=["translate"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
def health_check():
    celery_task.send_task("tasks.health_check")
    return {"status": 200, "message": "OK"}


@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")
