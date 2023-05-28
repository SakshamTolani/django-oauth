# CALENDAR EVENTS WITH DJANGO REST FRAMEWORK
[Django REST framework](http://www.django-rest-framework.org/) is a powerful and flexible toolkit for building Web APIs.

## Requirements
- Python 3.9.6
- Django 4.0.6
- Django REST Framework 3.13.1
- Google Auth 2.9.1
- Google API Python client 2.53.0

## Quick Start

- Fork and Clone the repository using-
```
git clone https://github.com/SakshamTolani/django-oauth
```
- Create a Branch- 
```
git checkout -b <branch_name>
```
- Create virtual environment-
```
python -m venv env
env\Scripts\activate
```
- Install dependencies using-
```
pip install -r requirements.txt
```
*If you have python2 and python3 installed you need to specify python3 by using command:*
```
python3 -m pip install -r requirements.txt
```

- Headover to Project Directory- 
```
cd backend
```
- Make migrations using-
```
python manage.py makemigrations
```
*If you have python2 and python3 installed you need to specify python3 by using command:*
```
python3 manage.py makemigrations
```

- Migrate Database-
```
python manage.py migrate
```
- Create a superuser-
```
python manage.py createsuperuser
```
- Create a project on https://console.google.com/ and fill up the required details related to OAuth Consent Screen and for Credentils.
- Download or copy .json file of credentials and paste it in the "credentials.json" file located in 
```
backend / base / credentials.json
```

- Run server using-
```
python manage.py runserver
```

## Structure
In a RESTful API, endpoints (URLs) define the structure of the API and how end users access data from our application using the HTTP methods - GET, POST, PUT, DELETE. Endpoints should be logically organized around _collections_ and _elements_, both of which are resources.

In our case, we have one single resource, `calendar`, so we will use the following URLS - `/rest/calendar/v1/init` and `/rest/calendar/v1/redirect` for collections and elements, respectively:

Endpoint |HTTP Method | CRUD Method | Result
-- | -- |-- |--
`/rest/calendar/v1/init` | GET | READ | Initializes OAuth by asking user their credentials
`/rest/calendar/v1/redirect` | GET | READ | Handles redirect request for above url and get all the events through user's calendar. 

### Commands
```
Authorize your google account
http http://127.0.0.1:8000/rest/calendar/v1/init/

Redirected to this page which has events for user
http GET http://127.0.0.1:8000/rest/calendar/v1/redirect/

```

> Made with ❤️ by Saksham Tolani




[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)  [![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)


