# file:     app/services/inventory_service.py

from app.supabase_client import supabase
from typing import List
from app.models.inventory_model import InventoryItem

def get_all_inventory() -> List[InventoryItem]:
    response = supabase.table("inventory").select("*").execute()
    items_data = response.data or []
    return [InventoryItem(**item) for item in items_data]

def get_inventory_by_id(pid: int) -> InventoryItem | None:
    response = supabase.table("inventory").select("*").eq("pid", pid).limit(1).execute()
    if not response.data:
        return None
    return InventoryItem(**response.data[0])