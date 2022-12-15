from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile

@login_required(login_url="signin")
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

        user = User.objects.create_user(
            username=username, email=email, password=password
        )
        user.save()

        user_model = User.objects.get(username=username)
        new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
        new_profile.save()
        return redirect("login")

    context = {}
    return render(request, "signup.html", context)


def signin(request):
    context = {}
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        try:
            user = User.objects.get(username=username)
        except Exception as e:
            messages.error(request, f"Sorry, we couldn't find the user username: '{username}'.")
        else:
            user = authenticate(request, username=username, password=password)
            # user is None if either username or password is incorrect
            if user:
                login(request, user)
                return redirect("index")
            else:
                messages.error(request, "Sorry, either 'username' or 'password' is incorrect.")
                return redirect("signin")

    # This will only run if the method is not POST
    return render(request, "signin.html", context)

@login_required(login_url="signin")
def logout_user(request):
    logout(request)
    messages.error(request, f"User was logged out.")
    return redirect("signin")