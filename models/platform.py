from pydantic import BaseModel

class Platform(BaseModel):
    id: int
    name: str
