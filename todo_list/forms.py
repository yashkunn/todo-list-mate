from django import forms
from .models import Task, Tag


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["content", "deadline", "tags"]
        widgets = {
            "tags": forms.CheckboxSelectMultiple(),
            "deadline": forms.DateInput(attrs={
                "type": "date",
                "class": "form-control"
            }),
        }

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['tags'].queryset = Tag.objects.all()
