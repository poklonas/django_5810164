# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-03 07:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0015_imported_csv_pass_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imported_csv',
            name='csv_file',
            field=models.FileField(upload_to='./accounting/media/imported_csv/'),
        ),
    ]