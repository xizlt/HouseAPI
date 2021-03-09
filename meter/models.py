from django.db import models

from account.models import Profile


class Meter(models.Model):
    name = models.CharField(max_length=10, unique=True)
    type = models.ForeignKey('TypeMeter', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"{self.name}"


class TypeMeter(models.Model):
    title = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.title


class Indication(models.Model):
    meter = models.ForeignKey(Meter, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    value = models.PositiveSmallIntegerField()
    used = models.SmallIntegerField()

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f"{self.meter.name}"


class ItemMeter(models.Model):
    meter = models.ForeignKey(Meter, on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='owen')

    class Meta:
        verbose_name = 'User meter'
        verbose_name_plural = 'User meters'

    def __str__(self):
        return f"{self.meter.name}"
