from django.contrib import admin
from .models import Todo
from .models import Respond
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Todo)
class PostAdmin(SummernoteModelAdmin):

    list_filter = ('date',)
    summernote_fields = ('details',)

# Register your models here.


admin.site.register(Respond)
