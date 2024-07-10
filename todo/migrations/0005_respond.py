# Generated by Django 4.2.13 on 2024-07-02 14:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todo', '0004_todo_allocated_to_alter_todo_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Respond',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),  # noqa
                ('response_text', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='responses', to=settings.AUTH_USER_MODEL)),  # noqa
                ('todo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='responses', to='todo.todo')),  # noqa
            ],
        ),
    ]
