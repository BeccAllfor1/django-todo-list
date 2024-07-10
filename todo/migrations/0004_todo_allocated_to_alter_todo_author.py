# Generated by Django 4.2.13 on 2024-06-21 08:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todo', '0003_alter_todo_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='allocated_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='allocated_todos', to=settings.AUTH_USER_MODEL),   # noqa
        ),
        migrations.AlterField(
            model_name='todo',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='todo', to=settings.AUTH_USER_MODEL),   # noqa
        ),
    ]
