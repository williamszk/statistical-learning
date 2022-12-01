from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm

projects_list = [
    {
        "id": "1",
        "title": "Ecommerce Website",
        "description": "Fully functional ecommerce website",
    },
    {
        "id": "2",
        "title": "Portfolio Website",
        "description": "A personal website to write articles and display work",
    },
    {
        "id": "3",
        "title": "Social Network",
        "description": "An open source project built by the community",
    },
]


def projects(request):
    # page = "Projects"
    # number = 10
    # context = {
    #     "page": page,
    #     "number": number,
    #     "projects": projects_list,
    # }
    projects = Project.objects.all()
    context = {
        "projects": projects,
    }
    return render(request, "projects/projects.html", context)


def project(request, pk):
    # chosen_project = None
    # for project_item in projects_list:
    #     if project_item["id"] == pk:
    #         chosen_project = project_item
    #         break
    chosen_project = Project.objects.get(id=pk)
    # tags = chosen_project.tags.all()
    context = {
        "project": chosen_project,
        # "tags": tags,
    }
    return render(request, "projects/single-project.html", context)


def create_project(request):
    form = ProjectForm()

    if request.method == "POST":
        form = ProjectForm(request.POST)
        # print(request.POST)
        if form.is_valid():
            form.save()
            # pass the name of the url as a string
            # to where we want to redirect
            return redirect("projects")

    context = {"form": form}
    return render(request, "projects/project-form.html", context)


def update_project(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect("projects")

    context = {"form": form}
    return render(request, "projects/project-form.html", context)


def delete_project(request, pk):
    project = Project.objects.get(id=pk)

    if request.method == "POST":
        project.delete()
        return redirect("projects")

    context = {"object": project}
    return render(request, "projects/delete-template.html", context)
