# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-11 15:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0004_auto_20170211_1238'),
    ]

    operations = [
        migrations.AddField(
            model_name='type_programe',
            name='type_for',
            field=models.CharField(default='income', max_length=20),
        ),
    ]
