from fastapi import APIRouter

router = APIRouter()

@router.get("/voice/ping")
def ping():
    return {"msg": "voice route ok"}
