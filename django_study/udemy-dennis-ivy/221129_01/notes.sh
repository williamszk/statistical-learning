
django-admin startproject devsearch
cd devsearch

# create a new app (sub project)
python3 manage.py startapp projects 


# how to run the server
python3 manage.py runserver


# about migrations
python3 manage.py migrate

# about admin panel
python3 manage.py createsuperuser 
admin

# create another user
johndoe
BUCsSzYlObvw5rQ

# after chaning the models.py
# we need to prepare migration and do the proper migration
python3 manage.py makemigrations
# this will create sql commands in the migrations directory

# I had a problem with No changes detected, django
# this link solved it
# https://stackoverflow.com/a/36154224/8782077 
# I need to include the project inside INSTEALLED_APPS in settings.py

# now we run
python3 manage.py migrate
# this will apply the migration in the database

# ===================================================================== #
# Python REPL to interact with the database
# we can pass python code through this shell to the Django backend
python3 manage.py shell

from projects.models import Project
projects = Project.objects.all()
print(projects) # <QuerySet [<Project: Ecommerce Website>, <Project: Portfolio website>, <Project: Mumble social network>, <Project: Yoga Vibe>]>
project_obj = Project.objects.get(title="Portfolio website")
print(project_obj)
print(type(project_obj)) # <class 'projects.models.Project'>
print(project_obj.title) # Portfolio website
print(type(project_obj.title)) # <class 'str'>
print(project_obj.created) # 2022-11-30 02:54:27.938662+00:00

# How to filter records in database
projects = Project.objects.filter(title__startswith="po")
projects # <QuerySet [<Project: Portfolio website>]>

# get all projects that have a voter ration above 50
projects = Project.objects.filter(vote_ratio__gte=50)
projects # <QuerySet [<Project: Portfolio website>, <Project: Yoga Vibe>]>

# get all projects that have vote_ratio less than 50
projects = Project.objects.filter(vote_ratio__lte=50)
projects # <QuerySet [<Project: Ecommerce Website>, <Project: Mumble social network>]>
type(projects)

# get the project Ecommerce Website
projects = Project.objects.get(title="Ecommerce Website")
projects # <Project: Ecommerce Website>
projects.review_set.all()
# found an error:
# AttributeError: 'QuerySet' object has no attribute 'review_set'
# this happened because I forgot to run the get above...
# It would not find the child 

# tags is an attribute of the Model Project
# we can query the many to many relationship as in the below example
projects.tags.all()


# ========================================= 
# get some resources from Dennis Ivanov github
cd static/images
curl -LO https://raw.githubusercontent.com/divanov11/Django-2021/master/static/images/logo.svg
curl -LO https://github.com/divanov11/Django-2021/raw/master/static/images/default.jpg
curl -LO https://github.com/divanov11/Django-2021/raw/master/static/images/yogavive.png
curl -LO https://github.com/divanov11/Django-2021/raw/master/static/images/codesniper.png
cd -

# about collecting static
python3 manage.py collectstatic

# install django whitenoise
pip3 install whitenoise


# ====================================================
# Creating the new app called "users"
python3 manage.py startapp users

python3 manage.py makemigrations

python3 manage.py migrate


# ====================================================

