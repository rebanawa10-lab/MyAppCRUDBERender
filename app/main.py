# file:     app/main.py

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import inventory, user
from app.supabase_client import supabase
import logging

app = FastAPI()

# Configure logging
logging.basicConfig(level=logging.INFO)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
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



@app.get("/testdb")
def test_db():
    try:
        # Attempt to fetch 1 user from Supabase
        response = supabase.table("users").select("*").limit(1).execute()

        if response.error:
            # Supabase returned an error
            logging.error(f"Supabase error: {response.error}")
            raise HTTPException(status_code=500, detail=f"Supabase error: {response.error}")

        # Successful response
        return {"connected": True, "data": response.data}

    except Exception as e:
        # Log unexpected exceptions
        logging.exception("Unexpected error when testing database connection")
        raise HTTPException(status_code=500, detail=f"Database connection failed: {e}")