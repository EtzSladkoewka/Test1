from django.db import models


class User(models.Model):
    us_first_name = models.CharField(verbose_name='Имя', max_length=20)
    us_second_name = models.CharField(verbose_name='Фамилия', max_length=20, blank=True)
    us_coin = models.IntegerField(verbose_name='Монеты')
    us_exp = models.IntegerField(verbose_name='Опыт')
    us_lvl = models.IntegerField(verbose_name='Уровень')
    us_avatar = models.ImageField(verbose_name='Изображение', upload_to="")

    class Meta:
        verbose_name = 'Профиль'
