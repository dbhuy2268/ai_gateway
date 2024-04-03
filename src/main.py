from fastapi import FastAPI
from src.tasks.translate import router as translate_router

app = FastAPI()

app.include_router(translate_router)


@app.get("/")
def health_check():
    return {"status": 200, "message": "OK"}
