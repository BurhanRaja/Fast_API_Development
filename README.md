# Fast_API_Development

- Overview
- Motivation
- Description
- Installation and Requirements
- Technologies used
- Directory Tree
- Demo

## Overview
The project is based on API development of a social media type application using a framework called Fastapi in python.

## Motivation
The motivation for doing this project to learn about how apis work in the backend of an application, how json is used to send data in frontend and to learn Postgresql database, Postman and SQLalchemy.
To explore the Fatsapi framework.

## Description
Here, I have used Fastapi framework to create a social media type application API.
I have used SQLalchemy and alembic to connect the database to the Postgresql.
I have used Pydantic models to create schemas of the json data sent to the frontend.
I have used jose library to generate a jwt token for the frontend data.

## Installation and Requirements

```
python == 3.9.6
```

### create env
```
python -m venv Fastapi
```

### Libraries
This will install all the lib required for the api development
```
pip install fastapi[all]
```

## Technologies used
![image](https://user-images.githubusercontent.com/76507095/146717612-7746a2e6-fb38-4b28-a247-3833f2ee3d04.png)

![image](https://user-images.githubusercontent.com/76507095/146717782-af5949f2-cc9f-45c4-ad2f-6d0eafaae959.png)

![image](https://user-images.githubusercontent.com/76507095/146717727-b9742da3-7380-408d-8f50-e9c2f7c0d5ae.png)

![image](https://user-images.githubusercontent.com/76507095/146717693-b4d0d6c9-e845-4213-9330-ee091251803b.png)


## Directory Tree

```
|---alembic
      |----- versions
                |------ 173258760f5d_add_foreign_key_to_user_id_in_posts_.py
                |------ 79439294dfcb_create_user_table.py
                |------ 9cef9eb5df04_add_remaining_columns_in_posts_table.py
                |------ ce912128bc12_create_vote_table.py
                |------ e9b5cbc8a07c_create_new_post.py
      |----- README
      |----- env.py
      |----- script.py.mako

|--- app
      |---- routers
              |------ auth.py
              |------ post.py
              |------ user.py
              |------ vote.py
      |---- __init__.py
      |---- config.py
      |---- database.py
      |---- main.py
      |---- models.py
      |---- oauth2.py
      |---- schemas.py
      |---- utils.py

|--- .gitignore
|--- Procfile
|--- README.md
|--- alembic.ini
|--- requirements.txt
```

## Demo

COMING SOON !!!
