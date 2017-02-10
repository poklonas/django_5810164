# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-08 13:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Month',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Pass_book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=60)),
                ('balance', models.IntegerField(default=0)),
                ('founded', models.DateTimeField(verbose_name='data founded')),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head_program', models.CharField(max_length=70)),
                ('detail', models.CharField(max_length=500)),
                ('value', models.IntegerField(default=0)),
                ('day_published', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting.Day')),
                ('month_published', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting.Month')),
                ('pass_book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting.Pass_book')),
            ],
        ),
        migrations.CreateModel(
            name='Type_programe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=20)),
                ('type_detail', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=60)),
                ('founded', models.DateTimeField(verbose_name='date founded')),
            ],
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(default=2017)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting.User')),
            ],
        ),
        migrations.AddField(
            model_name='type_programe',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting.User'),
        ),
        migrations.AddField(
            model_name='program',
            name='type_programe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting.Type_programe'),
        ),
        migrations.AddField(
            model_name='program',
            name='year_published',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting.Year'),
        ),
        migrations.AddField(
            model_name='pass_book',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting.User'),
        ),
        migrations.AddField(
            model_name='month',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting.User'),
        ),
        migrations.AddField(
            model_name='day',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting.User'),
        ),
    ]