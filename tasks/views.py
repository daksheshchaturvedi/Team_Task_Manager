from django.shortcuts import redirect
from .models import Task
from projects.models import Project
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def update_task(request):
    if request.method == "POST":
        body = json.loads(request.body)

        task_id = body.get("task_id")
        status = body.get("status")

        task = Task.objects.get(id=task_id)
        task.status = status
        task.save()

        return JsonResponse({"success": True})

@csrf_exempt
def create_task(request):
    if request.method == "POST":
        data = json.loads(request.body)

        title = data.get("title")
        project_id = data.get("project_id")

        project = Project.objects.get(id=project_id)

        task = Task.objects.create(
            title=title,
            project=project,
            status="TODO"
        )

        return JsonResponse({
            "id": task.id,
            "title": task.title,
            "status": task.status
        })


def update_task_status(request, task_id, status):
    task = Task.objects.get(id=task_id)
    task.status = status
    task.save()

    return redirect("dashboard")

def get_tasks(request, project_id):
    tasks = Task.objects.filter(project_id=project_id)

    data = []
    for task in tasks:
        data.append({
            "id": task.id,
            "title": task.title,
            "status": task.status,
        })

    return JsonResponse(data, safe=False)