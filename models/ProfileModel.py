from pydantic import BaseModel
from typing import Optional

class Profile(BaseModel):
    user_id: str
    name: str
    email: str
    image_url: Optional[str] = None
