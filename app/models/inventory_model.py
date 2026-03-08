# file: app/models/inventory_model.py

from pydantic import BaseModel
from typing import Optional

class InventoryItem(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float
    quantity: int