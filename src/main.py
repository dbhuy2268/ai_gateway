from fastapi import FastAPI
from src.service.translate.controller import router as translate_router
from src.service.test.controller import router as test_router

app = FastAPI()

app.include_router(translate_router)
app.include_router(test_router)


@app.get("/")
def health_check():
    return {"status": 200, "message": "OK"}
