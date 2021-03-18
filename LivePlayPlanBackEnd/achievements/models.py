from django.db import models


class Achievement(models.Model):
    ach_name = models.CharField(verbose_name='Название', max_length=20)
    ach_descr = models.TextField(verbose_name='Описание', max_length=80)
    ach_price = models.IntegerField(verbose_name='Цена')

    class Meta:
        verbose_name = 'Достижения'
