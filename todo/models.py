from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User




# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="todos", default=1
    )

 
    def __str__(self):
        return self.title


    