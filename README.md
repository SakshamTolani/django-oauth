# PAYMENT GATEWAY WITH DJANGO REST FRAMEWORK
[Django REST framework](http://www.django-rest-framework.org/) is a powerful and flexible toolkit for building Web APIs.

## Requirements
- Python 3.9.6
- Django 4.1.5
- Django REST Framework 3.14.0

## Quick Start

- Fork and Clone the repository using-
```
git clone https://github.com/SakshamTolani/payment-gateway
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
- Run server using-
```
python manage.py runserver
```

## Structure
In a RESTful API, endpoints (URLs) define the structure of the API and how end users access data from our application using the HTTP methods - GET, POST, PUT, DELETE. Endpoints should be logically organized around _collections_ and _elements_, both of which are resources.

In our case, we have one single resource, `orders`, so we will use the following URLS - `/api/` and `/api/<order_id>` for collections and elements, respectively:

Endpoint |HTTP Method | CRUD Method | Result
-- | -- |-- |--
`api/` | GET | READ | Get all orders
`api/:order_id/` | GET | READ | Get order by order-id
`api/createOrder/`| POST | CREATE | Create a new order
`api/:order_id/paymentStatus/` | GET | READ | Get Payment Details by order-id
`api/:order_id/paymentStatus/success/` | PUT | UPDATE | Update payment to success using order-id
`api/:order_id/paymentStatus/failure/` | PUT | UPDATE | Update payment to failure using order-id

### Commands
```
Get all orders
http http://127.0.0.1:8000/api/
Get order by order-id
http GET http://127.0.0.1:8000/api/{order_id}/
Create a new order
http POST http://127.0.0.1:8000/api/createOrder/ "order_id":"ORD265", "order_amount":2000, "customer_name":"Spiderman"
Get Payment Details by order-id
http GET http://127.0.0.1:8000/api/{order_id}/paymentStatus/ 
Update payment to success using order-id
http PUT http://127.0.0.1:8000/api/{order_id}/paymentStatus/success/
Update payment to failure using order-id
http PUT http://127.0.0.1:8000/api/{order_id}/paymentStatus/failure/ 
```

> Made with ❤️ by Saksham Tolani




[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)  [![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)


