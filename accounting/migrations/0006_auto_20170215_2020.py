# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-15 20:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0005_type_programe_type_for'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='day',
            name='user',
        ),
        migrations.RemoveField(
            model_name='month',
            name='user',
        ),
        migrations.RemoveField(
            model_name='year',
            name='user',
        ),
        migrations.RemoveField(
            model_name='program',
            name='day_published',
        ),
        migrations.RemoveField(
            model_name='program',
            name='month_published',
        ),
        migrations.RemoveField(
            model_name='program',
            name='year_published',
        ),
        migrations.DeleteModel(
            name='Day',
        ),
        migrations.DeleteModel(
            name='Month',
        ),
        migrations.DeleteModel(
            name='Year',
        ),
    ]