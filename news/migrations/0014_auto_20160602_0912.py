# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-02 06:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0013_auto_20160531_2252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='is_published',
            field=models.BooleanField(default=False, verbose_name='Опубликовать?'),
        ),
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='article_set', to='news.Tag'),
        ),
    ]
