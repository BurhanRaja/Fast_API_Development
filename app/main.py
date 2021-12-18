# Importing Libraries
from fastapi import FastAPI
from .routers import post, user, auth, vote
from fastapi.middleware.cors import CORSMiddleware

# Creating the database table
# models.Base.metadata.create_all(bind=engine)

# Getting app of fastapi
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Connecting to the routers
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

# GET Request
@app.get("/")
def root():
    return {"message":"Welcome to my World!"}
