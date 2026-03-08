# file: app/api/routes/inventory.py

from fastapi import APIRouter, HTTPException
from typing import List
from app.models.inventory_model import InventoryItem
from app.services.inventory_service import get_all_inventory, get_inventory_by_id

router = APIRouter(prefix="/inventory", tags=["inventory"])

@router.get("/", response_model=List[InventoryItem])
def read_inventory():
    return get_all_inventory()

@router.get("/{item_id}", response_model=InventoryItem)
def read_inventory_item(item_id: int):
    item = get_inventory_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Inventory item not found")
    return item