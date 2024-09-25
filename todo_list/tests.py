from django.forms import forms
from django.test import TestCase
from .forms import TaskForm
from .models import Task, Tag


class TaskFormTest(TestCase):
    def setUp(self):
        self.tag1 = Tag.objects.create(name="Work")
        self.tag2 = Tag.objects.create(name="Personal")

    def test_task_form_valid(self):
        form_data = {
            "content": "Test Task",
            "deadline": "2023-12-31",
            "tags": [self.tag1.id, self.tag2.id]
        }
        form = TaskForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_task_form_fields(self):
        form = TaskForm()
        self.assertIn("content", form.fields)
        self.assertIn("deadline", form.fields)
        self.assertIn("tags", form.fields)
        self.assertIsInstance(form.fields["tags"].widget, forms.CheckboxSelectMultiple)
        self.assertEqual(form.fields["deadline"].widget.attrs["type"], "date")
        self.assertEqual(form.fields["deadline"].widget.attrs["class"], "form-control")

    def test_task_form_queryset(self):
        form = TaskForm()
        self.assertQuerysetEqual(
            form.fields["tags"].queryset,
            Tag.objects.all(),
            transform=lambda x: x
        )