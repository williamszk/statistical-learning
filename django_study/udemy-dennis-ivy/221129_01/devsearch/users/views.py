from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from .forms import CustomUserCreationForm


def login_user(request):
    # print(f"{request.method = }")
    # print(f"{request.POST = }")
    page = "login"
    context = {
        "page": page,
    }

    if request.user.is_authenticated:
        # In case the authenticated user is trying to
        # access the login page again.
        return redirect("profiles")

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        try:
            user = User.objects.get(username=username)
        except Exception as e:
            print(e)
            messages.error(request, "Username does not exist.")
            # print("Username does not exist.")
        else:
            user = authenticate(request, username=username, password=password)
            if user:
                # this creates a session in the session table
                # and creates a cookie
                login(request, user)
                return redirect("profiles")
            else:
                messages.error(request, "Username OR password is incorrect.")
                # print("Username OR password is incorrect.")
    return render(request, "users/login-register.html", context)


def logout_user(request):
    logout(request)
    messages.error(request, "User was logged out.")
    return redirect("login")


def register_user(request):
    page ="register"
    form = CustomUserCreationForm()
    context = {"page":page, "form": form}

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, "User account was created.")

            login(request, user)
            return redirect('profiles')
        else:
            messages.success(request, "Sorry, we found that something is not right in the form's information.")

    return render(request, "users/login-register.html", context)


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
