# Importing Libraries
import psycopg2 as pg
from psycopg2.extras import RealDictCursor
from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
import time
from starlette.status import HTTP_204_NO_CONTENT

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

# Function to iterate the index of posts 1 by 1 in my_posts
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
    return {"All_Posts": my_posts}



# POST Request (Create)
@app.post("createposts/posts", status_code=status.HTTP_201_CREATED)
def create_post(post : Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 1000000)
    my_posts.append(post_dict)
    return {"Post": post_dict}



# GET request to recieve one post of a particular user
@app.get("getposts/posts/{id}")
def get_post(id : int, response: Response):
    post = find_post(id) # The id becomes string when passed in {}, so to convert it apply int()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} not found")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"Error message": f"post with id: {id} not found"}
    return {"One_Post" : post}



# DELETE request to delete one post of a particular user
@app.delete("deleteposts/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int):
    index = find_index_post(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} not found")
    my_posts.pop(index)
    return Response(status_code=HTTP_204_NO_CONTENT)



# UPDATE request to update a already existing post
@app.put("updateposts/posts/{id}")
def update_post(id:int, post:Post):
    
    cursor.execute(""" UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING * """, (post.title, post.content, post.published, str(id)))
    update_posts = cursor.fetchone()
    
    if update_posts == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} not found")
    conn.commit()
    return {"data" : update_posts}