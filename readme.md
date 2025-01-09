---INSTRUCTIONS---

Create virtual enviroment

To run the backend:
enter the environment: .venv\Scripts\activate

The installs needed:
pip install djangorestframework
pip install django
pip install Pillow(might not be needed, you could try without first)   

Before running the server, make sure that the database is running. (Google Cloud)

migrate if needed: python manage.py migrate  
start server: python manage.py runserver




Use the following url pattern to access the backend:

http://127.0.0.1:8000/admin/  
http://127.0.0.1:8000/api/carts/#id/ (#id is the id of the cart you want access to. Dont include id if you only want a list of carts)  
http://127.0.0.1:8000/api/cart-items/#id/  
http://127.0.0.1:8000/api/tvs/#id/  
http://127.0.0.1:8000/api/reviews/#id/  
