# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-25 12:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hobby',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hobbyname', models.CharField(max_length=32, unique=True, verbose_name='Хобби')),
                ('hobbytext', models.TextField(blank=True, verbose_name='Описание')),
                ('image', models.ImageField(blank=True, upload_to='img')),
            ],
        ),
        migrations.CreateModel(
            name='Teach',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('universitet', models.CharField(max_length=32, unique=True, verbose_name='Университет')),
                ('specials', models.CharField(blank=True, max_length=32, verbose_name='Специализация')),
                ('site', models.CharField(blank=True, max_length=64, verbose_name='Сайт')),
                ('datestart', models.CharField(blank=True, max_length=32, verbose_name='Дата поступления')),
                ('dateend', models.CharField(blank=True, max_length=32, verbose_name='Дата окончания')),
                ('image', models.ImageField(blank=True, upload_to='img')),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization', models.CharField(max_length=32, unique=True, verbose_name='Организация')),
                ('region', models.CharField(blank=True, max_length=32, verbose_name='Регион')),
                ('site', models.CharField(blank=True, max_length=64, verbose_name='Сайт')),
                ('sfera', models.CharField(blank=True, max_length=32, verbose_name='Направление')),
                ('position', models.CharField(blank=True, max_length=32, verbose_name='Должность')),
                ('duties', models.TextField(blank=True, verbose_name='Обязанности')),
                ('period', models.PositiveIntegerField(blank=True, verbose_name='Время работы')),
                ('datestart', models.CharField(blank=True, max_length=32, verbose_name='Дата начала')),
                ('dateend', models.CharField(blank=True, max_length=32, verbose_name='Дата окончания')),
                ('image', models.ImageField(blank=True, upload_to='img')),
            ],
        ),
    ]