from typing import List
from fastapi import Response, status, HTTPException, Depends, APIRouter
from starlette.status import HTTP_204_NO_CONTENT
from sqlalchemy.orm import Session
from app import oauth2
from app.oauth2 import get_current_user
from .. import models, schemas
from ..database import get_db

router = APIRouter(
    prefix="/posts", 
    tags=['Post']
)

# GET Request to recieve all posts of a user
@router.get("/", response_model= List[schemas.PostResponse])
def posts(db: Session = Depends(get_db), get_user_id: int = Depends(oauth2.get_current_user)):
    # from database
    posts = db.query(models.Post).all()
    return posts


# POST Request (Create)
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.PostResponse)
def create_post(post : schemas.PostCreate, db: Session = Depends(get_db), get_user_id: int = Depends(oauth2.get_current_user)):
    new_post = models.Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


# GET request to recieve one post of a particular user
@router.get("/{id}", response_model=schemas.PostResponse)
def get_post(id : int, db: Session = Depends(get_db), get_user_id: int = Depends(oauth2.get_current_user)):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist.")
    return post


# DELETE request to delete one post of a particular user
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int, db: Session = Depends(get_db), get_user_id: int = Depends(oauth2.get_current_user)):
    del_post = db.query(models.Post).filter(models.Post.id == id)
    if del_post.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist.")
    del_post.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=HTTP_204_NO_CONTENT)


# UPDATE request to edit the post
@router.put("/{id}", response_model=schemas.PostResponse)
def update_post(id:int, post:schemas.PostCreate, db: Session = Depends(get_db), get_user_id: int = Depends(oauth2.get_current_user)):
    
    post_query = db.query(models.Post).filter(models.Post.id == id)
    update_post = post_query.first()
    if update_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist.")
    post_query.update(post.dict(), synchronize_session=False)
    db.commit()
    return post_query.first()