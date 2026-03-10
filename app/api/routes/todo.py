# file:     app/api/routes/todo.py

from fastapi import APIRouter, HTTPException
from supabase import create_client
import os

router = APIRouter(prefix="/todo", tags=["todo"])

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)


# CREATE todo
@router.post("/")
def create_todo(data: dict):
    try:
        response = supabase.table("todo").insert(data).execute()
        return response.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# GET all data
@router.get("/")
def get_todo():
    try:
        response = supabase.table("todo").select("*").execute()
        return response.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# GET one data
@router.get("/{id}")
def get_todo_data(id: int):
    try:
        response = supabase.table("todo").select("*").eq("id", id).execute()

        if not response.data:
            return {"message": "Data not found"}

        return response.data[0]

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# UPDATE data
@router.put("/{id}")
def update_todo(id: int, data: dict):
    try:
        response = supabase.table("todo").update(data).eq("id", id).execute()
        return response.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# DELETE data
@router.delete("/{id}")
def delete_todo(id: int):
    try:
        response = supabase.table("todo").delete().eq("id", id).execute()
        return response.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))