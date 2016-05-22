# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sharpsite', '0003_auto_20160522_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teamrankpermission',
            name='rank',
            field=models.OneToOneField(to='sharpsite.TeamRank'),
        ),
    ]
