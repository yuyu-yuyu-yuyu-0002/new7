from fastapi import APIRouter

router = APIRouter()

@router.get("/share/ping")
def ping():
    return {"msg": "share route ok"}
