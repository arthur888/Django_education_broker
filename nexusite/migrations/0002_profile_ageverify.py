# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-28 16:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nexusite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='ageverify',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
    ]