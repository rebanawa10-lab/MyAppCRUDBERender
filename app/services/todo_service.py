# file:     app/services/todo_service.py

from app.supabase_client import supabase
from typing import List
from app.models.todo_model import TodoItem

def get_all_todo() -> List[TodoItem]:
    response = supabase.table("todo").select("*").execute()
    items_data = response.data or []
    return [TodoItem(**item) for item in items_data]

def get_todo_by_id(id: int) -> TodoItem | None:
    response = supabase.table("todo").select("*").eq("id", id).limit(1).execute()
    if not response.data:
        return None
    return TodoItem(**response.data[0])