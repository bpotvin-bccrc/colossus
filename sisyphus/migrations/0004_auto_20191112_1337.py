# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-11-12 21:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sisyphus', '0003_auto_20190809_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analysisrun',
            name='run_status',
            field=models.CharField(choices=[('idle', 'Idle'), ('error', 'Error'), ('running', 'Running'), ('archiving', 'Archiving'), ('complete', 'Complete'), ('align_complete', 'Align Complete'), ('hmmcopy_complete', 'Hmmcopy Complete'), ('annotation_complete', 'Annotation Complete')], default='idle', max_length=50, verbose_name='Run Status'),
        ),
        migrations.AlterField(
            model_name='historicalanalysisrun',
            name='run_status',
            field=models.CharField(choices=[('idle', 'Idle'), ('error', 'Error'), ('running', 'Running'), ('archiving', 'Archiving'), ('complete', 'Complete'), ('align_complete', 'Align Complete'), ('hmmcopy_complete', 'Hmmcopy Complete'), ('annotation_complete', 'Annotation Complete')], default='idle', max_length=50, verbose_name='Run Status'),
        ),
    ]
