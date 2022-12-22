
python3 -m venv .venv

pip3 install Django
pip3 install tzdata 

# Please, try to not use dashes "-" in names in django
django-admin startproject django_course_site

# create a new app
python3 manage.py startapp meetups

touch meetups/urls.py


# to start running the project
python manage.py runserver

# to migrate database 
python manage.py makemigrations
python manage.py migrate 

# create a new user in admin
python manage.py createsuperuser
admin
1234


