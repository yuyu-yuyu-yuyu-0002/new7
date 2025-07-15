from fastapi import APIRouter

router = APIRouter()

@router.get("/facebook/ping")
def ping():
    return {"msg": "facebook route ok"}
