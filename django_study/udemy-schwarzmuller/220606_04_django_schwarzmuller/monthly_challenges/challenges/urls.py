from django.urls import path
from . import views

# this will define what is called a URLconf
urlpatterns = [
    path("january", views.index),
]