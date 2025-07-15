from fastapi import APIRouter

router = APIRouter()

@router.get("/linkedin/ping")
def ping():
    return {"msg": "linkedin route ok"}
