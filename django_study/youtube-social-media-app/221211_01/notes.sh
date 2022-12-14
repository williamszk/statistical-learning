# install django in virtual environemnt
pip install django

# to create a new django project
django-admin startproject social_book

cd social_book

# create a django app
django-admin startapp core

# to run the server
python3 manage.py runserver

# to make migrations
python3 manage.py makemigrations
python3 manage.py migrate 

python3 manage.py createsuperuser 
admin
1234




