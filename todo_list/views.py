from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from todo_list.models import Task


def index(request: HttpRequest) -> HttpResponse:
    tasks = Task.objects.all().order_by("is_done", "-created_at")
    return render(request, "todo_list/index.html", {"tasks": tasks})
