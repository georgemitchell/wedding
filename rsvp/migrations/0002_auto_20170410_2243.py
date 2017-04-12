# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='guest',
            name='meal',
            field=models.SmallIntegerField(default=0, choices=[(0, b'no preference'), (1, b'beef'), (2, b'chicken'), (3, b'vegetarian')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rsvp',
            name='location',
            field=models.TextField(blank=True),
        ),
    ]
