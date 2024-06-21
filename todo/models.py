from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User





# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="todo")

    allocated_to = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="allocated_todos", null=True, blank=True
    )    
    

 
    def __str__(self):
        return self.title


    
    