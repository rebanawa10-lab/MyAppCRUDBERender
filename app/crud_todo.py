# file:     app/crud_todo.py

from .supabase_client import supabase


def get_todos():
    response = supabase.table("todo").select("*").execute()
    return response.data


def get_todo(id: int):
    response = supabase.table("todo").select("*").eq("id", id).execute()
    return response.data


def create_todo(data: dict):
    response = supabase.table("todo").insert(data).execute()
    return response.data


def update_todo(id: int, data: dict):
    response = supabase.table("todo").update(data).eq("id", id).execute()
    return response.data


def delete_todo(id: int):
    response = supabase.table("todo").delete().eq("id", id).execute()
    return response.data