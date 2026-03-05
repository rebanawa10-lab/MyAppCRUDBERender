#file:      crud.py

from sqlalchemy.orm import Session
from . import models, schemas 
#must use relative imports there too

def get_users(db: Session):
    return db.query(models.User).all()

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def create_user(db: Session, user: schemas.UserCreate):  # <- use schemas.UserCreate
    db_user = models.User(name=user.name, email=user.email)  # <- use models.User
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user_id: int, user: schemas.UserCreate):
    db_user = get_user(db, user_id)
    if db_user:
        db_user.name = user.name
        db_user.email = user.email
        db.commit()
        db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    db_user = get_user(db, user_id)
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user

# -------------------------
# Inventory CRUD
# -------------------------
def get_inventories(db: Session):
    return db.query(models.Inventory).all()

def get_inventory(db: Session, pid: int):
    return db.query(models.Inventory).filter(models.Inventory.pid == pid).first()

def create_inventory(db: Session, inventory: schemas.InventoryCreate):
    db_inventory = models.Inventory(
        pcode=inventory.pcode,
        pdesc=inventory.pdesc,
        pprice=inventory.pprice
    )
    db.add(db_inventory)
    db.commit()
    db.refresh(db_inventory)
    return db_inventory

def update_inventory(db: Session, pid: int, inventory: schemas.InventoryCreate):
    db_inventory = get_inventory(db, pid)
    if db_inventory:
        db_inventory.pcode = inventory.pcode
        db_inventory.pdesc = inventory.pdesc
        db_inventory.pprice = inventory.pprice
        db.commit()
        db.refresh(db_inventory)
    return db_inventory

def delete_inventory(db: Session, pid: int):
    db_inventory = get_inventory(db, pid)
    if db_inventory:
        db.delete(db_inventory)
        db.commit()
    return db_inventory