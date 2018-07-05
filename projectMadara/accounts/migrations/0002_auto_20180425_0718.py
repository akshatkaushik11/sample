# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-25 07:18
from __future__ import unicode_literals

import accounts.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, height_field='height_field', null=True, upload_to=accounts.models.upload_location, width_field='width_field')),
                ('width_field', models.IntegerField(default=0, null=True)),
                ('height_field', models.IntegerField(default=0, null=True)),
                ('bio', models.TextField(blank=True, max_length=500, null=True)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128)),
                ('status', models.CharField(default='Student', max_length=128)),
                ('totos', models.IntegerField(default=0)),
                ('user_since', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
