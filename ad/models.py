from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from account.models import Profile


class Ad(models.Model):
    title = models.CharField(max_length=200)
    type = models.ForeignKey('TypeAd', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    beginning = models.DateTimeField(default=timezone.now)
    ending = models.DateTimeField(blank=True, null=True)
    text = models.TextField(max_length=2000)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='profile', blank=True, null=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title


class TypeAd(models.Model):
    title = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.title
