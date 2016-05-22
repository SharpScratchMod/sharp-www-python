# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sharpsite', '0002_auto_20160522_1541'),
    ]

    operations = [
        migrations.AddField(
            model_name='teamrank',
            name='blocked',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='team',
            name='tid',
            field=models.CharField(unique=True, max_length=100),
        ),
    ]
