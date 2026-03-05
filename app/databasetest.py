#C:\Repos\FastAPI\app>  python databasetest.py
#RESULT:                (1,)
#REMARKS:               If it prints (1,), your SQL Server login works.


import pyodbc

# Replace sa / MyStrongPassword with your SQL Server credentials
conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost;"
    "DATABASE=AzureSQL;"
    "UID=sa;"
    "PWD=86427211abc"
)
cursor = conn.cursor()
cursor.execute("SELECT 1")  # simple test query
print(cursor.fetchone())    # should print (1,)
conn.close()