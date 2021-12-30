
from jose import jwt
from app import schemas
import pytest
from app.config import settings

# def test_root(client):
#     res = client.get('/')
#     print(res.json().get('message'))
#     assert res.json().get('message') == 'Welcome to my World!'
#     assert res.status_code == 200



def test_create_user(client):
    res = client.post("/users/", json={'email':"burhanuddin@gmail.com", 'password':'Burhan@786'})
    new_user = schemas.UserResponse(**res.json())
    assert new_user.email == 'burhanuddin@gmail.com'
    assert res.status_code == 201


def test_login(client, test_user):
    res = client.post("/login", data={'username':test_user['email'], 'password':test_user['password']})
    # print(res.json())
    login_res = schemas.Token(**res.json())
    payload = jwt.decode(login_res.access_token,
                         settings.secret_key, algorithms=[settings.algorithm])
    id = payload.get("user_id")
    assert id == test_user['id']
    assert login_res.token_type == "bearer"
    assert res.status_code == 200