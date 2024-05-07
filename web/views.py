from django.shortcuts import render
from .models import *
from .form import *

# Create your views here.

def index(request):
    
    return render(request,"index.html")

def projects(request):
    projects = Projects.objects.all()
    context = {
        "projects": projects,
    }
    
    return render(request,"projects.html",context)