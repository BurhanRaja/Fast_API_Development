from pydantic import BaseModel
from pydantic.networks import EmailStr
from sqlalchemy import orm
from datetime import datetime
from typing import Optional

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

# User Login
class UserLogin(BaseModel):
    email: EmailStr
    password: str

# User token
class Token(BaseModel):
    access_token: str
    token_type: str

# token data
class TokenData(BaseModel):
    id: Optional[str] = None
