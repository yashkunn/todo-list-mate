from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from todo_list.models import Task


def index(request: HttpRequest) -> HttpResponse:
    tasks = Task.objects.all().order_by("is_done", "-created_at")
    return render(request, "todo_list/index.html", {"tasks": tasks})


class AddTaskView(generic.CreateView):
    model = Task
    fields = ["content", "deadline"]
    success_url = reverse_lazy("index")
