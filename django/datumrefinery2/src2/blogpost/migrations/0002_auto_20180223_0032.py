# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-02-22 15:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogpost', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=400),
        ),
    ]
