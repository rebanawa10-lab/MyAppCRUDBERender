# file:     app/crud_user.py 

from app.supabase_client import supabase


def get_users():
    response = supabase.table("users").select("*").execute()
    return response.data


def get_user(uid: int):
    response = supabase.table("users").select("*").eq("uid", uid).execute()
    return response.data


def create_user(data: dict):
    response = supabase.table("users").insert(data).execute()
    return response.data


def update_user(uid: int, data: dict):
    response = supabase.table("users").update(data).eq("uid", uid).execute()
    return response.data


def delete_user(uid: int):
    response = supabase.table("users").delete().eq("uid", uid).execute()
    return response.data