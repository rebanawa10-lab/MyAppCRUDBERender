# file:     app/models/user_model.py

from pydantic import BaseModel

class User(BaseModel):
    id: int
    email: str
    username: str