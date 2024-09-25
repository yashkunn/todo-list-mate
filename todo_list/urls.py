from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from todo_list.views import index, AddTaskView

app_name = "todo_list"

urlpatterns = [
    path("", index, name="index"),
    path("add-task/", AddTaskView.as_view(), name="add-task"),
]