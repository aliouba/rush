# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presta_viticoles', '0002_auto_20150204_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configprestaviticole',
            name='cepage',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='configprestaviticole',
            name='deplacement',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='configprestaviticole',
            name='guyot',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='configprestaviticole',
            name='pente',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='configprestaviticole',
            name='plant',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='configprestaviticole',
            name='plant_manquant',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='configprestaviticole',
            name='superficie',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
