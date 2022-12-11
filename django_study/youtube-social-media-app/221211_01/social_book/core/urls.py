from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("welcome/", views.welcome_django, name="welcome_django"),
]