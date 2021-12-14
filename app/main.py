# Importing Libraries
from fastapi import FastAPI
from sqlalchemy import engine
from . import models
from .database import engine
from .routers import post, user, auth

# Creating the database table
models.Base.metadata.create_all(bind=engine)

# Getting app of fastapi
app = FastAPI()

# Connecting to the routers
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)

# GET Request
@app.get("/")
def root():
    return {"message":"Welcome to my World!"}
