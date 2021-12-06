from passlib.context import CryptContext

# For Protecting the password in database
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash(password: str):
    # Hash the password
    hashpwd = pwd_context.hash(password)
    return hashpwd