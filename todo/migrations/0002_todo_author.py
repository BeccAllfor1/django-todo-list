# Generated by Django 4.2.13 on 2024-06-19 12:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='author',
            field=models.ForeignKey(default=1,
                                    on_delete=django.db.models.deletion.CASCADE,  # noqa
                                    related_name='todos',
                                    to=settings.AUTH_USER_MODEL),
        ),
    ]
