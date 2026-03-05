# file: schemas.py

from pydantic import BaseModel
from typing import Optional  # <-- import Optional

class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int

    class Config:
        from_attributes = True



# -------------------------
# Inventory Schemas
# -------------------------
class InventoryBase(BaseModel):
    pcode: str
    pdesc: Optional[str] = None
    pprice: float  # can also use Decimal if you want more precision

class InventoryCreate(InventoryBase):
    pass

class Inventory(InventoryBase):
    pid: int

    class Config:
        from_attributes = True
        # orm_mode = True