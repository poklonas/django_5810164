# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-15 22:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0009_list_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='list',
            name='date',
        ),
    ]
