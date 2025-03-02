from django.db import models

# Create your models here.
class Articles(models.Model):
    title = models.CharField('Название', max_length=50, default='Без названия')
    anons = models.CharField('Анонс', max_length=150)
    text = models.TextField('Текст')
    date = models.DateTimeField('Дата публикации', default = '')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'