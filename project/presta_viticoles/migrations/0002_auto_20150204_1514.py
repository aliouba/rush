# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presta_viticoles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.FileField(max_length=45, null=True, upload_to=b''),
            preserve_default=True,
        ),
    ]
