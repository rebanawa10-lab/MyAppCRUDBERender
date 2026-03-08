# file: app/api/routes/inventory.py

from fastapi import APIRouter, HTTPException
from supabase import create_client
import os

router = APIRouter(prefix="/inventory", tags=["inventory"])

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)


# CREATE inventory
@router.post("/")
def create_inventory(item: dict):
    try:
        response = supabase.table("inventory").insert(item).execute()
        return response.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# GET all inventory
@router.get("/")
def get_inventory():
    try:
        response = supabase.table("inventory").select("*").execute()
        return response.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# GET one inventory
@router.get("/{pid}")
def get_inventory_item(pid: int):
    try:
        response = supabase.table("inventory").select("*").eq("id", pid).execute()

        if not response.data:
            return {"message": "Item not found"}

        return response.data[0]

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# UPDATE inventory
@router.put("/{pid}")
def update_inventory(pid: int, item: dict):
    try:
        response = supabase.table("inventory").update(item).eq("id", pid).execute()
        return response.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# DELETE inventory
@router.delete("/{pid}")
def delete_inventory(pid: int):
    try:
        response = supabase.table("inventory").delete().eq("id", pid).execute()
        return response.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))