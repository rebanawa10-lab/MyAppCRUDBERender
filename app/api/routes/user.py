# file: app/api/routes/users.py

from fastapi import APIRouter, HTTPException
from supabase import create_client
import os

router = APIRouter(prefix="/users", tags=["users"])

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)


# CREATE
@router.post("/")
def create_user(user: dict):
    try:
        response = supabase.table("users").insert(user).execute()
        return response.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# READ
@router.get("/")
def get_users():
    try:
        response = supabase.table("users").select("*").execute()
        return response.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
# Get One User
@router.get("/{user_id}")
def get_user(user_id: int):
    try:
        response = supabase.table("users").select("*").eq("id", user_id).execute()

        if not response.data:
            return {"message": "User not found"}

        return response.data[0]

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# UPDATE
@router.put("/{user_id}")
def update_user(user_id: int, user: dict):
    try:
        response = supabase.table("users").update(user).eq("id", user_id).execute()
        return response.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# DELETE
@router.delete("/{user_id}")
def delete_user(user_id: int):
    try:
        response = supabase.table("users").delete().eq("id", user_id).execute()
        return response.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))