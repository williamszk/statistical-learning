from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.template.loader import render_to_string

# Should view contain some domain logic?
# and the django html files should contain any logic related to presentation and UI?


monthly_challenges_dict = {
    "january": "Eat no meat for the entire month",
    "february": "Walk for at least 20 minutes everyday",
    "march": "Study Django for at least 20 minutes everyday",
    "april": "Eat no meat for the entire month",
    "may": "Walk for at least 20 minutes everyday",
    "june": "Study Django for at least 20 minutes everyday",
    "july": "Eat no meat for the entire month",
    "august": "Walk for at least 20 minutes everyday",
    "september": "september challenge:Study Django for at least 20 minutes everyday",
    "october": "october challenge: Eat no meat for the entire month",
    "november": "november challenge: Walk for at least 20 minutes everyday",
    "december": None,
}


def monthly_challenge(request, month: str):
    try:
        challenge_text = monthly_challenges_dict[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month": month
        })
        # This dictionary is called context for the template
        # Templaing is server side rendering
        # Django Templeting Engine
    except KeyError as e:
        print(e)
        # return HttpResponseNotFound("<h1>This month is not supported!</h1>")
        # return HttpResponseNotFound(render_to_string("404.html"))
        # Http404 is a class that should be raised and we can write an error message inside of it
        # and it will automatically look for a 404.html file in the root templates directory
        raise Http404()


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges_dict.keys())
    try:
        redirect_month = months[month-1]
    except IndexError as e:
        print(e)
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")

    redirect_path = reverse("month-challenge", args=[redirect_month])

    return HttpResponseRedirect(redirect_path)


def index(request):

    return render(request, "challenges/index.html", {
        "month_list": list(monthly_challenges_dict.keys())
    })