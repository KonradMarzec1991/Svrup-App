# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2019-01-23 20:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0005_video_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='free',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='video',
            name='member_required',
            field=models.BooleanField(default=False),
        ),
    ]
