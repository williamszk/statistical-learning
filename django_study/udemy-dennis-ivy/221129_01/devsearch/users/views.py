from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from .models import Profile


def login_user(request):
    print(f"{request.method = }")
    print(f"{request.POST = }")
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        try:
            user = User.objects.get(username=username)
        except Exception as e:
            print(e)
            print("Username does not exist.")
            # there should be a return in here

        user = authenticate(request, username=username,password=password)
        if user:
            # this creates a session in the session table
            # and creates a cookie
            login(request, user)
            return redirect("profiles")
        else:
            print("Username OR password is incorrect.")
    return render(request,"users/login-register.html")

def logout_user(request):
    logout(request)
    return redirect("login")


# Create your views here.
def profiles(request):
    profiles = Profile.objects.all()
    context = {"profiles": profiles}
    return render(request, "users/profiles.html", context)


def user_profile(request, pk):
    profile = Profile.objects.get(id=pk)

    top_skills = profile.skill_set.exclude(description__exact="")
    other_skills = profile.skill_set.filter(description="")

    context = {
        "profile": profile,
        "top_skills": top_skills,
        "other_skills": other_skills,
    }
    return render(request, "users/user-profile.html", context)
