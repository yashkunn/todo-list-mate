from django.urls import path

from todo_list.views import (
    index,
    AddTaskView,
    TaskUpdateView,
    TaskDeleteView,
    TaskToggleView,
    TagListView,
    TagCreate,
    TagUpdate,
    TagDelete
)

app_name = "todo_list"

urlpatterns = [
    path("", index, name="index"),
    path("add-task/", AddTaskView.as_view(), name="add-task"),
    path(
        "task/<int:pk>/update/",
        TaskUpdateView.as_view(),
        name="update-task"
    ),
    path(
        "task/<int:pk>/delete/",
        TaskDeleteView.as_view(),
        name="delete-task"
    ),
    path(
        "task/<int:pk>/toggle/",
        TaskToggleView.as_view(),
        name="toggle-task"
    ),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreate.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", TagUpdate.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagDelete.as_view(), name="tag-delete"),
]
