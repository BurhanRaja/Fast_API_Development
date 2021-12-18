from pydantic import BaseModel
from pydantic.networks import EmailStr
from pydantic.types import conint
from datetime import datetime
from typing import Optional

# Schema API = Structured data

# Users
class UserCreate(BaseModel):
    email: EmailStr
    password: str

# Users Response
class UserResponse(BaseModel):
    id: int
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

    


# Posts
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

# Posts Response
# Getting the information of user with all post respectively
class PostResponse(PostBase):
    id: int
    created_at: datetime
    user_id: int
    user: UserResponse

    class Config:
        orm_mode=True


# Vote
class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)


# Posted
class PostedVote(BaseModel):
    Post: PostResponse
    votes: int

    class Config:
        orm_mode=True
