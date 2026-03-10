# file:     app/models/todo_model.py

from pydantic import BaseModel
from typing import Optional

class TodoItem(BaseModel):
    id: int
    name: Optional[str] = None
