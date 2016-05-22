# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sharpsite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='tid',
            field=models.CharField(max_length=100, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teamrank',
            name='guest',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teamrank',
            name='invited',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
