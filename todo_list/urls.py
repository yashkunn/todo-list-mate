from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

app_name = "todo_list"

urlpatterns = [
    path("", index, name="index"),
]