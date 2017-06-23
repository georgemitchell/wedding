# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0003_auto_20170622_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='category',
            field=models.SmallIntegerField(choices=[(0, b'All Categories'), (1, b'Hotels'), (2, b'Bed & Breakfasts'), (3, b'Wineries'), (4, b'Shopping'), (5, b'Food'), (6, b'Attractions')]),
        ),
    ]
