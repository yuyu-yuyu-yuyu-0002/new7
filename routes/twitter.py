from fastapi import APIRouter

router = APIRouter()

@router.get("/twitter/ping")
def ping():
    return {"msg": "twitter route ok"}
