# file: app/api/routes/inventory.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from ... import schemas, crud
from ...database import get_db  # make sure you have this function in database.py

router = APIRouter(
    prefix="/inventory",
    tags=["Inventory"]
)

# -------------------------
# Get all inventories
# -------------------------
@router.get("/", response_model=List[schemas.Inventory])
def read_inventories(db: Session = Depends(get_db)):
    return crud.get_inventories(db)

# -------------------------
# Get inventory by PID
# -------------------------
@router.get("/{pid}", response_model=schemas.Inventory)
def read_inventory(pid: int, db: Session = Depends(get_db)):
    inventory = crud.get_inventory(db, pid)
    if not inventory:
        raise HTTPException(status_code=404, detail="Inventory not found")
    return inventory

# -------------------------
# Create inventory
# -------------------------
@router.post("/", response_model=schemas.Inventory)
def create_inventory(inventory: schemas.InventoryCreate, db: Session = Depends(get_db)):
    return crud.create_inventory(db, inventory)

# -------------------------
# Update inventory
# -------------------------
@router.put("/{pid}", response_model=schemas.Inventory)
def update_inventory(pid: int, inventory: schemas.InventoryCreate, db: Session = Depends(get_db)):
    updated_inventory = crud.update_inventory(db, pid, inventory)
    if not updated_inventory:
        raise HTTPException(status_code=404, detail="Inventory not found")
    return updated_inventory

# -------------------------
# Delete inventory
# -------------------------
@router.delete("/{pid}", response_model=schemas.Inventory)
def delete_inventory(pid: int, db: Session = Depends(get_db)):
    deleted_inventory = crud.delete_inventory(db, pid)
    if not deleted_inventory:
        raise HTTPException(status_code=404, detail="Inventory not found")
    return deleted_inventory