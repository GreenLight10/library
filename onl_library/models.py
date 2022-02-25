from turtle import title
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.


class Books(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название книги')
    slug = models.SlugField()
    author = models.CharField(
        max_length=100, default='Автор не указан', verbose_name='Автор книги')
    description = models.TextField(
        verbose_name='Описание', default='Описание появится позже')
    pub_date = models.DateField(verbose_name='Дата публикации')
    pdf_book = models.FileField(upload_to='pdfs/', verbose_name='Файл книги')
    link = models.CharField(max_length=100, default='Нет данных', verbose_name='Сввязь с автором')
    image = models.ImageField(
        upload_to='images/covers/', null=True, blank=True)
    favourites = models.ManyToManyField(User, verbose_name='favourites', default=None, blank=True)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('book_detail', kwargs={'book_slug': self.slug})

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
