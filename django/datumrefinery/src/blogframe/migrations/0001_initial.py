# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-02-21 06:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(blank=True, max_length=120, null=True)),
                ('lastname', models.CharField(max_length=120)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
