# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityPrestaViticole',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=45, null=True)),
                ('description', models.CharField(max_length=255, null=True)),
                ('price_plant_gd', models.DecimalField(null=True, max_digits=10, decimal_places=3)),
                ('price_plant_gs', models.DecimalField(null=True, max_digits=10, decimal_places=3)),
                ('price_ha_gs', models.DecimalField(null=True, max_digits=10, decimal_places=3)),
                ('price_ha_gd', models.DecimalField(null=True, max_digits=10, decimal_places=3)),
                ('creationdate', models.DateTimeField(null=True)),
                ('modificationdate', models.DateTimeField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Benefit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nb', models.FloatField(null=True)),
                ('unit_price', models.DecimalField(null=True, max_digits=10, decimal_places=3)),
                ('unit_type', models.CharField(max_length=45)),
                ('price_with_tax', models.DecimalField(null=True, max_digits=10, decimal_places=3)),
                ('price_without_tax', models.DecimalField(null=True, max_digits=10, decimal_places=0)),
                ('tax', models.DecimalField(null=True, max_digits=10, decimal_places=0)),
                ('creationdate', models.DateTimeField(null=True)),
                ('modificationdate', models.DateTimeField(null=True)),
                ('activity', models.ForeignKey(to='presta_viticoles.ActivityPrestaViticole')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=45, null=True)),
                ('description', models.CharField(max_length=255, null=True)),
                ('siret', models.CharField(max_length=14, null=True)),
                ('phonenumber', models.CharField(max_length=45, null=True)),
                ('mail', models.CharField(max_length=45, null=True)),
                ('cp', models.CharField(max_length=45, null=True)),
                ('city', models.CharField(max_length=45, null=True)),
                ('adresse', models.CharField(max_length=45, null=True)),
                ('country', models.CharField(max_length=45, null=True)),
                ('logo', models.CharField(max_length=45, null=True)),
                ('creationdate', models.DateTimeField(null=True)),
                ('modificationdate', models.DateTimeField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ConfigPrestaViticole',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('guyot', models.IntegerField(null=True)),
                ('superficie', models.IntegerField(null=True)),
                ('plant', models.IntegerField(null=True)),
                ('plant_manquant', models.IntegerField(null=True)),
                ('deplacement', models.IntegerField(null=True)),
                ('pente', models.IntegerField(null=True)),
                ('cepage', models.IntegerField(null=True)),
                ('creationdate', models.DateTimeField(null=True)),
                ('modificationdate', models.DateTimeField(null=True)),
                ('company', models.ForeignKey(to='presta_viticoles.Company')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstname', models.CharField(max_length=45, null=True)),
                ('lastname', models.CharField(max_length=45, null=True)),
                ('phonenumber', models.CharField(max_length=45, null=True)),
                ('mail', models.CharField(max_length=45, null=True)),
                ('cp', models.CharField(max_length=45, null=True)),
                ('city', models.CharField(max_length=45, null=True)),
                ('adresse', models.CharField(max_length=45, null=True)),
                ('country', models.CharField(max_length=45, null=True)),
                ('creationdate', models.DateTimeField(null=True)),
                ('modificationdate', models.DateTimeField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstname', models.CharField(max_length=45, null=True)),
                ('lastname', models.CharField(max_length=45, null=True)),
                ('phonenumber', models.CharField(max_length=45, null=True)),
                ('mail', models.CharField(max_length=45, null=True)),
                ('creationdate', models.DateTimeField(null=True)),
                ('modificationdate', models.DateTimeField(null=True)),
                ('company', models.ForeignKey(to='presta_viticoles.Company')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Estimate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('creationdate', models.DateTimeField(null=True)),
                ('modificationdate', models.DateTimeField(null=True)),
                ('customer', models.ForeignKey(to='presta_viticoles.Customer')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='benefit',
            name='estimate',
            field=models.ForeignKey(to='presta_viticoles.Estimate'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='activityprestaviticole',
            name='company',
            field=models.ForeignKey(to='presta_viticoles.Company'),
            preserve_default=True,
        ),
    ]
