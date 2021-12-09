from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import User
from ..utils import verify
from ..oauth2 import create_encode_token
from ..schemas import Token

router = APIRouter(tags=['Authentication'])

@router.post("/login", response_model=Token)
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    log_user = db.query(User).filter(User.email == user_credentials.username).first()

    if not log_user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f'Invalid Credentials')
    
    # To verify the hashed password
    if not verify(user_credentials.password, log_user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f'Invalid Credentials.')
    
    access_token = create_encode_token(data = {"user_id":log_user.user_id})
    return {"access_token":access_token, "token_type":"bearer"} 