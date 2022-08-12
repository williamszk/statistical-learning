from urllib import response
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

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
    "december": "december challenge:  Study Django for at least 20 minutes everyday",
}


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges_dict[month]

        response_data = f"<h1>{challenge_text}</h1>"

        return HttpResponse(response_data)
    except KeyError as e:
        print(e)
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")


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
    # response_data = """
    # <ul>
    #     <li><a href="/challenges/january">January</a></li>
    #     <li><a href="/challenges/february">february</a></li>
    #     <li><a href="/challenges/march">march</a></li>
    #     <li><a href="/challenges/april">april</a></li>
    #     <li><a href="/challenges/may">may</a></li>
    #     <li><a href="/challenges/june">june</a></li>
    #     <li><a href="/challenges/july">july</a></li>
    #     <li><a href="/challenges/august">august</a></li>
    #     <li><a href="/challenges/september">september</a></li>
    #     <li><a href="/challenges/october">october</a></li>
    #     <li><a href="/challenges/november">november</a></li>
    #     <li><a href="/challenges/december">december</a></li>
    # </ul>
    # """

    response_data = "<ul>"+"".join(
        [f"<li><a href=\"/challenges/{month}\">{month}</a></li>"
         for month in monthly_challenges_dict.keys()]) +\
        "</ul>"

    return HttpResponse(response_data)
