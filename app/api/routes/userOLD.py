from fastapi import APIRouter
from app.services.user_service import get_all_users
from typing import List
from app.models.user_model import User

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/", response_model=List[User])
def read_users():
    return get_all_users()