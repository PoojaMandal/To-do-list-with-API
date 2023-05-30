# from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class TaskManager(models.Manager):
    def for_user(self, user):
        return self.filter(user=user)

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='base_tasks', null=True, default=1)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    objects = TaskManager()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']
