from django.db import models

# Create your models here.
class Work(models.Model):
    organization = models.CharField(verbose_name='Организация', max_length=32)
    region = models.CharField(verbose_name='Регион', max_length=32, blank=True)
    site = models.CharField(verbose_name='Сайт', max_length=64, blank=True)
    sfere = models.CharField(verbose_name='Направление', max_length=16, blank=True)
    position = models.CharField(verbose_name='Должность', max_length=16, blank=True)
    duties = models.TextField(verbose_name='Обязанности', blank=True)
    period = models.PositiveIntegerField(verbose_name='Время работы', blank=True)
    datestart = models.CharField(verbose_name='Дата начала', blank=True, max_length=32)
    dateend = models.CharField(verbose_name='Дата окончания', blank=True, max_length=32)

class Teach(models.Model):
    universitet = models.CharField(verbose_name='Университет', max_length=32)
    specials = models.CharField(verbose_name='Специализация', max_length=32, blank=True)
    site = models.CharField(verbose_name='Сайт', max_length=64, blank=True)
    datestart = models.CharField(verbose_name='Дата поступления', blank=True, max_length=32)
    dateend = models.CharField(verbose_name='Дата окончания', blank=True, max_length=32)