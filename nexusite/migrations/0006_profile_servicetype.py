# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-28 20:25
from __future__ import unicode_literals

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('nexusite', '0005_auto_20170828_1924'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='servicetype',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Course Tutoring', 'Course Tutoring'), ('College Counseling', 'College Counseling'), ('Standardized Test Preparation', 'Standardized Test Preparation'), ('Other', 'Other')], default=None, max_length=70, null=True),
        ),
    ]
