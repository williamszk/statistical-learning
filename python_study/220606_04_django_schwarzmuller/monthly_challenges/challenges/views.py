from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello there") 


# Create your views here.
