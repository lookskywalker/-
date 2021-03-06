# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-06 13:21
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('sid', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('lat', models.DecimalField(decimal_places=3, max_digits=8)),
                ('lon', models.DecimalField(decimal_places=3, max_digits=8)),
                ('inventory', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
            options={
                'ordering': ('sid',),
            },
        ),
    ]
