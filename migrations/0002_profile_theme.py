# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-03 16:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jam', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='theme',
            field=models.CharField(default='cosmo', max_length=16),
        ),
    ]
