# BVC-api
### An API developed in Python :snake: with Django, Django Rest Framework and PostgreSQL :elephant:
This API was developed consuming the BVC (Bolsa de Valores de Caracas) public data. Was made as MVP for the challenge *Zero To One* of *Platzi*.

## Setup
*Create a .env file with the following structure and add your database credentials:*
```
DATABASE_HOST=
DATABASE_NAME=
DATABASE_USER=
DATABASE_PASSWORD=
DATABASE_PORT=
```
*Run the following commands*
```
pip install virtualenv
virtualenv venv
source venv/bin/activate
python manage.py migrate
python manage.py runserver
```