# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-10 21:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0002_auto_20170210_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pass_book',
            name='balance',
            field=models.FloatField(default=0),
        ),
    ]
