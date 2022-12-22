from django.shortcuts import render
from django.http import HttpResponse
from .models import Meetup

# Create your views here.
def index(request):
    meetups = Meetup.objects.all()
    context = {
        "show_meetups": True,
        "meetups": meetups,
    }


    return render(request, "meetups/index.html", context)


def meetup_details(request, meetup_slug):
    try:
        meetup = Meetup.objects.get(slug=meetup_slug)
    except Meetup.DoesNotExist as e:
        context = {
            "meetup_found":False
        }
        return render(request, "meetups/meetup-details.html", context)
    else:
        context = {
            "meetup_found":True,
            "meetup":meetup
            }
        return render(request, "meetups/meetup-details.html", context)

