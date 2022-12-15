
python3 -m venv .venv

pip3 install Django
pip3 install tzdata 

# Please, try to not use dashes "-" in names in django
django-admin startproject django_course_site

# create a new app
python3 manage.py startapp meetups

touch meetups/urls.py


# to start running the project
python3 manage.py runserver



