# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-28 13:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invitation',
            name='user_from',
        ),
        migrations.RemoveField(
            model_name='invitation',
            name='user_to',
        ),
        migrations.DeleteModel(
            name='Invitation',
        ),
    ]