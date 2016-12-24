# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-28 16:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tictactoe', '0004_auto_20160528_1848'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='game',
            options={'ordering': ('-last_active',)},
        ),
        migrations.AlterField(
            model_name='game',
            name='status',
            field=models.CharField(choices=[('A', 'Active'), ('F', 'Finished')], default='A', max_length=1),
        ),
    ]
