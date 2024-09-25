from django.test import TestCase
from django.urls import reverse

from todo_list.models import Task, Tag


class TaskViewTest(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(name="Test Tag")
        self.task = Task.objects.create(content="Test Task")
        self.task.tags.add(self.tag)

    def test_index_view(self):
        response = self.client.get(reverse("todo_list:index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "todo_list/index.html")
        self.assertContains(response, "Test Task")

    def test_add_task_view(self):
        response = self.client.get(reverse("todo_list:add-task"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "todo_list/task_form.html")

    def test_update_task_view(self):
        response = self.client.get(reverse("todo_list:update-task", args=[self.task.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "todo_list/task_form.html")

    def test_delete_task_view(self):
        response = self.client.get(reverse("todo_list:delete-task", args=[self.task.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "todo_list/task_confirm_delete.html")


class TagsViewTest(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(name="Test Tag")

    def test_tag_list_view(self):
        response = self.client.get(reverse("todo_list:tag-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "todo_list/tag_list.html")

    def test_create_tag_view(self):
        response = self.client.get(reverse("todo_list:tag-create"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "todo_list/tag_form.html")

    def test_update_tag_view(self):
        response = self.client.get(reverse("todo_list:tag-update", args=[self.tag.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "todo_list/tag_form.html")

    def test_delete_tag_view(self):
        response = self.client.get(reverse("todo_list:tag-delete", args=[self.tag.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "todo_list/tag_confirm_delete.html")
