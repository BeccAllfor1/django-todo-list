from django import forms
from .models import Todo
 
 
class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'details', 'date', 'allocated_to']
