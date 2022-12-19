from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("<p>Hi there</p>") 
    meetups = [
        {"title":"A first meetup"},
        {"title":"A Second meetup"},
    ]
    context = {
        "show_meetups": True,
        "meetups": meetups,
    }
    return render(request, "meetups/index.html", context)