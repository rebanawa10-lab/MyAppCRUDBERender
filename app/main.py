# file:     app/main.py

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import inventory, user
from app.supabase_client import supabase
import logging

# Supabase connection
from supabase import create_client
import os


app = FastAPI()

APP_VERSION = "v1.4"

# Supabase connection
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Configure logging
logging.basicConfig(level=logging.INFO)

# CORS
app.add_middleware(
    CORSMiddleware,
    # allow_origins=[
    #     "http://localhost:5173",
    #     "http://127.0.0.1:5173",
    #  "https://myappcrudberender.onrender.com",  # optional if calling from same domain
    # ],
     allow_origins=[
        "http://localhost:4173",  # npm run preview locally
        "http://localhost:5173",  # npm run dev
        "https://rebanawa10-lab.github.io",                     # GitHub Pages root
        "https://rebanawa10-lab.github.io/MyAppCRUDFEReact",    # GitHub Pages project page
       
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(user.router)
app.include_router(inventory.router)

@app.get("/")
def root():
    return {"message": "FastAPI + Supabase running"}

@app.get("/version")
def version():
    return {"version": APP_VERSION}

# NEW: 
# Test database connection
@app.get("/testdb")
def test_db():
    try:
        response = supabase.table("inventory").select("*").limit(1).execute()
        if response.error:
            logging.error(f"Supabase error: {response.error}")
            raise HTTPException(status_code=500, detail=f"Supabase error: {response.error}")
        return {"database": "connected", "data": response.data}
    except Exception as e:
        logging.exception("Database connection failed")
        raise HTTPException(status_code=500, detail=f"Database connection failed: {e}")
    

# OLDV2:
# def test_db():
#     try:
#         response = supabase.table("inventory").select("*").limit(1).execute()

#         return {
#             "database": "connected",
#             "data": response.data
#         }

#     except Exception as e:
#         raise HTTPException(
#             status_code=500,
#             detail=f"Database connection failed: {str(e)}"
#         )


# OLD: 
# @app.get("/testdb")
# def test_db():
#     try:
#         # Attempt to fetch 1 user from Supabase
#         response = supabase.table("users").select("*").limit(1).execute()

#         if response.error:
#             # Supabase returned an error
#             logging.error(f"Supabase error: {response.error}")
#             raise HTTPException(status_code=500, detail=f"Supabase error: {response.error}")

#         # Successful response
#         return {"connected": True, "data": response.data}

#     except Exception as e:
#         # Log unexpected exceptions
#         logging.exception("Unexpected error when testing database connection")
#         raise HTTPException(status_code=500, detail=f"Database connection failed: {e}")