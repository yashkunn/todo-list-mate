from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from todo_list.views import (
    index,
    AddTaskView,
    TaskUpdateView,
    TaskDeleteView,
    TaskToggleView
)

app_name = "todo_list"

urlpatterns = [
    path("", index, name="index"),
    path("add-task/", AddTaskView.as_view(), name="add-task"),
    path("task/<int:pk>/update/", TaskUpdateView.as_view(), name="update-task"),
    path("task/<int:pk>/delete/", TaskDeleteView.as_view(), name="delete-task"),
    path("task/<int:pk>/toggle/", TaskToggleView.as_view(), name="toggle-task"),
]