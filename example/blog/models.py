from django.db import models


class Article(models.Model):
    head = models.CharField('Заголовок статьи', max_length=100)
    text = models.TextField('Текст статьи')
    image = models.ImageField(null=True, blank=True, upload_to="", height_field=100, width_field=100, verbose_name='Картинка')

    def __str__(self):
        return self.head

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

class Comment(models.Model):
    article_head = models.ForeignKey(Article, on_delete=models.CASCADE)
    comm_name = models.CharField ('Имя', max_length=30)
    comm_text = models.TextField ('Комментарий')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'