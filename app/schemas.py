from pydantic import BaseModel
from pydantic.networks import EmailStr
from sqlalchemy import orm
from datetime import datetime

# Schema API = Structured data

# Posts
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

# Posts Response
class PostResponse(PostBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode=True


# Users
class UserCreate(BaseModel):
    email: EmailStr
    password: str

# Users Response
class UserResponse(BaseModel):
    user_id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode=True 