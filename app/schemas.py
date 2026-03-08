# file:     app/schemas.py

from pydantic import BaseModel

# Example: Inventory
class InventoryCreate(BaseModel):
    name: str
    quantity: int
    price: float

# Example: User
class UserCreate(BaseModel):
    username: str
    email: str