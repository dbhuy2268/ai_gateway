import json
import logging
from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from src.utils.websocket import ConnectionManager

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/translate",
    tags=["translate"],
    responses={404: {"description": "Not found"}},
)


manager = ConnectionManager()


@router.get("/test")
async def test():
    await manager.broadcast("Test message")
    return {"status": 200, "message": "OK"}


@router.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: str):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_json()
            logger.info("data:")
            logger.info(json.dumps(data))
            # await manager.send_personal_message(f"You wrote: {data}", websocket)
            # await manager.broadcast_json(f"Client {client_id} said: {json.dumps(data)}")
            data["text"] = f"""Client {client_id} said: {data["text"]}"""
            await manager.broadcast_json(data)
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Client {client_id} left the chat")
