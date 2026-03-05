#file : user.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session


# OLD:
# from app.database import get_db
# from app import crud, schemas
from app.models import User

# NEW
from typing import List
from ... import schemas, crud
from ...database import get_db



# OLD:
# router = APIRouter()

# NEW:
router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


# GET ALL USERS

@router.get("/")
def read_users(db: Session = Depends(get_db)):
    return crud.get_users(db)




# GET ONE USER
@router.get("/{user_id}")
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


# CREATE USER
@router.post("/")
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)


# UPDATE USER
@router.put("/{user_id}")
def update_user(user_id: int, user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.update_user(db, user_id, user)


# DELETE USER
@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return crud.delete_user(db, user_id)