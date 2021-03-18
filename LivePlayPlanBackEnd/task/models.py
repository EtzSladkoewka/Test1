from django.db import models


class Task(models.Model):
    task_descr = models.CharField(max_length=300, verbose_name='Описание')
    task_time = models.DateTimeField(verbose_name='Срок')
