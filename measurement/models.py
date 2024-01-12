from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название', null=False, unique=True)
    description = models.TextField(null=True, verbose_name='Описание')


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements',)
    temperature = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Температура при измерении')
    datetime = models.DateField(auto_now_add=True, verbose_name='Дата и время измерения')


