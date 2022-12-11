from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from .forms import CustomUserCreationForm, ProfileForm, SkillForm


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
    messages.info(request, "User was logged out.")
    return redirect("login")


def register_user(request):
    page = "register"
    form = CustomUserCreationForm()
    context = {"page": page, "form": form}

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, "User account was created.")

            login(request, user)
            return redirect("edit-account")
        else:
            messages.error(
                request,
                "Sorry, we found that something is not right in the information in the form.",
            )

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


@login_required(login_url="login")
def user_account(request):
    profile = request.user.profile
    skills = profile.skill_set.all()
    projects = profile.project_set.all()
    context = {
        "profile": profile,
        "projects": projects,
        "skills": skills,
    }
    return render(request, "users/account.html", context)


@login_required(login_url="login")
def edit_account(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("account")

    context = {"form": form}
    return render(request, "users/profile-form.html", context)


@login_required(login_url="login")
def create_skill(request):
    profile = request.user.profile
    if request.method == "POST":
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.owner = profile
            skill.save()
            messages.success(request, "Skill was added successfully.")
            return redirect("account")


    context = {"form": SkillForm()}
    return render(request, "users/skill-form.html", context)


@login_required(login_url="login")
def update_skill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)
    form = SkillForm(instance=skill)
    if request.method == "POST":
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            messages.success(request, "Skill was updated successfully.")
            return redirect("account")

    context = {"form": form}
    return render(request, "users/skill-form.html", context)