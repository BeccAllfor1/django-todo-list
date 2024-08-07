from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings
from cloudinary.models import CloudinaryField

# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="todo")
    allocated_to = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="allocated_todos",
        null=True, blank=True
    )

    def __str__(self):
        return self.title


class Respond(models.Model):
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE,
                             related_name='responses')
    response_text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name="responses")

    def __str__(self):
        return f'Response to {self.todo.title} by {self.author.username}'
