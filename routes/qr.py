from fastapi import APIRouter

router = APIRouter()

@router.get("/qr/ping")
def ping():
    return {"msg": "qr route ok"}
