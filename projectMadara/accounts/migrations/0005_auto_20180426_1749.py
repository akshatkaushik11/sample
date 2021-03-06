# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-26 17:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20180426_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='custom_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='email',
            field=models.EmailField(blank=True, max_length=255, null=True, unique=True, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='facebook_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='github_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='linkedin_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='reddit_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='twitter_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
