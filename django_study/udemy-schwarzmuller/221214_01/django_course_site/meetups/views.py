from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("<p>Hi there</p>")
    meetups = [
        {
            "title": "How to create a famous programming language?",
            "location": "Amsterdam",
            "slug": "the-amsterdam-first-meetup",
        },
        {
            "title": "The capital is sinking!",
            "location": "Jakarta",
            "slug": "the-indonesia-meetup-to-make-capitals",
        },
    ]
    context = {
        "show_meetups": True,
        "meetups": meetups,
    }
    return render(request, "meetups/index.html", context)
