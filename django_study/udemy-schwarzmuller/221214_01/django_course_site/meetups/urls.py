from django.urls import path
from . import views


urlpatterns = [
    path("meetups/", views.index, name="meetups"),
    path("meetup-details/", views.meetup_details, name="meetup-details"),
]