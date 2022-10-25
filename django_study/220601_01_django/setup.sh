
# https://www.udemy.com/course/python-django-the-practical-guide/learn/lecture/26372756#overview

pip3 install Django

# installing django will create commands that we'll use
django-admin

# to create a new django project
django-admin startproject mypage

# to start a development server
# we need to be inside the project directory
cd mypage
python3 manage.py runserver

# in a django project we create what are called apps, which are basically modules,
# which are no modules, they are kind of packages

# to create a new app
python3 manage.py startapp challenges



