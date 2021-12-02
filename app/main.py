# Importing Libraries
from fastapi import FastAPI, Response, status, HTTPException, Depends
from sqlalchemy import engine
from starlette.status import HTTP_204_NO_CONTENT
import psycopg2 as pg
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session
from . import models, schemas
from .database import engine, get_db

models.Base.metadata.create_all(bind=engine)

# Getting app of fastapi
app = FastAPI()

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
def posts(db: Session = Depends(get_db)):
    # from database
    posts = db.query(models.Post).all()
    return{"data":posts}


# POST Request (Create)
@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(post : schemas.PostCreate, db: Session = Depends(get_db)):
    new_post = models.Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return {"Data":new_post}


# GET request to recieve one post of a particular user
@app.get("/posts/{id}")
def get_post(id : int, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} not found")
    return {"One_Post" : post}


# DELETE request to delete one post of a particular user
@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int, db: Session = Depends(get_db)):
    del_post = db.query(models.Post).filter(models.Post.id == id)
    if del_post.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} not found")
    del_post.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=HTTP_204_NO_CONTENT)

# 
@app.put("/posts/{id}")
def update_post(id:int, post:schemas.PostCreate, db: Session = Depends(get_db)):
    
    post_query = db.query(models.Post).filter(models.Post.id == id)
    update_post = post_query.first()

    if update_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} not found")
    
    post_query.update(post.dict(), synchronize_session=False)
    db.commit()
    return {"data" : post_query.first()}