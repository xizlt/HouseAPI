from django.db import models

from account.models import Profile


class Meter(models.Model):
    name = models.CharField("Название", max_length=10, unique=True)
    type = models.ForeignKey('TypeMeter', on_delete=models.CASCADE, verbose_name="Тип")
    created = models.DateTimeField("Создано", auto_now_add=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Счетчик'
        verbose_name_plural = 'Счетчики'

    def __str__(self):
        return f"{self.name}"


class TypeMeter(models.Model):
    title = models.CharField("Название", max_length=200, unique=True)

    class Meta:
        verbose_name = 'Тип счетчика'
        verbose_name_plural = 'Типы счетчиков'

    def __str__(self):
        return self.title


class Indication(models.Model):
    meter = models.ForeignKey(Meter, on_delete=models.CASCADE, verbose_name="Счетчик")
    created = models.DateTimeField("Создано", auto_now_add=True)
    value = models.PositiveSmallIntegerField("Показание")
    used = models.SmallIntegerField("Потреблено")

    class Meta:
        ordering = ['-created']
        verbose_name = 'Показание'
        verbose_name_plural = 'Покозания'

    def __str__(self):
        return f"{self.meter.name}"


class ItemMeter(models.Model):
    meter = models.ForeignKey(Meter, on_delete=models.CASCADE, verbose_name="Счетчик")
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='owen', verbose_name="Пользователь")

    class Meta:
        verbose_name = 'Владелец счетчика'
        verbose_name_plural = 'Владелецы счетчиков'

    def __str__(self):
        return f"{self.meter.name}"
