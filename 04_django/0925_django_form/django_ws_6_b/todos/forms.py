from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = "__all__"
        # exclude = ("content",)
        widgets = {
            "work": forms.TextInput(attrs={"class": "form-control"}),
            "content": forms.Textarea(attrs={"class": "form-control"}),
            "is_completed": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }
