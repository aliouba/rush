# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presta_viticoles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='activityprestaviticole',
            name='group',
            field=models.ForeignKey(default=1, to='presta_viticoles.ActivityGroup'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='activityprestaviticole',
            name='name',
            field=models.CharField(max_length=255, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='company',
            name='adresse',
            field=models.CharField(max_length=45, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='company',
            name='city',
            field=models.CharField(max_length=45, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='company',
            name='country',
            field=models.CharField(max_length=45, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='company',
            name='cp',
            field=models.CharField(max_length=45, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='company',
            name='description',
            field=models.CharField(max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.FileField(max_length=45, null=True, upload_to=b'', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='company',
            name='mail',
            field=models.CharField(max_length=45, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='company',
            name='phonenumber',
            field=models.CharField(max_length=45, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='company',
            name='siret',
            field=models.CharField(max_length=14, null=True, blank=True),
            preserve_default=True,
        ),
    ]
