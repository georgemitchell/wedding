# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('address', models.CharField(max_length=256)),
                ('location', models.SmallIntegerField(choices=[(1, b'Old Mission'), (2, b'Traverse City'), (3, b'Leelanau')])),
                ('category', models.SmallIntegerField(choices=[(1, b'Hotel'), (2, b'Bed & Brekfast'), (3, b'Winery'), (4, b'Shop'), (5, b'Food'), (6, b'Attraction')])),
                ('static_image', models.CharField(max_length=128)),
                ('description', models.TextField()),
            ],
        ),
    ]
