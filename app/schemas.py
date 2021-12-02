from pydantic import BaseModel

# Schema API = Structured data
class PostBse(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBse):
    pass