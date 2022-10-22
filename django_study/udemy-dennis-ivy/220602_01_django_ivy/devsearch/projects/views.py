from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def projects(request):
    # return HttpResponse("Here are our products")
    return render(request, 'projects/projects.html')

# pk stands for primary key
def project(request, pk):
    # return HttpResponse(f"A SINGLE PROJECT, you called for {pk}")
    return render(request, 'projects/single-project.html')
