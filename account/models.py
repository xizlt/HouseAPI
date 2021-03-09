from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    status = models.ForeignKey('Status', on_delete=models.CASCADE, blank=True, null=True)

    phone = models.IntegerField(blank=True, null=True)
    city = models.CharField(default="Санкт-Петербург", max_length=100)
    street = models.CharField(max_length=100, default="Невский")
    house = models.PositiveSmallIntegerField(default=100)
    flat = models.PositiveSmallIntegerField(blank=True, null=True)

    ban = models.BooleanField(default=False)
    ban_start = models.DateField(blank=True, null=True)
    ban_end = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.user.username


class Status(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title
