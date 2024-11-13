from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = '__all__'
        exclude = ("user",)
        # exclude = ('is_completed', )
        widgets = {'is_completed': forms.HiddenInput()}