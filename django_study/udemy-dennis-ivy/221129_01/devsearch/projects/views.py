from django.shortcuts import render

# Create your views here.


def projects(request):
    # return HttpResponse("Here are some products.")
    return render(request, "projects/projects.html")

def project(request, pk):
    # return HttpResponse(f"Here is your specific project. With id {pk}.")
    return render(request, "projects/single-project.html")