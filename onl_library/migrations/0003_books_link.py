# Generated by Django 4.0.2 on 2022-02-25 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onl_library', '0002_books_favourites'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='link',
            field=models.CharField(default='Нет данных', max_length=100, verbose_name='Сввязь с автором'),
        ),
    ]