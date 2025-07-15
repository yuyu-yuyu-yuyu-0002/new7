from pydantic import BaseModel

class SocialLink(BaseModel):
    id: int
    platform: str
    url: str
