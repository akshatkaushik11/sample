# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-18 11:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('write', '0008_auto_20180309_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='toto',
            name='content',
            field=models.TextField(max_length=255),
        ),
    ]
