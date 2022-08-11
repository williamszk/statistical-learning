from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render

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
        return HttpResponse(challenge_text)
    except KeyError as e:
        print(e)
        return HttpResponseNotFound("This month is not supported!")


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges_dict.keys())
    try:
        redirect_month = months[month-1]
    except IndexError as e:
        print(e)
        return HttpResponseNotFound("This month is not supported!")

    return HttpResponseRedirect(f"/challenges/{redirect_month}")
