from fastapi import APIRouter

router = APIRouter()

@router.get("/social/ping")
def ping():
    return {"msg": "social route ok"}
