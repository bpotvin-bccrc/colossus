# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-09-11 21:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenx', '0006_auto_20190909_1630'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicaltenxlibrary',
            name='gsc_library_id',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='GSC Library ID'),
        ),
        migrations.AddField(
            model_name='tenxlibrary',
            name='gsc_library_id',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='GSC Library ID'),
        ),
    ]
