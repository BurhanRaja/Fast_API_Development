# Importing Libraries
from typing import List
from fastapi import FastAPI
from sqlalchemy import engine
import psycopg2 as pg
from psycopg2.extras import RealDictCursor
import time
from . import models
from .database import engine
from .routers import post, user, auth

# Creating the database table
models.Base.metadata.create_all(bind=engine)

# Getting app of fastapi
app = FastAPI()

# Putting condition for connecting to database
while True:
    try:
        conn = pg.connect(host='localhost', database='fastapi_API_Dev', user='postgres', password='Burhan123', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was successfull!!")
        break
    except Exception as error:
        print("Connecting to database failed!!")
        print("ERROR: ", error)
        time.sleep(2)


# Connecting to the routers
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)

# GET Request
@app.get("/")
def root():
    return {"message":"Welcome to my World!"}
