release: python manage.py makemigrations && python manage.py migrate
web: gunicorn ecommerce.wsgi --log-file -