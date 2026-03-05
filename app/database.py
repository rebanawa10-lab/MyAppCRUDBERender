# file:         database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = (
    "mssql+pyodbc://sa:86427211abc@localhost:1433/AzureSQL"
    "?driver=ODBC+Driver+17+for+SQL+Server"
)

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# FORMAT:
# DATABASE_URL = (
#     "mssql+pyodbc://username:password@localhost:1433/YourDB"
#     "?driver=ODBC+Driver+17+for+SQL+Server"
# )
