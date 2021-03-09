from django.db import models


class ParameterType(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.title


class Parameter(models.Model):
    title = models.ForeignKey(ParameterType, on_delete=models.CASCADE)
    value = models.SmallIntegerField()

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.title.title)

class HotWater(Parameter):
    class Meta:
        verbose_name = 'Горячая вода'
        verbose_name_plural = 'Горячая вода'


class CoolWater(Parameter):
    class Meta:
        verbose_name = 'Холодная вода'
        verbose_name_plural = 'Холодная вода'


class Gas(Parameter):
    class Meta:
        verbose_name = 'Газ'
        verbose_name_plural = 'Газ'


class ElectroDay(Parameter):
    class Meta:
        verbose_name = 'Электричество день'
        verbose_name_plural = 'Электричество день'


class ElectroNight(Parameter):
    class Meta:
        verbose_name = 'Электричество ночь'
        verbose_name_plural = 'Электричество ночь'
