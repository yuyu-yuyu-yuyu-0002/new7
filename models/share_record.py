from pydantic import BaseModel

class ShareRecord(BaseModel):
    id: int
    user_id: int
    platform: str
    timestamp: str
