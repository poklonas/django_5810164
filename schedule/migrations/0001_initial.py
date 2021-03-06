# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-03 07:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_left', models.IntegerField(default=0)),
                ('connected', models.BooleanField(default=False)),
                ('detail', models.CharField(default='', max_length=100)),
                ('time', models.IntegerField(default=0)),
                ('day', models.CharField(default='Monday', max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.AddField(
            model_name='activity',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.User'),
        ),
    ]
