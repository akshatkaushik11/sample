# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-23 09:49
from __future__ import unicode_literals

from django.db import migrations, models
import write.models


class Migration(migrations.Migration):

    dependencies = [
        ('write', '0003_auto_20170922_1249'),
    ]

    operations = [
        migrations.AddField(
            model_name='toto',
            name='photo11',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to=write.models.upload_location, width_field='width_field'),
        ),
        migrations.AddField(
            model_name='toto',
            name='photo12',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to=write.models.upload_location, width_field='width_field'),
        ),
        migrations.AddField(
            model_name='toto',
            name='photo13',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to=write.models.upload_location, width_field='width_field'),
        ),
        migrations.AddField(
            model_name='toto',
            name='photo14',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to=write.models.upload_location, width_field='width_field'),
        ),
        migrations.AddField(
            model_name='toto',
            name='photo15',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to=write.models.upload_location, width_field='width_field'),
        ),
        migrations.AddField(
            model_name='toto',
            name='text11',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='toto',
            name='text12',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='toto',
            name='text13',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='toto',
            name='text14',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='toto',
            name='text15',
            field=models.TextField(blank=True, null=True),
        ),
    ]
