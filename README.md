# Fast_API_Development

- Overview
- Description
- Motivation
- Installations
- Technologies Used
- Directory Tree 

## Overview
I have created an API Development project to understand how an API sends a request to a frontend from the backend.
So, to understand this I built the whole API from scratch using FastApi library in python.
This API contains a combination great libraries which are worth exploring in python.
Head to URL:- http://127.0.0.1:8000/ after downloading requirements.txt and running the server command given in Installations.

## Description
It was hard for me to understand how an API works in theory, so I tried to implement it myself with the help from the documentation and freecodecamp.org.
But, now I can say that I understand that how an API works in the backend.
The API project is based on the FastApi library i.e. a fast and efficient library for the backend development.
I used SqlAlchemy and alembic to connect the Postgresql database to store, recieve and send the data to and from the api.
I undertood the use of Postman, for testing, which I found very powerful.
I used pytest for testing the API before pushing it to production.
I also used CI/CD pipeline to push the changes in production after testing.

## Motivation
The main motivation for me to do such project was to understand the working of API in the backend.
To explore the different libraries of python like FastApi, SqlAlchemy, Psycopg, pydantic etc.
To understand the how to use database and how to connect a database with a server.

## Installations
### FastApi
```
pip install "fastapi[all]"
```
### SqlAlchemy
```
pip install sqlalchemy
```
### Psycopg (Postgresql library for python)
```
pip install psycopg2-binary
```
### To start the server use the below command
```
uvicorn app.main:app
```
### JWT Authentication token
```
pip install authlib
```

## Technologies Used

![image](https://user-images.githubusercontent.com/76507095/147755400-a5cfb60a-2db8-4e97-a439-f50130038e41.png)

![image](https://user-images.githubusercontent.com/76507095/147755421-ddfefbda-37e7-4192-8210-24ad5c157c79.png)

![image](https://user-images.githubusercontent.com/76507095/147755435-da58fcae-bb66-4f51-a2c7-15518dc10a37.png)

![image](https://user-images.githubusercontent.com/76507095/147755469-18774057-dfef-4b97-a59b-f040a29614c9.png)

![image](https://user-images.githubusercontent.com/76507095/147755773-2686d3a0-246a-4f11-981c-bb345519097c.png)

![image](https://user-images.githubusercontent.com/76507095/147755830-420f116d-3ba7-476c-b145-78b5eddf7486.png)


## Directory Tree
```
|--- alembic
      |---- versions
              |----- 173258760f5d_add_foreign_key_to_user_id_in_posts_.py
              |----- 79439294dfcb_create_user_table.py
              |----- 9cef9eb5df04_add_remaining_columns_in_posts_table.py
              |----- ce912128bc12_create_vote_table.py
              |----- e9b5cbc8a07c_create_new_post.py
      |---- README
      |---- env.py
      |---- script.py.mako
|--- app
      |---- routers
              |----- auth.py
              |----- post.py
              |----- user.py
              |----- vote.py
      |---- __init__.py
      |---- config.py
      |---- database.py
      |---- main.py
      |---- models.py
      |---- oauth2.py
      |---- schemas.py
      |---- utils.py
|--- tests
      |---- __init__.py
      |---- conftest.py
      |---- database.py
      |---- test_users.py
|--- .gitignore
|--- Procfile
|--- README.md
|--- alembic.ini
|--- requirements.txt
```
