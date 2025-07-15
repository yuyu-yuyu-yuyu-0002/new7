from fastapi import APIRouter

router = APIRouter()

@router.get("/tiktok/ping")
def ping():
    return {"msg": "tiktok route ok"}
