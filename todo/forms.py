from django import forms
from .models import Todo
from .models import Respond
 
 
class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'details', 'date', 'allocated_to']


class RespondForm(forms.ModelForm):
    class Meta:
        model = Respond
        fields = ['todo', 'response_text', ]