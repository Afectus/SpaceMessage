# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-25 05:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_auto_20180125_0519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tokengenerator',
            name='tokens',
            field=models.CharField(default='RaDA', max_length=255),
        ),
    ]
