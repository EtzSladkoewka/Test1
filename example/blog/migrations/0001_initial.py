# Generated by Django 3.1.7 on 2021-02-21 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head', models.CharField(max_length=100, verbose_name='Заголовок статьи')),
                ('text', models.TextField(verbose_name='Текст статьи')),
                ('image', models.ImageField(height_field=80, upload_to='', width_field=80)),
            ],
            options={
                'verbose_name': 'Статьи',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comm_name', models.CharField(max_length=30, verbose_name='Имя')),
                ('comm_text', models.TextField(verbose_name='Комментарий')),
                ('article_head', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.article')),
            ],
            options={
                'verbose_name': 'Комментарии',
            },
        ),
    ]
