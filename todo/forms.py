from django import forms
from .models import Todo
from .models import Respond
 
 
class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'details', 'date', 'allocated_to']
        
    def __init__(self, *args, **kwargs):
        super(TodoForm, self).__init__(*args, **kwargs)
        self.fields['allocated_to'].required = True

class RespondForm(forms.ModelForm):
    class Meta:
        model = Respond
        fields = ['todo', 'response_text', ]