# Importing Libraries
from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
from sqlalchemy import engine
from starlette.status import HTTP_204_NO_CONTENT
import psycopg2 as pg
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session
from . import models
from .database import engine, get_db

models.Base.metadata.create_all(bind=engine)

# Getting app of fastapi
app = FastAPI()

# Schema API = Structured data
class Post(BaseModel):
    title: str
    content: str
    published: bool = True

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


# Creating database like format
my_posts = [{"title": "This is my 1st post", "content":"This is my 1st content", "id":1}, {"title": "My favourite recipe", "content": "Below are three recipes", "id":2}]

# Function to get a post from my_posts
def find_post(id):
    for p in my_posts:
        if p['id'] == id:
            return p

# Function to delete a post from my_posts
def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i

# GET Request
@app.get("/")
def root():
    return {"message":"Welcome to my World!"}

# GET Request to recieve all posts of a user
@app.get("/posts")
def posts():
    # from database
    cursor.execute(""" SELECT * FROM posts """)
    posts = cursor.fetchall()
    return {"All_Posts": posts}

# Test
@app.get("/sqlalchemy")
def test_post(db: Session = Depends(get_db)):

    posts = db.query(models.Post).all()
    return{"data":posts}


# POST Request (Create)
@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(post : Post):
    # from database
    cursor.execute(""" INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING * """, (post.title, post.content, post.published))
    new_post = cursor.fetchone()
    # Saving int Database
    conn.commit()

    return {"Data":new_post}


# GET request to recieve one post of a particular user
@app.get("/posts/{id}")
def get_post(id : int):
    cursor.execute(""" SELECT * FROM posts WHERE id = %s RETURNING * """, (str(id)))
    post = cursor.fetchone()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} not found")
    return {"One_Post" : post}


# DELETE request to delete one post of a particular user
@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int):
    cursor.execute(""" DELETE FROM posts WHERE id = %s RETURNING * """, (str(id)))
    delete_post = cursor.fetchone()
    # Saving in Database
    conn.commit()

    if delete_post == None:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} not found")
        
    return Response(status_code=HTTP_204_NO_CONTENT)

# 
@app.put("/posts/{id}")
def update_post(id:int, post:Post):
    cursor.execute(""" UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING * """, (post.title, post.content, post.published, str(id)))
    update_posts = cursor.fetchone()

    if update_posts == None:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} not found")

    conn.commit()
    return {"data" : update_posts}