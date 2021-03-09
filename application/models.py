from django.contrib.auth.models import User
from django.db import models

from account.models import Profile


class Application(models.Model):
    title = models.CharField(max_length=200)
    type = models.ForeignKey('TypeApplication', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    due_data = models.DateTimeField()
    executed = models.BooleanField(default=False)
    mark = models.TextField(max_length=2000, blank=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title


class TypeApplication(models.Model):
    title = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.title

