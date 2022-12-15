from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import messages
from .models import Profile

def index(request):
    context = {}
    return render(request, "index.html", context)

def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["password2"]

        if password != password2:
            messages.error(request, "Sorry, the passwords don't match.")
            return redirect("signup")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Sorry, this e-mail was already taken.")
            return redirect("signup")
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Sorry, this username was already taken.")
            return redirect("signup")

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        user_model = User.objects.get(username=username)
        new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
        new_profile.save()
        return redirect("login")


    context = {}
    return render(request, "signup.html", context)


def login(request):
    pass