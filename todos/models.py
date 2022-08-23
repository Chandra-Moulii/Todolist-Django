from asyncio import tasks
from datetime import datetime
from statistics import mode
from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    todo=models.CharField(max_length=200)
    description=models.TextField(blank=True, null=True)
    completed =models.BooleanField(default=False)
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.user.username+" -- "+ self.todo+" -- "+str(self.completed)