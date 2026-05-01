from django.shortcuts import render, redirect
from .models import Project
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    projects = Project.objects.filter(members=request.user)
    return render(request, "dashboard.html", {"projects": projects})

def create_project(request):
    if request.method == "POST":
        name = request.POST.get('name')
        desc = request.POST.get('description')

        project = Project.objects.create(
            name=name,
            description=desc,
            owner=request.user
        )
        project.members.add(request.user)

        return redirect('dashboard')

    return render(request, 'create_project.html')