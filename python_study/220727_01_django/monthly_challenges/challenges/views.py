from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

def monthly_challenge(request, month):
    challenge_text = None
    if month == "january":
        challenge_text = "This works!"
    elif month == "february":
        challenge_text = "Walk for at least 20 minutes everyday"
    elif month == "march":
        challenge_text = "This is the march challenge"
    else:
        return HttpResponseNotFound("This month is not supported")


    return HttpResponse(challenge_text)
