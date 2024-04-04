from fastapi import APIRouter


router = APIRouter(
    prefix="/test",
    tags=["test"],
    responses={404: {"description": "Not found"}},
)


@router.get("/ram")
def test_ram():
    some_str = bytearray(1024 * 1024 * 1000)
    print("Memory allocated")
    return {"status": 200, "message": "OK"}
