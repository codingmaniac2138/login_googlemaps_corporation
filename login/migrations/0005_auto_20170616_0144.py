# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-16 01:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_auto_20170616_0135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
