from fastapi import APIRouter

router = APIRouter()

@router.get("/instagram/ping")
def ping():
    return {"msg": "instagram route ok"}
