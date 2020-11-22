from django import forms
from django.forms import ModelForm

from .models import Task

# naming convention: name of class+Form

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = '__all__'
        # para di tayo gagawa ng mano manong forms