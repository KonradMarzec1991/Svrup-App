# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2019-01-24 01:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_auto_20190123_2229'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecture',
            name='order',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
