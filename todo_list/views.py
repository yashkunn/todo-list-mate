from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from todo_list.models import Task


def index(request: HttpRequest) -> HttpResponse:
    tasks = Task.objects.all().order_by("is_done", "-created_at")
    return render(request, "todo_list/index.html", {"tasks": tasks})


class AddTaskView(generic.CreateView):
    model = Task
    fields = ["content", "deadline"]
    success_url = reverse_lazy("todo_list:index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = ["content", "deadline", "is_done"]
    success_url = reverse_lazy("todo_list:index")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo_list:index")


class TaskToggleView(generic.View):
    def post(self, request: HttpRequest, pk: int) -> HttpResponse:
        task = Task.objects.get(pk=pk)
        task.is_done = not task.is_done
        task.save()
        return redirect("todo_list:index")
