from django.shortcuts import render

projects_list = [
    {
        'id': '1',
        'title': 'Ecommerce Website',
        'description': 'Fully functional ecommerce website'
    },
    {
        'id': '2',
        'title': 'Portfolio Website',
        'description': 'A personal website to write articles and display work'
    },
    {
        'id': '3',
        'title': 'Social Network',
        'description': 'An open source project built by the community'
    }
]



def projects(request):
    page = "Projects"
    number = 10
    context = {
        "page": page,
        "number": number,
        "projects": projects_list,
    }
    return render(request, "projects/projects.html", context)

def project(request, pk):
    chosen_project = None
    for project_item in projects_list:
        if project_item["id"] == pk:
            chosen_project = project_item
            break

    context = {
        "project": chosen_project,
    }
    return render(request, "projects/single-project.html", context)