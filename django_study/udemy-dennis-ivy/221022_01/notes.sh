# https://www.udemy.com/course/python-django-2021-complete-course/learn/lecture/27268008#overview

pip install Django
pip freeze
django-admin

django-admin startproject devsearch
cd devsearch
python3 manage.py runserver


python3 manage.py startapp projects 
cd projects


python3 manage.py migrate
# What does this thing do?
# we need this to create stuff inside the sqlite3 database
# and stop warnings from python3 manage.py runserver
# Operations to perform:
#   Apply all migrations: admin, auth, contenttypes, sessions
# Running migrations:
#   Applying contenttypes.0001_initial... OK
#   Applying auth.0001_initial... OK
#   Applying admin.0001_initial... OK
#   Applying admin.0002_logentry_remove_auto_add... OK
#   Applying admin.0003_logentry_add_action_flag_choices... OK
#   Applying contenttypes.0002_remove_content_type_name... OK
#   Applying auth.0002_alter_permission_name_max_length... OK
#   Applying auth.0003_alter_user_email_max_length... OK
#   Applying auth.0004_alter_user_username_opts... OK
#   Applying auth.0005_alter_user_last_login_null... OK
#   Applying auth.0006_require_contenttypes_0002... OK
#   Applying auth.0007_alter_validators_add_error_messages... OK
#   Applying auth.0008_alter_user_username_max_length... OK
#   Applying auth.0009_alter_user_last_name_max_length... OK
#   Applying auth.0010_alter_group_name_max_length... OK
#   Applying auth.0011_update_proxy_permissions... OK
#   Applying auth.0012_alter_user_first_name_max_length... OK
#   Applying sessions.0001_initial... OK

# to create a admin user in django admin
python3 manage.py createsuperuser 
admin
1234

johndoe
BUCsSzYlObvw5rQ


python3 manage.py makemigrations
# Migrations for 'projects':
#   projects/migrations/0001_initial.py
#     - Create model Project

python3 manage.py migrate
# Operations to perform:
#   Apply all migrations: admin, auth, contenttypes, projects, sessions
# Running migrations:
#   Applying projects.0001_initial... OK

# register model with admin panel

# after including more models
python3 manage.py makemigrations
python3 manage.py migrate
# (.venv) root@d03aa4273aef:~/statistical-learning/django_study/udemy-dennis-ivy/221022_01/devsearch# python3 manage.py makemigrations
# Migrations for 'projects':
#   projects/migrations/0002_tag_project_vote_ratio_project_vote_total_review_and_more.py
#     - Create model Tag
#     - Add field vote_ratio to project
#     - Add field vote_total to project
#     - Create model Review
#     - Add field tags to project
# (.venv) root@d03aa4273aef:~/statistical-learning/django_study/udemy-dennis-ivy/221022_01/devsearch# python3 manage.py migrate
# Operations to perform:
#   Apply all migrations: admin, auth, contenttypes, projects, sessions
# Running migrations:
#   Applying projects.0002_tag_project_vote_ratio_project_vote_total_review_and_more... OK

# register tables in the admin panel

# How to start application?
python3 manage.py runserver



