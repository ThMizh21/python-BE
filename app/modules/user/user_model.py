# models.py
from pydantic import BaseModel

class User(BaseModel):
    user_id: int
    name: str
    email: str
    age: int
