# file:     models.py


from sqlalchemy import Column, Integer, String, Numeric
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)


class Inventory(Base):
    __tablename__ = "Inventory"

    pid = Column(Integer, primary_key=True, autoincrement=True)  # matches INT IDENTITY(1,1)
    pcode = Column(String(50), nullable=False)                   # NVARCHAR(50)
    pdesc = Column(String(200))                                  # NVARCHAR(200)
    pprice = Column(Numeric(13, 2))                              # DECIMAL(13,2)