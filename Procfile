release: python manage.py makemigrations cart && python manage.py makemigrations shop && python manage.py makemigrations orders && python manage.py migrate
web: gunicorn ecommerce.wsgi --log-file -