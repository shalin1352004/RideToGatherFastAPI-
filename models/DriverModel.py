from pydantic import BaseModel

class  Driver(BaseModel):
    driver_id: str
    age: int
    name: str