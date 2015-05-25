# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='area',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('locality_id', models.IntegerField()),
                ('locality_name', models.CharField(max_length=40)),
                ('city', models.CharField(max_length=30)),
                ('latitude', models.DecimalField(max_digits=11, decimal_places=8)),
                ('longitude', models.DecimalField(max_digits=11, decimal_places=8)),
                ('added_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
