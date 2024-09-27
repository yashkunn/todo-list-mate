from django.test import TestCase

from todo_list.forms import TaskForm
from todo_list.models import Tag


class TaskFormTest(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(name="Test Tag")

    def test_task_form_valid(self):
        form_data = {
            "content": "Test Task",
            "deadline": "2024-09-30",
            "tags": [self.tag.id],
        }
        form = TaskForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_task_form_invalid_no_tags(self):
        form_data = {
            "content": "Test Task",
            "deadline": "2024-09-30",
            "tags": [],
        }
        form = TaskForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("tags", form.errors)