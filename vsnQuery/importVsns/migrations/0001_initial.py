# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VSNData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Indexed_SNP', models.CharField(max_length=100)),
                ('SerialNumberPattern', models.CharField(max_length=12)),
                ('VehicleTrimId', models.IntegerField()),
                ('Year', models.IntegerField()),
                ('Make', models.CharField(max_length=3)),
                ('Model', models.CharField(max_length=200)),
                ('TrimName', models.CharField(max_length=20)),
            ],
        ),
    ]
