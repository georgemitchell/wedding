# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0002_destination_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='latitude',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=7, blank=True),
        ),
        migrations.AddField(
            model_name='destination',
            name='longitude',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=7, blank=True),
        ),
        migrations.AlterField(
            model_name='destination',
            name='category',
            field=models.SmallIntegerField(choices=[(0, b'All Categories'), (1, b'Hotels'), (2, b'Bed & Brekfasts'), (3, b'Wineries'), (4, b'Shopping'), (5, b'Food'), (6, b'Attractions')]),
        ),
        migrations.AlterField(
            model_name='destination',
            name='location',
            field=models.SmallIntegerField(choices=[(0, b'All Locations'), (1, b'Old Mission'), (2, b'Traverse City'), (3, b'Leelanau')]),
        ),
    ]
