# file:     app/crud_Inventory.py

from .supabase_client import supabase


def get_inventories():
    response = supabase.table("inventory").select("*").execute()
    return response.data


def get_inventory(pid: int):
    response = supabase.table("inventory").select("*").eq("pid", pid).execute()
    return response.data


def create_inventory(data: dict):
    response = supabase.table("inventory").insert(data).execute()
    return response.data


def update_inventory(pid: int, data: dict):
    response = supabase.table("inventory").update(data).eq("pid", pid).execute()
    return response.data


def delete_inventory(pid: int):
    response = supabase.table("inventory").delete().eq("pid", pid).execute()
    return response.data