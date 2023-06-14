from pathlib import Path
from fastapi import FastAPI, Query, Depends
from typing import List
from db import models, crud, schemas
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

CORS_ALLOW_ORIGINS = []

app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ALLOW_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# DB Session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Routes
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/users/")
def read_users(db: Session = Depends(get_db)):
    return crud.get_users(db)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True, port=os.getenv['FAST_API_PORT'])