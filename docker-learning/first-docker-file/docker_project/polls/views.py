from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return render(request,'../docker_project/templates/docker_project.html')

# Create your views here.
