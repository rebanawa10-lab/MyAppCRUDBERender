# file:     app/services/user_service.py

from app.supabase_client import supabase
from typing import List
from app.models.user_model import User

def get_all_users() -> List[User]:
    response = supabase.table("users").select("*").execute()
    users_data = response.data or []
    return [User(**user) for user in users_data]