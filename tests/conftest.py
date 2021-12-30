from sqlalchemy import create_engine, engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import settings
from app.database import get_db, Base
from app.main import app
import pytest
from fastapi.testclient import TestClient

SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}_test'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Drop and create database, start the session with engine to create the database
@pytest.fixture(scope='module')
def session():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

# call the session function and over-riding the get_db
@pytest.fixture(scope='module')
def client(session):
    def override_get_db():
        try:
            yield session
        finally:
            session.close()
    app.dependency_overrides[get_db] = override_get_db

    yield TestClient(app)

# User test for user login
@pytest.fixture
def test_user(client):
    user_data = {'email':'burhan@gmail.com', 'password':'Burhan@123'}
    res = client.post("/users/", json=user_data)
    # To add password to res.json() data
    new_data = res.json()
    new_data['password'] = user_data['password']
    return new_data