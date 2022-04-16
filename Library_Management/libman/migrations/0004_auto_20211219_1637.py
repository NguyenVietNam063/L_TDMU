# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2021-12-19 09:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libman', '0003_auto_20180526_0437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='barcode',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='batch',
            field=models.CharField(choices=[('2017', '2017'), ('2018', '2018'), ('2019', '2019'), ('2020', '2020'), ('2021', '2021')], max_length=4),
        ),
    ]
