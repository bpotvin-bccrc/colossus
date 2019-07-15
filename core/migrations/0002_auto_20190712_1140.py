# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-07-12 18:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
        ('dlp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sublibraryinformation',
            name='library',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dlp.DlpLibrary', verbose_name='Library'),
        ),
        migrations.AddField(
            model_name='sublibraryinformation',
            name='sample_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Sample', verbose_name='Sample_ID'),
        ),
        migrations.AddField(
            model_name='historicalsublibraryinformation',
            name='chip_region',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='core.ChipRegion', verbose_name='Chip_Region'),
        ),
        migrations.AddField(
            model_name='historicalsublibraryinformation',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicalsublibraryinformation',
            name='library',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='dlp.DlpLibrary', verbose_name='Library'),
        ),
        migrations.AddField(
            model_name='historicalsublibraryinformation',
            name='sample_id',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='core.Sample', verbose_name='Sample_ID'),
        ),
        migrations.AddField(
            model_name='historicalsample',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicalmetadatafield',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicaljirauser',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicalchipregionmetadata',
            name='chip_region',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='core.ChipRegion', verbose_name='Chip_Region'),
        ),
        migrations.AddField(
            model_name='historicalchipregionmetadata',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicalchipregionmetadata',
            name='metadata_field',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='core.MetadataField', verbose_name='Metadata key'),
        ),
        migrations.AddField(
            model_name='historicalchipregion',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicalchipregion',
            name='library',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='dlp.DlpLibrary', verbose_name='Library'),
        ),
        migrations.AddField(
            model_name='historicaladditionalsampleinformation',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicaladditionalsampleinformation',
            name='sample',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='core.Sample', verbose_name='Sample'),
        ),
        migrations.AddField(
            model_name='chipregionmetadata',
            name='chip_region',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.ChipRegion', verbose_name='Chip_Region'),
        ),
        migrations.AddField(
            model_name='chipregionmetadata',
            name='metadata_field',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.MetadataField', verbose_name='Metadata key'),
        ),
        migrations.AddField(
            model_name='chipregion',
            name='library',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dlp.DlpLibrary', verbose_name='Library'),
        ),
        migrations.AddField(
            model_name='additionalsampleinformation',
            name='sample',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.Sample', verbose_name='Sample'),
        ),
    ]
