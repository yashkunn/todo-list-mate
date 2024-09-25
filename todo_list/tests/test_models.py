from django.test import TestCase
from django.utils import timezone

from todo_list.models import Task, Tag


class TagModelTest(TestCase):
    def test_tag_str(self):
        tag = Tag.objects.create(name="Test Tag")
        self.assertEqual(str(tag), "Test Tag")

    def test_tag_creation(self):
        tag = Tag.objects.create(name="New Tag")
        self.assertEqual(tag.name, "New Tag")

class TaskModelTest(TestCase):
    def test_task_str(self):
        task = Task.objects.create(content="Test Task")
        self.assertEqual(str(task), "Test Task")

    def test_task_creation(self):
        deadline_date = timezone.datetime(2024, 9, 30)
        task = Task.objects.create(content="New Task", deadline=deadline_date)
        self.assertEqual(task.content, "New Task")
        self.assertEqual(task.deadline.strftime("%Y-%m-%d"), "2024-09-30")
        self.assertFalse(task.is_done)

    def test_task_with_tags(self):
        tag1 = Tag.objects.create(name="Tag 1")
        tag2 = Tag.objects.create(name="Tag 2")
        task = Task.objects.create(content="Task with Tags")
        task.tags.add(tag1, tag2)
        self.assertEqual(task.tags.count(), 2)
        self.assertIn(tag1, task.tags.all())
        self.assertIn(tag2, task.tags.all())
