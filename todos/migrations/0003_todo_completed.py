# Generated by Django 4.0.5 on 2022-08-18 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0002_alter_todo_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
