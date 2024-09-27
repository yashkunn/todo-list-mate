from django.contrib import admin
from .models import Tag, Task


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("id", "content", "created_at", "is_done")
    list_filter = ("is_done", "created_at")
    search_fields = ("content",)
    prepopulated_fields = {"content": ("content",)}