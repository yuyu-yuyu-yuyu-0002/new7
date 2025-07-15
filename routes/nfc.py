from fastapi import APIRouter

router = APIRouter()

@router.get("/nfc/ping")
def ping():
    return {"msg": "nfc route ok"}
