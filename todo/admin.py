from django.contrib import admin
from .models import Todo
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Todo)
class PostAdmin(SummernoteModelAdmin):


    summernote_fields = ('details',)

# Register your models here.
