# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presta_viticoles', '0003_auto_20150204_1556'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=45, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='activityprestaviticole',
            name='name',
            field=models.ForeignKey(to='presta_viticoles.ActivityGroup'),
            preserve_default=True,
        ),
    ]
