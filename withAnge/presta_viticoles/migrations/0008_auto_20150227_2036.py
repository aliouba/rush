# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presta_viticoles', '0007_auto_20150227_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activityprestaviticole',
            name='group',
            field=models.ForeignKey(related_query_name=b'group', related_name='groups', to='presta_viticoles.ActivityGroup'),
            preserve_default=True,
        ),
    ]
