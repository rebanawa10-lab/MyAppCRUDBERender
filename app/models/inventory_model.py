# file: app/models/inventory_model.py

from pydantic import BaseModel
from typing import Optional

class InventoryItem(BaseModel):
    pid: int
    pcode: str
    pdesc: Optional[str] = None
    pprice: float
    